import { readFileSync, readdirSync, statSync } from "node:fs";
import { createRequire } from "node:module";
import { join, resolve } from "node:path";

const EXTENSIONS = /\.(ts|tsx|mts|cts|js|jsx|mjs|cjs)$/;
const SKIPPED = new Set(["node_modules", ".git", "dist", "build", "coverage", ".next", "generated"]);
const DYNAMIC_FUNCTIONS = new Set(["eval", "Function", "require"]);
const REFLECT_METHODS = new Set(["apply", "construct", "get"]);

function loadTypeScript(projectRoot) {
    try {
        return createRequire(join(projectRoot, "package.json"))("typescript");
    } catch {
        console.log("MISSING_PARSER\ttypescript is not installed in this project; ask the developer, or fall back to grep");
        process.exit(3);
    }
}

function sourceFiles(path) {
    if (statSync(path).isFile()) return EXTENSIONS.test(path) ? [path] : [];
    return readdirSync(path).filter((name) => !SKIPPED.has(name)).flatMap((name) => sourceFiles(join(path, name)));
}

function isFunction(ts, node) {
    return ts.isFunctionDeclaration(node) || ts.isMethodDeclaration(node) || ts.isArrowFunction(node)
        || ts.isFunctionExpression(node) || ts.isConstructorDeclaration(node);
}

function callFinding(ts, node, file) {
    const callee = node.expression;
    if (ts.isElementAccessExpression(callee) && !ts.isStringLiteral(callee.argumentExpression)) {
        return ["LOOKUP_CALL", `${file.text.slice(callee.pos, callee.end).trim()}(...)`];
    }
    if (ts.isIdentifier(callee) && DYNAMIC_FUNCTIONS.has(callee.text)) {
        const literal = node.arguments.length === 1 && ts.isStringLiteral(node.arguments[0]);
        return literal ? null : ["DYNAMIC_CALL", `${callee.text}(...)`];
    }
    if (ts.isPropertyAccessExpression(callee) && callee.expression.getText(file) === "Reflect"
        && REFLECT_METHODS.has(callee.name.text)) return ["DYNAMIC_CALL", `Reflect.${callee.name.text}(...)`];
    if (callee.kind === ts.SyntaxKind.ImportKeyword && !ts.isStringLiteral(node.arguments[0])) {
        return ["DYNAMIC_CALL", "import(<expression>)"];
    }
    return null;
}

function scanFile(ts, path, maxLines, findings) {
    const file = ts.createSourceFile(path, readFileSync(path, "utf8"), ts.ScriptTarget.Latest, true);
    const lineOf = (position) => file.getLineAndCharacterOfPosition(position).line + 1;
    const visit = (node) => {
        if (isFunction(ts, node) && node.body) {
            const length = lineOf(node.end) - lineOf(node.getStart(file)) + 1;
            const name = node.name ? node.name.getText(file) : "<anonymous>";
            if (length > maxLines) findings.push(`FUNCTION_LENGTH\t${path}:${lineOf(node.getStart(file))}\t${name} ${length} lines > ${maxLines}`);
        }
        if (ts.isCallExpression(node)) {
            const finding = callFinding(ts, node, file);
            if (finding) findings.push(`${finding[0]}\t${path}:${lineOf(node.getStart(file))}\t${finding[1]}`);
        }
        ts.forEachChild(node, visit);
    };
    visit(file);
}

function main() {
    const args = process.argv.slice(2);
    const limitIndex = args.indexOf("--max-function-lines");
    const maxLines = limitIndex >= 0 ? Number(args.splice(limitIndex, 2)[1]) : 80;
    const projectIndex = args.indexOf("--project");
    const projectRoot = resolve(projectIndex >= 0 ? args.splice(projectIndex, 2)[1] : ".");
    const ts = loadTypeScript(projectRoot);
    const files = args.flatMap((path) => sourceFiles(resolve(path)));
    const findings = [];
    for (const file of files) scanFile(ts, file, maxLines, findings);
    console.log(findings.length ? findings.join("\n") : "OK\tno findings");
    console.log(`SCANNED\t${files.length} JS/TS files`);
}

main();

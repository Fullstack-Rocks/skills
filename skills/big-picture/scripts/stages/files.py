"""Reading the project's YAML and JSON files: rule and view definitions, OpenAPI documents."""
import json
import shutil
import subprocess
from pathlib import Path

YAML_TO_JSON = "import json, sys, yaml; print(json.dumps(yaml.safe_load(open(sys.argv[1]))))"


def load_data(path: Path) -> object | None:
    """A JSON or YAML file; YAML through PyYAML, or uv with PyYAML when it isn't installed."""
    if path.suffix == ".json":
        return json.loads(path.read_text())
    try:
        import yaml  # noqa: PLC0415 - optional: only YAML files need it
        return yaml.safe_load(path.read_text())
    except ImportError:
        if not shutil.which("uv"):
            print(f"{path}: skipped, it is YAML and neither PyYAML nor uv is installed")
            return None
        result = subprocess.run(["uv", "run", "--no-project", "--with", "pyyaml==6.0.2", "python", "-c", YAML_TO_JSON, str(path)],
                                capture_output=True, text=True, check=False)
        return json.loads(result.stdout) if result.returncode == 0 else None


def definitions(folder: Path) -> list[tuple[Path, dict]]:
    """Every .yml, .yaml and .json definition in a .big-picture/ folder, in name order."""
    found = sorted(p for p in folder.glob("*") if p.suffix in (".yml", ".yaml", ".json")) if folder.is_dir() else []
    return [(path, data) for path in found if isinstance(data := load_data(path), dict)]

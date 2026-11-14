"""Print the SQL DDL of a project's SQLAlchemy models, for big-picture's schema stage. Run it with the
project's own Python, from a schema command in .big-picture/config.yml:

  <project python> -I {scripts}/sqlalchemy_ddl.py <package> <module:Base> [--dialect postgresql]

It imports every module of the package so every model registers, then compiles each table of the
base's metadata, and its indexes, for the dialect. It connects to nothing and writes nothing."""
import argparse
import importlib
import pkgutil

from sqlalchemy.dialects import registry
from sqlalchemy.schema import CreateIndex, CreateTable


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("package", help="the package holding the models, e.g. schemas")
    parser.add_argument("base", help="the declarative base, as module:Name, e.g. schemas.base_schemas:BaseSchema")
    parser.add_argument("--dialect", default="postgresql")
    args = parser.parse_args()
    package = importlib.import_module(args.package)
    for module in pkgutil.walk_packages(package.__path__, f"{args.package}."):
        importlib.import_module(module.name)
    module, _, name = args.base.partition(":")
    # the base is named on the command line, so it can only be looked up by that name
    metadata = getattr(importlib.import_module(module), name).metadata
    dialect = registry.load(args.dialect)()
    for table in metadata.sorted_tables:
        print(f"{str(CreateTable(table).compile(dialect=dialect)).strip()};\n")
        for index in sorted(table.indexes, key=lambda i: i.name or ""):
            print(f"{str(CreateIndex(index).compile(dialect=dialect)).strip()};\n")


if __name__ == "__main__":
    main()

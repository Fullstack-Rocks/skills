"""Read a SCIP index (protobuf) with the standard library: only the fields the graph uses.

SCIP schema (github.com/sourcegraph/scip, scip.proto): Index.documents = 2; Document.relative_path = 1,
Document.occurrences = 2; Occurrence.range = 1 (packed int32: start line, start char, [end line,] end char),
Occurrence.symbol = 2, Occurrence.symbol_roles = 3 (bit 1 = definition). Lines are 0-based.
"""
from dataclasses import dataclass
from pathlib import Path

DEFINITION = 0x1


@dataclass
class Occurrence:
    line: int  # 1-based, like lizard and ast-grep output
    symbol: str
    is_definition: bool


def varint(data: bytes, pos: int) -> tuple[int, int]:
    value, shift = 0, 0
    while True:
        byte = data[pos]
        value |= (byte & 0x7F) << shift
        pos += 1
        if byte < 0x80:
            return value, pos
        shift += 7


def fields(data: bytes):
    """Yield (field number, value) per field; length-delimited values come back as bytes."""
    pos = 0
    while pos < len(data):
        tag, pos = varint(data, pos)
        number, wire = tag >> 3, tag & 7
        size = {0: 0, 1: 8, 2: -1, 5: 4}.get(wire)
        if size is None:
            raise ValueError(f"unsupported protobuf wire type {wire}")
        if size == 0:
            value, pos = varint(data, pos)
        else:
            if size == -1:
                size, pos = varint(data, pos)
            value, pos = data[pos:pos + size], pos + size
        yield number, value


def read_index(index: Path) -> dict[str, list[Occurrence]]:
    """Occurrences per file path, relative to the indexed project. Documents and occurrences are
    decoded in place, so the reader stays two calls deep."""
    documents = {}
    for number, document in fields(index.read_bytes()):
        if number != 2:
            continue
        path, occurrences = "", []
        for doc_field, value in fields(document):
            if doc_field == 1:
                path = value.decode()
            elif doc_field == 2:
                found = dict(fields(value))  # 1: range, 2: symbol, 3: roles
                line = varint(found[1], 0)[0] + 1 if 1 in found else 0
                occurrences.append(Occurrence(line, found.get(2, b"").decode(),
                                              bool(found.get(3, 0) & DEFINITION)))
        documents[path] = occurrences
    return documents

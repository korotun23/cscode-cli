import csv
from cscode_CLI.models.record import Record 

def read_csv(path: str, delimiter: str) -> list[Record]:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return [Record(**row) for row in reader]
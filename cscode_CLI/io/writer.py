import csv
from cscode_CLI.models.record import Record

def write_csv(path: str, records: list[Record], delimiter: str):
    if not records:
        return
    
    with open(path, "w", newline="", encording="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=records[0].__dict__.keys(),
            delimiter=delimiter
        )
        writer.writeheader()

        for record in records:
            writer.writerow(record.__dict__)
import csv
from cscode_CLI.models.record import Record 
from cscode_CLI.utils.exceptions import CsvReadError

def read_csv(path: str, delimiter: str) -> list[Record]:

    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            return list(reader)
    # Error handling
    except FileNotFoundError:
        raise CsvReadError(f"File not found: {path}")
    except PermissionError:
        raise CsvReadError(f"Permission denied: {path}")
    except IsADirectoryError:
        raise CsvReadError(f"Is a directory: {path}")
    except StopIteration:
        raise CsvReadError(f"Empty file: {path}")
    except Exception as e:
        raise CsvReadError(f"Error reading CSV file: {e}")
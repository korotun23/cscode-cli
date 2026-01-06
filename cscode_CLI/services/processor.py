from cscode_CLI.io.reader import read_csv
from cscode_CLI.io.writer import write_csv

def process_csv (input_path: str, output_path: str, delimiter: str):
    records = read_csv(input_path, delimiter)
    
    # TODO: Process records
    processed = [
        r for r in records
    ]

    print(f"Records in {input_path}")
    print(processed)

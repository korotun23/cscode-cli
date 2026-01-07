from cscode_CLI.io.reader import read_csv
from cscode_CLI.io.writer import write_barcode
from cscode_CLI.services import barcode_generator
from cscode_CLI.utils.validators import validate_record
from cscode_CLI.utils.exceptions import InvalidDataError

import os

def process_csv (input_path: str, output_path: str, delimiter: str, barcode_type: str):
    
    rows = read_csv(input_path, delimiter)
    
    records = []

    for i, row in enumerate(rows, start=1):
        try:
            records.append(validate_record(row))
        except InvalidDataError as e:
            raise InvalidDataError(f"Invalid data: {e} at row {i}")

    for record in records:
        barcode = barcode_generator.generate_barcode(barcode_type, record["data"])
        path = os.path.join(output_path, record["file_name"])
        write_barcode(path, barcode)

    print(f"Records in {input_path} : {len(records)}")
    print(f"Barcodes saved to {output_path}")
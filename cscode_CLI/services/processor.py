from cscode_CLI.io.reader import read_csv
from cscode_CLI.io.writer import write_barcode
from cscode_CLI.services import barcode_generator
import os

def process_csv (input_path: str, output_path: str, delimiter: str, barcode_type: str):
    records = read_csv(input_path, delimiter)
    
    # TODO: Process records
    processed = [
        r for r in records
    ]

    for record in processed:
        barcode = barcode_generator.generate_barcode(barcode_type, record.data)
        path = os.path.join(output_path, record.file_name)
        write_barcode(path, barcode)

    print(f"Records in {input_path} : {len(processed)}")
    print(f"Barcodes saved to {output_path}")
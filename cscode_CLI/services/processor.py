import multiprocessing
from cscode_CLI.io.reader import read_csv
from cscode_CLI.io.writer import write_barcode
from cscode_CLI.services import barcode_generator
from cscode_CLI.utils.validators import validate_record
from cscode_CLI.utils.exceptions import InvalidDataError

import os
from multiprocessing import Pool
import multiprocessing

import threading
from concurrent.futures import ThreadPoolExecutor

def process_record(record: dict, width: int, height: int, barcode_type: str, output_path: str):
    try:
        barcode = barcode_generator.generate_barcode(barcode_type, width, height, record["data"])
        path = os.path.join(output_path, record["file_name"])
        write_barcode(path, barcode)
    except Exception as e:
        raise Exception(f"Error processing record {record['file_name']}: {e}")
    
    return barcode

def process_csv (input_path: str, output_path: str, delimiter: str, barcode_type: str, width: int, height: int):
    
    rows = read_csv(input_path, delimiter)
    
    records = []

    for i, row in enumerate(rows, start=1):
        try:
            records.append(validate_record(row))
        except InvalidDataError as e:
            raise InvalidDataError(f"Invalid data: {e} at row {i}")

    # Multithreading execution
    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        for record in records:
            try:
                executor.submit(process_record, record, width, height, barcode_type, output_path)
            except Exception as e:
                raise Exception(f"Error writing barcode {record['file_name']}: {e}")
        
        
        # Monoprocessing alternative
        #for record in records:
        #barcode = barcode_generator.generate_barcode(barcode_type, width, height, record["data"])
        #path = os.path.join(output_path, record["file_name"])
        #write_barcode(path, barcode) """

    print(f"Records in {input_path} : {len(records)}")
    print(f"Barcodes saved to {output_path}")
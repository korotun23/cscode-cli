import argparse
from cscode_CLI.utils.exceptions import CscodeCliError
from cscode_CLI.services.processor import process_csv
from cscode_CLI.utils.validators import validate_parameters
import sys

# CLI Entry point :
# - Parse arguments
# - Call main logic
# - Handle errors

def main():

    # Parse arguments
    parser = argparse.ArgumentParser(description="CSCODE CLI - Barcode generating tool from csv data source")
    parser.add_argument("input", help="CSV file path")
    parser.add_argument("--format", "-f", help="Barcode format")
    parser.add_argument("--width", "-sw", help="Barcode width in mm")
    parser.add_argument("--height", "-sh", help="Barcode height in mm")
    parser.add_argument("--output", "-o", help="Output directory")
    parser.add_argument("--delimiter", "-d", help="CSV delimiter")
    args = parser.parse_args()

    try:
        # Validate parameters
        validate_parameters({
            "format": args.format,
            "width": args.width,
            "height": args.height,
            "delimiter": args.delimiter
        })
        # CSV processing
        process_csv(
            input_path=args.input,
            output_path=args.output,
            delimiter=args.delimiter,
            barcode_type=args.format,
            width=args.width,
            height=args.height
        )
    except CscodeCliError as e:
        print("Error: " + str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()

    
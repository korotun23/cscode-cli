import argparse
from cscode_CLI.services.processor import process_csv

# CLI Entry point :
# - Parse arguments
# - Call main logic
# - Handle errors

def main():

    # Parse arguments
    parser = argparse.ArgumentParser(description="CSCODE CLI - Barcode generating tool from csv data source")
    parser.add_argument("input", help="CSV file path")
    parser.add_argument("--format", "-f", help="Barcode format")
    parser.add_argument("--output", "-o", help="Output directory")
    parser.add_argument("--delimiter", "-d", help="CSV delimiter")
    args = parser.parse_args()

    # CSV processing
    process_csv(
        input_path=args.input,
        output_path=args.output,
        delimiter=args.delimiter
    )

if __name__ == "__main__":
    main()

    
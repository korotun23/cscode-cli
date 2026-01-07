from cscode_CLI.utils.exceptions import InvalidDataError
import os
import re

def validate_record(row: dict):
    if "data" not in row:
        raise InvalidDataError("Missing data")

    if "file_name" not in row:
        raise InvalidDataError("Missing file_name")

    if os.path.splitext(row["file_name"])[1] not in [".png", ".jpg", ".jpeg"]:
        raise InvalidDataError("File name should end with .png or .jpg")
    
    return row

def validate_parameters(params: dict):

    # Check if width and height are real numbers
    num_pattern = "^(?:-(?:[1-9](?:\\d{0,2}(?:,\\d{3})+|\\d*))|(?:0|(?:[1-9](?:\\d{0,2}(?:,\\d{3})+|\\d*))))(?:.\\d+|)$"

    if not re.match(num_pattern, params["width"]):
        raise InvalidDataError("Width must be a positive number")

    if not re.match(num_pattern, params["height"]):
        raise InvalidDataError("Height must be a positive number")

    # Check if barcode format is valid
    if params["format"] not in ["code128", "ean13", "ean8", "upca", "upce"]:
        raise InvalidDataError("Invalid format")
    
    # Check if csv delimiter is valid
    if params["delimiter"] not in [",", ";", "\t"]:
        raise InvalidDataError("Invalid delimiter")
from cscode_CLI.utils.exceptions import InvalidDataError
import os

def validate_record(row: dict):
    if "data" not in row:
        raise InvalidDataError("Missing data")

    if "file_name" not in row:
        raise InvalidDataError("Missing file_name")

    if os.path.splitext(row["file_name"])[1] not in [".png", ".jpg", ".jpeg"]:
        raise InvalidDataError("File name should end with .png or .jpg")
    
    return row

def validate_parameters(params: dict):

    if params["format"] not in ["code128", "ean13", "ean8", "upca", "upce"]:
        raise InvalidDataError("Invalid format")
    
    if params["delimiter"] not in [",", ";", "\t"]:
        raise InvalidDataError("Invalid delimiter")
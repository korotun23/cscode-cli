class CscodeCliError(Exception):
    pass

# CSV errors
class CsvReadError(CscodeCliError):
    pass

class CsvWriteError(CscodeCliError):
    pass

class InvalidCSVStructureError(CscodeCliError):
    pass

# Barcode generation errors
class BarcodeGenerationError(CscodeCliError):
    pass

# Data errors
class InvalidDataError(CscodeCliError):
    pass

# CLI errors
class InvalidParameterError(CscodeCliError):
    pass

class InvalidBarcodeTypeError(CscodeCliError):
    pass
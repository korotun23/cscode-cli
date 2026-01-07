from PIL import Image
import treepoem

from cscode_CLI.utils.exceptions import BarcodeGenerationError

def generate_barcode(barcode_type: str, width: int, height: int, data: str) -> Image:

    # Convert width and height in mm to pixels
    width = int(width * 23.622)
    height = int(height * 23.622)

    try:
        image = treepoem.generate_barcode(
            barcode_type = barcode_type,
            data = data,
            options = {
                "scale": 5,
                "size": (width, height) 
            }
        )
    except BarcodeGenerationError:
        raise BarcodeGenerationError("Error generating barcode")

    return image

    
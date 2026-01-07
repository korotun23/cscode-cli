from PIL import Image
import treepoem

from cscode_CLI.utils.exceptions import BarcodeGenerationError

def generate_barcode(barcode_type: str, data: str) -> Image:

    try:
        image = treepoem.generate_barcode(
            barcode_type = barcode_type,
            data = data,
            options = {
                "scale": 10,
        }
    )
    except BarcodeGenerationError:
        raise BarcodeGenerationError("Error generating barcode")

    return image

    
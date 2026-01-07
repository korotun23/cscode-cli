from PIL import Image, ImageOps
import treepoem

from cscode_CLI.utils.exceptions import BarcodeGenerationError

def generate_barcode(barcode_type: str, width: int, height: int, data: str) -> Image:

    # Convert width and height in mm to pixels
    width = int(int(width) * 23.622/2)
    height = int(int(height) * 23.622/2)

    try:
        image = treepoem.generate_barcode(
            barcode_type = barcode_type,
            data = data,
            scale=5
        )
        image = ImageOps.fit(image, (width, height), Image.Resampling.BICUBIC)
    except BarcodeGenerationError:
        raise BarcodeGenerationError("Error generating barcode")

    return image

    
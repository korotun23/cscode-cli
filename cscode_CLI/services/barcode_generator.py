from PIL import Image
import treepoem


def generate_barcode(barcode_type: str, data: str) -> Image:

    image = treepoem.generate_barcode(
        barcode_type = barcode_type,
        data = data,
        options = {
            "scale": 10,
        }
    )

    return image

    
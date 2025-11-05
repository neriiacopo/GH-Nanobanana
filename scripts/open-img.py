"""Grasshopper Script"""
# requirements: pillow

import base64
from io import BytesIO
from PIL import Image

p = P

def image_to_base64(img: Image.Image, format: str = "PNG") -> str:

    buffer = BytesIO()
    img.save(buffer, format=format)
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")

img = Image.open(p)
D = image_to_base64(img)
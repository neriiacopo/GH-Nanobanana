"""Grasshopper Script"""
# requirements: pillow, google-genai

import os
import Rhino
import System
import base64
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from base64 import b64encode, b64decode


if r == "":
    R = "1:1" 
else:
    R=r

if not f : f = "temp.png"

INPUT_MIX = I
IMAGE_MODEL = "gemini-2.5-flash-image"

script_dir =  os.path.dirname(ghdoc.Path)
output_path = os.path.join(script_dir,f)

INPUT = []
for i in INPUT_MIX:
    try:
        img = Image.open(BytesIO(b64decode(i)))
        INPUT.append(img)
    except:
        INPUT.append(i)


if run == True :
    client = genai.Client(api_key=K)

    response = client.models.generate_content(
        model=IMAGE_MODEL,
        contents=INPUT,
        config=types.GenerateContentConfig(
            response_modalities=["Image"],
            image_config=types.ImageConfig(
                aspect_ratio=R,
            )
        )
    )

    if response.candidates:
        for i, candidate in enumerate(response.candidates):
            for part in candidate.content.parts:
                
                if part.inline_data is not None:
                    
                    image_data = part.inline_data.data
                    image = Image.open(BytesIO(image_data))

                    filename = output_path
                    image.save(filename)
                    print(f"Successfully generated and saved image: {filename}")

                    P = filename

    else:
        print("Image generation failed or returned no candidates.")

    client.close()

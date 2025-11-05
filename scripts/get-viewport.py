"""Grasshopper Script"""

import os
import Rhino
import System
import base64
from io import BytesIO
from base64 import b64encode, b64decode

v = V

if v != None:
    VIEWPORT = v

    view = Rhino.RhinoDoc.ActiveDoc.Views.Find(VIEWPORT, False)
    if not view:
        raise ValueError(f"Viewport '{VIEWPORT}' not found.")

    # Capture viewport as bitmap
    size = view.ActiveViewport.Size
    bitmap = view.CaptureToBitmap(System.Drawing.Size(size.Width, size.Height))

    # Convert to PNG bytes in memory using .NET stream
    stream = System.IO.MemoryStream()
    bitmap.Save(stream, System.Drawing.Imaging.ImageFormat.Png)
    byte_data = bytearray(stream.ToArray())  # Convert .NET byte[] → Python bytes
    stream.Close()

    b64img = base64.b64encode(byte_data).decode("utf-8")

    D = b64img
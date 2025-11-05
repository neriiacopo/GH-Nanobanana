# GH-Nanobanana

GH-Nanobanana is a Grasshopper script for Rhino that connects to Google Gemini (Nanobanana) to generate images using prompts and images captured from the Rhino viewport.

## Overview

The script revolves around one main Python component (open) that sends requests to the Google GenAI API. It provides three different image generation pipelines:

1. **Prompt to Image**: Generate images directly from text prompts
2. **Viewport to Image**: Generate images using the current Rhino viewport as input
3. **Viewport to Image with Post-processing**: Generate images from the viewport, then use the generated image as input for another generation cycle
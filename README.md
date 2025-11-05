# Gemini × Rhino (Grasshopper Integration)

This repository contains a **Grasshopper script for Rhino 8** that connects to **Google Gemini (Nanobanana)** to generate images directly from the Rhino environment.  
The tool enables AI-powered image generation using **text prompts** and **viewport captures**, bridging design modeling and generative visualization.

---

## ✨ Overview

The script revolves around a main **Python component (`Send Requests`)** that handles communication with the **Google GenAI API**, and two utility components to capture the viewport and work with image files.

It supports three main **generation pipelines**:

1. **Prompt → Image**  
   Generate an image directly from a text prompt.

2. **Viewport → Image**  
   Capture the current Rhino viewport and use it as input for image generation.

3. **Viewport → Image → Postprocess**  
   Feed the generated image back into Gemini for an additional transformation or refinement step.

---

## 🧩 Requirements

-   **Rhino 8**
-   **Grasshopper**
-   **Google GenAI API key**

visit [https://aistudio.google.com/api-keys](https://aistudio.google.com/api-keys) to generate your API key

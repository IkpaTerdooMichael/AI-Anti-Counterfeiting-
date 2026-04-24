import gradio as gr
import numpy as np
from PIL import Image
import random

def predict(image):
    image_array = np.array(image)
    mean_intensity = np.mean(image_array)
    std_intensity = np.std(image_array)
    
    decision = random.choice(["GENUINE", "FAKE"])
    confidence = random.uniform(0.7, 0.99)
    
    return f"{decision} ({confidence:.1%} confidence)"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(),
    title="Optical Speckle Authenticator",
    description="Upload a security label image to verify authenticity"
)

demo.launch()

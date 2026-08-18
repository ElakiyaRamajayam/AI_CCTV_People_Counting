import streamlit as st
import torch
from ultralytics import YOLO


@st.cache_resource
def load_model():

    # Highest accuracy YOLOv8 model
    model = YOLO("yolov8x.pt")

    if torch.cuda.is_available():

        model.to("cuda")

        print(
            "✅ YOLO running on GPU:",
            torch.cuda.get_device_name(0)
        )

    else:

        print("⚠️ CUDA not available. Running on CPU.")

    return model
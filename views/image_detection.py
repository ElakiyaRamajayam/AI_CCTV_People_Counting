import streamlit as st
import numpy as np
import cv2
import time
import os

from PIL import Image

from models.yolo_model import load_model
from utils.drawing import draw_people_count


model = load_model()


def image_detection():

    st.title("🖼️ Human Detection & Counting")

    st.write(
        "Upload an image to detect and count people."
    )

    confidence = st.slider(
        "Confidence Threshold",
        0.05,
        0.90,
        0.25,
        0.05
    )

    img_size = st.selectbox(
        "Image Size",
        [640, 960, 1280, 1600, 1920],
        index=4
    )

    uploaded_image = st.file_uploader(
        "Upload an Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    if uploaded_image is None:
        return

    image = Image.open(uploaded_image).convert("RGB")

    img = np.array(image)

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            image,
            caption="Original Image",
            use_container_width=True
        )

    start = time.time()

    results = model.predict(
        source=img,
        device=0,
        classes=[0],
        conf=confidence,
        imgsz=img_size,
        iou=0.45,
        max_det=1000,
        agnostic_nms=False,
        augment=True,
        verbose=False
    )

    end = time.time()

    result = results[0]

    person_count = len(result.boxes)

    annotated = result.plot(
        line_width=2,
        font_size=12
    )

    annotated = cv2.cvtColor(
        annotated,
        cv2.COLOR_BGR2RGB
    )

    annotated = draw_people_count(
        annotated,
        person_count
    )

    with col2:

        st.image(
            annotated,
            caption="Detection Result",
            use_container_width=True
        )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "👥 People Detected",
            person_count
        )

    with c2:

        st.metric(
            "Confidence",
            f"{confidence:.2f}"
        )

    with c3:

        st.metric(
            "Processing Time",
            f"{end-start:.2f} sec"
        )

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    output_path = "outputs/result.jpg"

    cv2.imwrite(
        output_path,
        cv2.cvtColor(
            annotated,
            cv2.COLOR_RGB2BGR
        )
    )

    with open(output_path, "rb") as file:

        st.download_button(
            "📥 Download Result",
            file,
            file_name="Human_Detection_Result.jpg",
            mime="image/jpeg"
        )
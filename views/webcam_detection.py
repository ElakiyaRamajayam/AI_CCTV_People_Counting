import streamlit as st
import cv2
import time

from models.yolo_model import load_model
from utils.drawing import draw_people_count


model = load_model()


def webcam_detection():

    st.title("Live Camera Detection")

    confidence = st.slider(
        "Confidence",
        0.10,
        0.90,
        0.25,
        0.05
    )

    start = st.checkbox("Start Camera")

    # Live people count
    count_placeholder = st.empty()

    FRAME_WINDOW = st.empty()

    if start:

        camera = cv2.VideoCapture(0)

        if not camera.isOpened():
            st.error("Camera not detected")
            return

        while start:

            ret, frame = camera.read()

            if not ret:
                st.error("Cannot read camera")
                break

            results = model.predict(
                source=frame,
                device=0,
                classes=[0],
                conf=confidence,
                imgsz=960,
                iou=0.45,
                max_det=300,
                verbose=False
            )

            result = results[0]

            people = len(result.boxes)

            # Show live count on the page
            count_placeholder.metric(
                "Current People",
                people
            )

            annotated = result.plot()

            # No text will be drawn because draw_people_count() returns the frame unchanged
            annotated = draw_people_count(
                annotated,
                people
            )

            FRAME_WINDOW.image(
                cv2.cvtColor(
                    annotated,
                    cv2.COLOR_BGR2RGB
                ),
                channels="RGB"
            )

            time.sleep(0.03)

        camera.release()
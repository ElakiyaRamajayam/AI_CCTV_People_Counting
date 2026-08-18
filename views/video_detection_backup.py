import streamlit as st
import cv2
import os
import tempfile
import time
import subprocess

from models.yolo_model import load_model
from utils.drawing import draw_people_count


model = load_model()



def video_detection():


    st.title("Video Human Detection")


    confidence = st.slider(
        "Confidence Threshold",
        0.10,
        0.90,
        0.25,
        0.05
    )


    uploaded_video = st.file_uploader(

        "Upload Video",

        type=[
            "mp4",
            "avi",
            "mov",
            "mkv"
        ]

    )


    if uploaded_video is None:

        return



    # Original video preview

    st.video(uploaded_video)



    if st.button("Start Detection"):


        os.makedirs(
            "outputs",
            exist_ok=True
        )


        temp_video = tempfile.NamedTemporaryFile(

            delete=False,

            suffix=".mp4"

        )


        temp_video.write(
            uploaded_video.read()
        )


        temp_video.close()



        cap = cv2.VideoCapture(
            temp_video.name
        )


        if not cap.isOpened():

            st.error(
                "Cannot open video file"
            )

            return



        width = int(
            cap.get(
                cv2.CAP_PROP_FRAME_WIDTH
            )
        )


        height = int(
            cap.get(
                cv2.CAP_PROP_FRAME_HEIGHT
            )
        )


        fps = cap.get(
            cv2.CAP_PROP_FPS
        )


        if fps == 0:

            fps = 25



        output_path = (
            "outputs/detected_video.avi"
        )


        fourcc = cv2.VideoWriter_fourcc(
            *"XVID"
        )


        writer = cv2.VideoWriter(

            output_path,

            fourcc,

            fps,

            (width, height)

        )



        if not writer.isOpened():

            st.error(
                "Video writer failed"
            )

            cap.release()

            return



        max_people = 0


        start = time.time()



        frame_total = int(
            cap.get(
                cv2.CAP_PROP_FRAME_COUNT
            )
        )


        frame_number = 0


        progress = st.progress(0)



        with st.spinner(
            "Processing video..."
        ):


            while True:


                ret, frame = cap.read()


                if not ret:

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


                people = len(
                    result.boxes
                )


                max_people = max(
                    max_people,
                    people
                )


                annotated = result.plot()



                annotated = draw_people_count(

                    annotated,

                    people

                )



                writer.write(
                    annotated
                )


                frame_number += 1



                if frame_total > 0:

                    progress.progress(

                        min(

                            frame_number / frame_total,

                            1.0

                        )

                    )



        cap.release()

        writer.release()



        # Convert AVI to browser compatible MP4

        final_video = (
            "outputs/final_video.mp4"
        )


        subprocess.run(

            [

                "ffmpeg",

                "-y",

                "-i",

                output_path,

                "-vcodec",

                "libx264",

                "-pix_fmt",

                "yuv420p",

                final_video

            ],

            stdout=subprocess.DEVNULL,

            stderr=subprocess.DEVNULL

        )



        end = time.time()



        st.success(
            "Video Detection Completed"
        )



        st.video(
            final_video
        )



        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Maximum People",
                max_people
            )


        with col2:

            st.metric(
                "Confidence",
                f"{confidence:.2f}"
            )


        with col3:

            st.metric(
                "Processing Time",
                f"{end-start:.2f} sec"
            )



        with open(

            final_video,

            "rb"

        ) as file:


            st.download_button(

                "Download Processed Video",

                file,

                file_name="detected_video.mp4",

                mime="video/mp4"

            )



        os.remove(
            temp_video.name
        )
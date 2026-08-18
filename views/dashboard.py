import streamlit as st

from components.cards import metric_card



def dashboard():


    st.title(
        "AI CCTV Monitoring Dashboard"
    )


    st.caption(
        "Human Detection and Occupancy Monitoring System"
    )


    st.divider()



    # ================================
    # STATUS CARDS
    # ================================


    col1, col2, col3, col4 = st.columns(4)



    with col1:

        metric_card(

            "CURRENT PEOPLE",

            "0",

            "Live Detection"

        )



    with col2:

        metric_card(

            "TOTAL IN",

            "0",

            "Entry Count"

        )



    with col3:

        metric_card(

            "TOTAL OUT",

            "0",

            "Exit Count"

        )



    with col4:

        metric_card(

            "CAMERA STATUS",

            "Offline",

            "System State"

        )



    st.divider()



    # ================================
    # MAIN AREA
    # ================================


    left, right = st.columns(
        [3,1]
    )


    with left:


        st.subheader(
            "Live Detection Preview"
        )


        preview = st.container(
            height=500
        )


        with preview:

            st.info(
                "Camera feed will appear here"
            )



    with right:


        st.subheader(
            "System Information"
        )


        st.success(
            "AI Model Ready"
        )


        st.success(
            "GPU Enabled"
        )


        st.success(
            "CUDA Enabled"
        )


        st.info(
            "Model: YOLO"
        )


        st.info(
            "Camera: Offline"
        )
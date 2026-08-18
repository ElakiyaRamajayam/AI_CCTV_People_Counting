import streamlit as st

from components.sidebar import create_sidebar

from views.dashboard import dashboard
from views.image_detection import image_detection
from views.video_detection import video_detection
from views.webcam_detection import webcam_detection
from views.reports import reports
from views.settings import settings


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI CCTV People Counting",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# LOAD CSS
# =====================================================

def load_css():

    try:

        with open("styles/style.css", "r") as css:

            st.markdown(
                f"""
                <style>
                {css.read()}
                </style>
                """,
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        st.warning("CSS file not found")


load_css()


# =====================================================
# SIDEBAR
# =====================================================

selected = create_sidebar()


# =====================================================
# PAGE ROUTING
# =====================================================

if selected == "Dashboard":

    dashboard()


elif selected == "Image Detection":

    image_detection()


elif selected == "Video Detection":

    video_detection()


elif selected == "Live Camera":

    webcam_detection()


elif selected == "Reports":

    reports()


elif selected == "Settings":

    settings()
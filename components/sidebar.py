import streamlit as st
from streamlit_option_menu import option_menu


def create_sidebar():

    with st.sidebar:

        st.markdown(
            "## AI CCTV"
        )

        st.caption(
            "People Counting System"
        )


        selected = option_menu(

            menu_title=None,

            options=[
                "Dashboard",
                "Image Detection",
                "Video Detection",
                "Live Camera",
                "Reports",
                "Settings"
            ],

            icons=[
                "speedometer2",
                "image",
                "camera-video",
                "camera",
                "bar-chart",
                "gear"
            ],

            default_index=0,


            styles={

                "container": {
                    "padding": "0",
                    "background-color": "#111827"
                },


                "icon": {
                    "color": "#94A3B8",
                    "font-size": "16px"
                },


                "nav-link": {

                    "font-size": "15px",
                    "color": "#CBD5E1",
                    "margin": "6px 0",
                    "border-radius": "10px"

                },


                "nav-link:hover": {

                    "background-color": "#1E293B",
                    "color": "#FFFFFF"

                },


                "nav-link-selected": {

                    "background-color": "#2563EB",
                    "color": "white"

                }

            }

        )


        st.divider()


        st.caption(
            "GPU Accelerated\nYOLO Detection System"
        )


        return selected
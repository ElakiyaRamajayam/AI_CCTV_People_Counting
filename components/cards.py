import streamlit as st


def metric_card(title, value, subtitle):

    st.markdown(
        f"""
        **{title}**

        # {value}

        {subtitle}
        """
    )
import streamlit as st
import time
from datetime import datetime, timedelta

def introduction():
    # with st.session_state["sidebar"]:
    st.markdown("<h1 style='text-align: center;'>Welcome to my small corner of the internet</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>You have some how or way navigated here, so you might as well get in touch</h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    left, middle, right = st.columns(3)
    with left:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/rayleighxu7/", type="secondary", use_container_width=True)
    with middle:
        st.link_button("GitHub", "https://github.com/rayleighxu7", type="secondary", use_container_width=True)
    with right:
        st.link_button("Email", "mailto:rayleighxu7@live.com", type="secondary", use_container_width=True)
    st.markdown("---")

def about():
    st.markdown("<h2 style='text-align: center;'>About Me</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>I'm Rayleigh, a data analyst/engineer/scientist whatever you want to call it. Hungry to grow, obsessed with success and unfazed by failure", unsafe_allow_html=True)
    # st.image("images/cv.png")
    st.markdown("---")

def clock():
    with st.empty():
        def time_until_april_16():
            now = datetime.now()
            st.write(now)
            target = datetime(now.year, 4, 16)  # Set target to April 16 of the current year

            # If April 16 has already passed this year, calculate for the next year
            if now > target:
                target = datetime(now.year + 1, 4, 16)

            time_diff = target - now

            months = (target.year - now.year) * 12 + (target.month - now.month)
            if now.day > target.day:
                months -= 1
                last_month = target.replace(month=target.month - 1 if target.month > 1 else 12)
                days = (target - last_month).days - now.day + target.day
            else:
                days = target.day - now.day

            seconds = time_diff.seconds
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)

            return months, days, f"{hours:02}", f"{minutes:02}", f"{seconds:02}"
        while True:
            months, days, hours, minutes, seconds = time_until_april_16()
            st.markdown(f"<div style='text-align: center;'>Born Day Countdown {months}:{days}:{hours}:{minutes}:{seconds}", unsafe_allow_html=True)
            time.sleep(1)

def _setup():
    st.set_page_config(
        page_title="Rayleigh's Corner",
        page_icon="images/2842-stressedpsyduck.png",
        initial_sidebar_state="expanded",
    )

    st.markdown("""<style>#MainMenu {visibility: hidden;}</style>""", unsafe_allow_html=True)
    hide_streamlit_style = """
                    <style>
                    div[data-testid="stToolbar"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }
                    div[data-testid="stDecoration"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }
                    div[data-testid="stStatusWidget"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }
                    #MainMenu {
                    visibility: hidden;
                    height: 0%;
                    }
                    header {
                    visibility: hidden;
                    height: 0%;
                    }
                    footer {
                    visibility: hidden;
                    height: 0%;
                    }
                    </style>
                    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if __name__ == "__main__":
    _setup()
    introduction()
    about()
    clock()
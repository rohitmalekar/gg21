import streamlit as st
import datetime

# Set page config
st.set_page_config(page_title="Coming Soon", page_icon="🚀", layout="centered")

# Custom CSS to style the app
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stTitle {
        color: #1e3a8a;
        font-size: 3rem !important;
    }
    .stSubheader {
        color: #374151;
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.title("🚀 GrantsScope for GG21 Coming Soon!")
st.subheader("Launches on August 8th - within 1 day after donations begin.")

# Countdown timer
launch_date = datetime.datetime(2024, 08, 07, 23, 59, 59)  # Set your launch date here
current_time = datetime.datetime.now()
time_left = launch_date - current_time

days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

st.write(f"Time until launch: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# Progress bar
progress = st.progress(0)
progress.progress(int((current_time - datetime.datetime.now()).total_seconds() / (launch_date - datetime.datetime.now()).total_seconds() * 100))

import streamlit as st
import datetime

# Set page config
st.set_page_config(page_title="Coming Soon", page_icon="🚀", layout="centered")

# Main content
st.title("🚀 GrantsScope for GG21 - Coming Soon!")
st.subheader("Launches on August 8th - within 1 day after donations begin.")

st.markdown("Check out grantsscope.xyz for the product journey over the last year!")

# Countdown timer
launch_date = datetime.datetime(2024, 8, 7, 23, 59, 59)  # Set your launch date here
current_time = datetime.datetime.now()
time_left = launch_date - current_time

days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

st.write(f"Time until launch: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")


import streamlit as st
import datetime

# Set page config
st.set_page_config(page_title="Coming Soon", page_icon="🚀", layout="centered")

# Main content
st.title("🚀 GrantsScope for GG21")
st.subheader("Launches on August 8th")

# Countdown timer
launch_date = datetime.datetime(2024, 8, 7, 23, 59, 59)  # Set your launch date here
current_time = datetime.datetime.now()
time_left = launch_date - current_time

days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

st.info(f"Time until launch: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

st.markdown("Check out [grantsscope.xyz](grantsscope.xyz) or the project's [Karma GAP page](https://gap.karmahq.xyz/project/grantsscope---grantee-discovery-using-llms) for the product journey over the last year!")

col1, col2, col3 = st.columns(3)

col1.markdown("## GG20")
col1.markdown("In GG20, GrantsScope used conversational experience to help self-discovery of grnatees led by user inquiries.")
col1.link_button("View app", "https://all-about-gg20.streamlit.app/")
col1.image("https://grantsscope.xyz/wp-content/uploads/2024/04/screenshot-2024-04-29-at-2.26.44-pm.png")

col1.markdown("In Gitcoin Citizens Round 3, GrantsScope utilized historical donor decisions to create personalized recommendations for donors.")
col2.image("https://grantsscope.xyz/wp-content/uploads/2024/04/screenshot-2024-04-09-at-11.58.53-am.png")

col3.image("https://grantsscope.xyz/wp-content/uploads/2024/03/zoom-in.gif")

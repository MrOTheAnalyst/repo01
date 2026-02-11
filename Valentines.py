# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 22:38:24 2026

@author: ompha
"""

import streamlit as st
import time

st.set_page_config(page_title="Happy Valentine's", page_icon="💖")
st.title("💌 Happy Valentine's Day 💌")
st.write("Today is about YOU ❤️")

# List of romantic messages
messages = [
    "You are the first thing on my mind this morning 💭",
    "Your smile lights up my day 😊",
    "Every moment with you feels magical ✨",
    "I can't wait to create more memories with you 🥰",
    "You make my heart skip a beat ❤️"
]

# Show messages one by one
for msg in messages:
    st.write(msg)
    time.sleep(2)  # pauses for 2 seconds for effect

# The big surprise button
if st.button("💖 Open your surprise 💖"):
    st.markdown("### 🎉 YOU ARE AMAZING 🎉")
    st.markdown("I hope your day is as incredible as your smile 😘")
    st.markdown("💌💌💌💌💌")
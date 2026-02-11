# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 22:38:24 2026

@author: ompha
"""

import streamlit as st
import time

# ------------------------------
# PAGE SETUP
# ------------------------------
st.set_page_config(page_title="💖 Happy Valentine's Day 💖", page_icon="💌", layout="centered")

# Custom CSS for background gradient, fonts, and styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #ffc1cc, #ffe0e6);
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #800020;
        text-align: center;
    }
    .big-title {
        font-size: 48px;
        font-weight: bold;
        margin-top: 20px;
    }
    .message {
        font-size: 28px;
        margin: 20px 0;
        transition: all 1s ease-in-out;
    }
    .surprise {
        font-size: 36px;
        margin-top: 30px;
        color: #ff1493;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="big-title">💌 Happy Valentine\'s Day 💌</h1>', unsafe_allow_html=True)
st.markdown('<h3>Today is all about YOU ❤️</h3>', unsafe_allow_html=True)

# ------------------------------
# ROMANTIC MESSAGES
# ------------------------------
messages = [
    "You are the first thing on my mind this morning 💭",
    "Your smile lights up my world 🌸",
    "Every moment with you feels magical ✨",
    "I can't wait to make more memories with you 🥰",
    "You make my heart skip a beat ❤️"
]

placeholder = st.empty()  # container for slow message reveal

for msg in messages:
    placeholder.markdown(f'<p class="message">{msg}</p>', unsafe_allow_html=True)
    time.sleep(2)  # pause between messages

# ------------------------------
# BIG SURPRISE BUTTON
# ------------------------------
if st.button("💖 Open Your Surprise 💖"):
    st.markdown('<h2 class="surprise">🎉 YOU ARE AMAZING 🎉</h2>', unsafe_allow_html=True)
    st.markdown('<h3>I hope your day is as incredible as your smile 😘</h3>', unsafe_allow_html=True)
    st.markdown('<h1>💌💌💌💌💌</h1>', unsafe_allow_html=True)
    
    # Cute GIF for maximum effect
    st.image("https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif", use_column_width=True)

    # Optional: add more floating hearts or emojis
    st.markdown('<h1>💖🌸💖🌸💖</h1>', unsafe_allow_html=True)

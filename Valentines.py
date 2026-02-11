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
st.set_page_config(page_title="💖 Mr. O's Valentine 💖", page_icon="💌", layout="centered")

# Custom CSS for full background and styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #ffafbd, #ffc3a0);
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #800020;
        text-align: center;
    }
    .big-title {
        font-size: 60px;
        font-weight: bold;
        margin-top: 50px;
    }
    .subheading {
        font-size: 36px;
        margin-bottom: 40px;
    }
    .yes-button {
        font-size: 50px !important;
        padding: 30px 60px !important;
        background-color: #ff1493 !important;
        color: white !important;
        border-radius: 20px !important;
    }
    .message {
        font-size: 32px;
        margin: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# TITLE + SUBHEADING
# ------------------------------
st.markdown('<h1 class="big-title">Mr. O</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subheading">Will you be my Valentine? 💌</h2>', unsafe_allow_html=True)

# ------------------------------
# YES BUTTON
# ------------------------------
if st.button("YES! 💖", key="yes_button"):
    # BIG ROMANTIC REVEAL
    st.balloons()  # Streamlit balloons for fun effect
    st.markdown('<h2 class="message">OMG 😍 You said YES!</h2>', unsafe_allow_html=True)
    st.markdown('<h2 class="message">I can’t wait to spend more magical moments with you 🥰</h2>', unsafe_allow_html=True)
    st.markdown('<h2 class="message">You make my heart skip a beat ❤️🌸</h2>', unsafe_allow_html=True)
    
    # GIF + emojis for max effect
    st.image("https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif", use_column_width=True)
    st.markdown('<h1>💖💌🌹💖💌🌹💖</h1>', unsafe_allow_html=True)

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

# ------------------------------
# CUSTOM CSS (background + fonts + buttons)
# ------------------------------
st.markdown(
    """
    <style>
    /* Full background gradient */
    .stApp {
        background: linear-gradient(to bottom right, #ffafbd, #ffc3a0);
        background-attachment: fixed;
    }
    /* Big Title */
    .big-title {
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
        color: #800020;
    }
    /* Subheading */
    .subheading {
        font-size: 36px;
        text-align: center;
        margin-bottom: 40px;
        color: #800020;
    }
    /* YES button */
    div.stButton > button {
        font-size: 50px;
        padding: 30px 60px;
        background-color: #ff1493;
        color: white;
        border-radius: 20px;
        border: none;
    }
    /* Romantic messages */
    .message {
        font-size: 32px;
        margin: 20px 0;
        text-align: center;
        color: #800020;
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
    
    # BALLONS FOR FUN
    st.balloons()
    
    # ROMANTIC MESSAGES APPEARING SLOWLY
    messages = [
        "OMG 😍 You said YES!",
        "I can’t wait to spend more magical moments with you 🥰",
        "You make my heart skip a beat ❤️",
        "Every day with you feels like a dream 🌸",
        "I LOVE YOU 💌"
    ]
    
    placeholder = st.empty()
    for msg in messages:
        placeholder.markdown(f'<p class="message">{msg}</p>', unsafe_allow_html=True)
        time.sleep(2)  # slow reveal

    # GIF OF "I LOVE YOU"
    st.image("https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif", use_column_width=True)

    # EXTRA HEARTS AND FLOWERS
    st.markdown('<h1>💖💌🌹💖💌🌹💖</h1>', unsafe_allow_html=True)

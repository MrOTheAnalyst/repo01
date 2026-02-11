# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 22:38:24 2026

@author: ompha
"""

import streamlit as st
import time

# Page setup
st.set_page_config(page_title="💖 Mr. O's Valentine 💖", page_icon="💌", layout="centered")

# Custom CSS
st.markdown("""
<style>
/* Background gradient */
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
/* YES Button */
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
/* Floating hearts animation */
@keyframes floatUp {
    0% { transform: translateY(100vh) translateX(0px); opacity: 1; }
    100% { transform: translateY(-10vh) translateX(50px); opacity: 0; }
}
.floating {
    position: fixed;
    font-size: 30px;
    animation: floatUp 6s linear infinite;
}
</style>
""", unsafe_allow_html=True)

# Title and subheading
st.markdown('<h1 class="big-title">Mr. O</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subheading">Will you be my Valentine? 💌</h2>', unsafe_allow_html=True)

# YES button
if st.button("YES! 💖"):
    
    # Floating hearts
    st.markdown("""
    <div class="floating" style="left:10%;">💖</div>
    <div class="floating" style="left:30%; animation-delay: 1s;">🌸</div>
    <div class="floating" style="left:50%; animation-delay: 2s;">💌</div>
    <div class="floating" style="left:70%; animation-delay: 3s;">🌹</div>
    <div class="floating" style="left:90%; animation-delay: 4s;">💖</div>
    """, unsafe_allow_html=True)

    # Balloons
    st.balloons()

    # Slow message reveal
    messages = [
        "OMG 😍 You said YES!",
        "I can’t wait to spend more magical moments with you 🥰",
        "You make my heart skip a beat ❤️",
        "Every second with you feels like a dream 🌸",
        "This song is for you… 💌"
    ]
    placeholder = st.empty()
    for msg in messages:
        placeholder.markdown(f'<p class="message">{msg}</p>', unsafe_allow_html=True)
        time.sleep(2)

    # Embed YouTube music video for "Nawe" by Simmy
    st.video("https://www.youtube.com/watch?v=L7wXeG1aYQQ")

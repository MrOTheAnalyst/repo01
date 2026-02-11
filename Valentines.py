# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 22:38:24 2026

@author: ompha
"""

import streamlit as st
import random
import time

st.set_page_config(
    page_title="💘 Mr. O",
    page_icon="❤️",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS (ROMANTIC THEME)
# -----------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #5f0a87, #a4508b);
    overflow: hidden;
}

.main {
    background: transparent;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 50px;
    border-radius: 25px;
    text-align: center;
    color: white;
    box-shadow: 0px 15px 50px rgba(0,0,0,0.4);
    backdrop-filter: blur(12px);
    animation: fadeIn 1.2s ease-in-out;
}

h1, h2, h3 {
    text-shadow: 0px 0px 25px rgba(255,255,255,0.6);
}

button[kind="primary"] {
    background-color: #ff4d6d !important;
    border-radius: 30px !important;
    height: 3em;
    width: 12em;
    font-weight: bold;
    font-size: 18px;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(30px);}
    to {opacity: 1; transform: translateY(0);}
}

.heart {
    position: fixed;
    bottom: -50px;
    font-size: 22px;
    animation: floatUp 7s linear infinite;
    color: pink;
}

@keyframes floatUp {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(-110vh); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# BACKGROUND MUSIC
# -----------------------------
try:
    audio_file = open("iloveyou.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")
except:
    st.warning("Add 'iloveyou.mp3' to project folder for background music 🎵")

# -----------------------------
# FLOATING HEARTS
# -----------------------------
for i in range(20):
    left = random.randint(0, 100)
    delay = random.uniform(0, 5)
    st.markdown(
        f"""
        <div class="heart" style="left:{left}%; animation-delay:{delay}s;">
            ❤️
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# LOVE MESSAGES
# -----------------------------
LOVE_MESSAGES = [
    "Loving you was never a question.",
    "It was patience.",
    "It was timing.",
    "Trusting life would meet us halfway.",
    "You are my peace.",
    "My safe place.",
    "My heart.",
    "You feel like home.",
    "Every day with you feels intentional.",
    "This isn't a moment.",
    "It's a continuation.",
    "You are my answered prayer.",
    "My forever starts with you."
]

def get_random_message():
    return random.choice(LOVE_MESSAGES)

# -----------------------------
# SESSION CONTROL
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

# -----------------------------
# SCREEN 1 — PROPOSAL
# -----------------------------
if st.session_state.step == 1:

    st.markdown("""
    <div class="card">
        <h1>For You ❤️</h1>
        <h2>Will you be my Valentine?</h2>
        <br>
        <p>— Mr. O 💌</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("YES 💖", type="primary"):
        st.session_state.step = 2
        st.rerun()

# -----------------------------
# SCREEN 2 — ONE MORE THING
# -----------------------------
elif st.session_state.step == 2:

    st.markdown("""
    <div class="card">
        <h2>One More Thing… ✨</h2>
        <p>A special message from Mr. O is waiting for you.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("READ YOUR LETTER 💌", type="primary"):
        st.session_state.step = 3
        st.rerun()

# -----------------------------
# SCREEN 3 — AUTO LOVE MODE
# -----------------------------
elif st.session_state.step == 3:

    placeholder = st.empty()

    st.balloons()

    for i in range(1000):  # long romantic loop
        message = get_random_message()

        placeholder.markdown(f"""
            <div class="card">
                <h2>❤️</h2>
                <h3>{message}</h3>
                <br>
                <p>Forever Yours,</p>
                <h3>Mr. O 💍</h3>
            </div>
        """, unsafe_allow_html=True)

        time.sleep(4)

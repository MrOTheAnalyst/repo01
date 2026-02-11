# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 22:38:24 2026

@author: ompha
"""

import streamlit as st
import random
import time

st.set_page_config(page_title="💘 Mr. O", layout="centered")

# -------------------------
# BACKGROUND STYLE
# -------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #5f0a87, #a4508b);
    overflow: hidden;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 60px;
    border-radius: 25px;
    text-align: center;
    color: white;
    box-shadow: 0px 20px 60px rgba(0,0,0,0.4);
    backdrop-filter: blur(12px);
    animation: fadeIn 1.5s ease-in-out;
}

h1, h2, h3 {
    text-shadow: 0px 0px 25px rgba(255,255,255,0.7);
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(30px);}
    to {opacity: 1; transform: translateY(0);}
}

/* 🌸 FLOWERS */
.flower {
    position: fixed;
    top: -50px;
    font-size: 25px;
    animation: fall 8s linear infinite;
}

@keyframes fall {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(110vh); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 🎵 BACKGROUND MUSIC (RAW GITHUB LINK)
# -------------------------
st.audio(
    "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/iloveyou.mp3",
    format="audio/mp3"
)

# -------------------------
# 🌸 FLOATING FLOWERS
# -------------------------
flowers = ["🌸", "🌺", "🌷", "💐"]

for i in range(25):
    left = random.randint(0, 100)
    delay = random.uniform(0, 5)
    flower = random.choice(flowers)

    st.markdown(
        f"""
        <div class="flower" style="left:{left}%; animation-delay:{delay}s;">
            {flower}
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------
# LOVE MESSAGES
# -------------------------
LOVE_MESSAGES = [
    "Loving you was never a question.",
    "It was patience.",
    "It was timing.",
    "You are my peace.",
    "My safe place.",
    "My heart.",
    "You feel like home.",
    "This isn't a moment.",
    "It's a continuation.",
    "Forever starts with you.",
    "Every day with you feels intentional.",
    "You are my answered prayer."
]

# -------------------------
# SESSION STATE
# -------------------------
if "start" not in st.session_state:
    st.session_state.start = False

# -------------------------
# FIRST SCREEN
# -------------------------
if not st.session_state.start:

    st.markdown("""
    <div class="card">
        <h1>For You ❤️</h1>
        <h2>Will you be my Valentine?</h2>
        <br>
        <p>— Mr. O 💌</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("YES 💖"):
        st.session_state.start = True
        st.rerun()

# -------------------------
# LOVE MESSAGE SCREEN
# -------------------------
else:

    placeholder = st.empty()
    st.balloons()

    for i in range(1000):

        message = random.choice(LOVE_MESSAGES)

        placeholder.markdown(f"""
        <div class="card">
            <h2>❤️</h2>
            <h3>{message}</h3>
            <br>
            <p>Forever Yours,</p>
            <h2>Mr. O 💍</h2>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(4)

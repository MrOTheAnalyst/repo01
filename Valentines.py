# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 22:38:24 2026

@author: ompha
"""

import streamlit as st
import random
import time

st.set_page_config(page_title="💘 Mr. O", layout="centered")

# -------------------------------------------------
# 🌌 MASSIVE ROMANTIC STYLE
# -------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #2b1055, #7597de);
    overflow: hidden;
}

/* Glass Card */
.card {
    background: rgba(255, 255, 255, 0.1);
    padding: 60px;
    border-radius: 30px;
    text-align: center;
    color: white;
    box-shadow: 0px 25px 80px rgba(0,0,0,0.5);
    backdrop-filter: blur(15px);
    animation: fadeIn 1.5s ease-in-out;
}

/* Glow Text */
h1, h2, h3 {
    text-shadow: 0px 0px 30px rgba(255,255,255,0.8);
}

/* Fade Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(40px);}
    to {opacity: 1; transform: translateY(0);}
}

/* 🌸 Falling Flowers */
.flower {
    position: fixed;
    top: -50px;
    font-size: 28px;
    animation: fall linear infinite;
    z-index: 0;
}

@keyframes fall {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(120vh); opacity: 0; }
}

/* ❤️ Floating Hearts */
.heart {
    position: fixed;
    bottom: -40px;
    font-size: 22px;
    animation: rise linear infinite;
    z-index: 0;
}

@keyframes rise {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(-120vh); opacity: 0; }
}

button[kind="primary"] {
    background-color: #ff4d6d !important;
    border-radius: 40px !important;
    height: 3.2em;
    width: 13em;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# 🎵 BACKGROUND MUSIC (RAW GITHUB LINK)
# -------------------------------------------------
st.audio(
    "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/iloveyou.mpeg",
    format="audio/mpeg"
)

# -------------------------------------------------
# 🌸 FLOWERS + ❤️ HEARTS
# -------------------------------------------------
flowers = ["🌸", "🌺", "🌷", "💐"]
for i in range(30):
    left = random.randint(0, 100)
    duration = random.randint(6, 12)
    delay = random.uniform(0, 5)
    flower = random.choice(flowers)

    st.markdown(
        f"""
        <div class="flower" 
             style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s;">
             {flower}
        </div>
        """,
        unsafe_allow_html=True,
    )

for i in range(20):
    left = random.randint(0, 100)
    duration = random.randint(5, 10)
    delay = random.uniform(0, 5)

    st.markdown(
        f"""
        <div class="heart"
             style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s;">
             ❤️
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------------------------------
# 💌 LOVE MESSAGES
# -------------------------------------------------
LOVE_MESSAGES = [
    "Loving you was never a question.",
    "It was patience.",
    "It was timing.",
    "You are my peace.",
    "My safe place.",
    "My heart.",
    "You feel like home.",
    "Every day with you feels intentional.",
    "This isn't a moment.",
    "It's a continuation.",
    "Forever starts with you.",
    "You are my answered prayer.",
    "You are my greatest blessing.",
    "With you, life feels complete.",
    "I choose you. Always."
]

# -------------------------------------------------
# SESSION CONTROL
# -------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = 1

# -------------------------------------------------
# 💖 SCREEN 1 — PROPOSAL
# -------------------------------------------------
if st.session_state.page == 1:

    st.markdown("""
    <div class="card">
        <h1>For You ❤️</h1>
        <h2>Will you be my Valentine?</h2>
        <br>
        <p>— Mr. O 💌</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("YES 💖", type="primary"):
        st.session_state.page = 2
        st.rerun()

# -------------------------------------------------
# ✨ SCREEN 2 — BUILD SUSPENSE
# -------------------------------------------------
elif st.session_state.page == 2:

    st.markdown("""
    <div class="card">
        <h2>One More Thing… ✨</h2>
        <p>A special love letter is about to unfold.</p>
        <p>Ready?</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open My Heart 💘", type="primary"):
        st.session_state.page = 3
        st.rerun()

# -------------------------------------------------
# 💌 SCREEN 3 — AUTO LOVE MODE
# -------------------------------------------------
elif st.session_state.page == 3:

    placeholder = st.empty()
    st.balloons()

    for i in range(500):

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

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

# -------------------------
# CLEAN BACKGROUND STYLE
# -------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #5f0a87, #a4508b);
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 50px;
    border-radius: 25px;
    text-align: center;
    color: white;
    box-shadow: 0px 15px 50px rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
    animation: fadeIn 1.2s ease-in-out;
}

h1, h2, h3 {
    text-shadow: 0px 0px 20px rgba(255,255,255,0.6);
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# AUDIO (GITHUB SAFE)
# -------------------------
st.markdown(
    """
    <audio autoplay loop>
        <source src="iloveyou.mp3" type="audio/mp3">
    </audio>
    """,
    unsafe_allow_html=True
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
    "Forever starts with you."
]

def get_random_message():
    return random.choice(LOVE_MESSAGES)

# -------------------------
# SESSION CONTROL
# -------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

# -------------------------
# SCREEN 1
# -------------------------
if st.session_state.step == 1:

    st.markdown("""
    <div class="card">
        <h1>For You ❤️</h1>
        <h2>Will you be my Valentine?</h2>
        <p>— Mr. O 💌</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("YES 💖"):
        st.session_state.step = 2
        st.rerun()

# -------------------------
# SCREEN 2
# -------------------------
elif st.session_state.step == 2:

    st.markdown("""
    <div class="card">
        <h2>One More Thing… ✨</h2>
        <p>A message from Mr. O is waiting.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("READ YOUR LETTER 💌"):
        st.session_state.step = 3
        st.rerun()

# -------------------------
# SCREEN 3
# -------------------------
elif st.session_state.step == 3:

    placeholder = st.empty()

    for i in range(100):
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

        time.sleep(3)

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 19:14:19 2026

@author: ompha
"""

import streamlit as st
from urllib.parse import quote
import time

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="MR. O's STEM ACADEMY",
    page_icon="📐",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
/* Main layout */
section.main { background-color: #f0f4f8; padding: 30px 50px; }

/* Titles */
h1 { font-family: 'Poppins', sans-serif; color: #FF6600; font-size: 3rem; text-align: center; }
h2 { font-family: 'Poppins', sans-serif; color: #FF6600; font-size: 2rem; text-align: center; margin-bottom:30px; }

/* Product image hover effect */
div.stImage img { border-radius:15px; box-shadow:0 5px 20px rgba(0,0,0,0.15); transition: transform 0.3s; }
div.stImage img:hover { transform: scale(1.05); }

/* Price style */
.price { font-size:18px; font-weight:bold; color:#0b3d91; margin-bottom:10px; }

/* Button style */
.button {
    background-color:#0b3d91;
    color:white;
    padding:12px 25px;
    border:none;
    border-radius:8px;
    font-weight:bold;
    font-size:16px;
    cursor:pointer;
    margin-top:5px;
}
.button:hover { background-color:#094182; }

/* Sidebar cart title */
.sidebar .sidebar-content h1, .sidebar .sidebar-content h2 { color:#FF6600; }
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("<h1> MR. O's STEM ACADEMY</h1>", unsafe_allow_html=True)
st.markdown("<h2>Get Equipped for Less – Shop Now!</h2>", unsafe_allow_html=True)
st.divider()

# ---------------- PRODUCTS ----------------
products = [
    ("A3 Paper", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/a3_paper.jpg", 1.99),
    ("Big Compass", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/big_compass.jpg", 99.99),
    ("Clutch Pencil", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/clutch_pencil.jpg", 9.99),
    ("Combo Set", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/combo.jpg", 94.99),
    ("Compass Leads", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/compass_leads.jpg", 9.99),
    ("Drawing Bag", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/drawing_bag.jpg", 219.99),
]

# ---------------- SESSION STATE ----------------
if 'cart' not in st.session_state:
    st.session_state.cart = []

my_number = "27632757157"  # WhatsApp number

# ---------------- SIDEBAR CART ----------------
st.sidebar.title("🛒 Your Cart")

def display_cart():
    total = sum([item[1] for item in st.session_state.cart])
    if st.session_state.cart:
        for i, (name, price) in enumerate(st.session_state.cart):
            col1, col2 = st.sidebar.columns([3,1])
            col1.write(f"{name} - R{price:.2f}")
            if col2.button("❌", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                return
        st.sidebar.markdown(f"**Total: R{total:.2f}**")

        cart_items = "\n".join([f"{name} - R{price:.2f}" for name, price in st.session_state.cart])
        wa_message = f"Hello! I would like to order the following items:\n{cart_items}\nTotal: R{total:.2f}"
        wa_url = f"https://wa.me/{my_number}?text={quote(wa_message)}"
        
        st.sidebar.markdown(f"""
        <a href="{wa_url}" target="_blank">
            <button class="button">
                📲 Order All via WhatsApp
            </button>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.sidebar.write("Your cart is empty")

display_cart()

# ---------------- PRODUCT GRID ----------------
st.subheader("Our Products📦🗳️")
cols = st.columns(3)

for i, (order, img_url, price) in enumerate(products):
    with cols[i % 3]:
        st.image(img_url, use_container_width=True)
        st.markdown(f"### {order}")
        st.markdown(f"<p class='price'>Price: R{price:.2f}</p>", unsafe_allow_html=True)

        # Add to Cart animation
        add_placeholder = st.empty()
        if st.button(f"Add to Cart", key=f"cart_{order}"):
            st.session_state.cart.append((order, price))
            
            # Flying emoji animation
            add_placeholder.markdown(f"<p style='font-size:24px;'>🛒 {order} added!</p>", unsafe_allow_html=True)
            time.sleep(0.8)
            add_placeholder.empty()
            
            display_cart()  # refresh sidebar cart

        # WhatsApp button for single product
        wa_message = f"Hello! I would like to order {order} for R{price:.2f}"
        wa_url = f"https://wa.me/{my_number}?text={quote(wa_message)}"
        st.markdown(f"""
        <a href="{wa_url}" target="_blank">
            <button class="button">
                📲 Buy via WhatsApp
            </button>
        </a>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.divider()
st.markdown("<h4 style='text-align:center; color:#FF6600;'>© 2026 MR. O's STEM ACADEMY | Free Delivery🚚📦</h4>", unsafe_allow_html=True)

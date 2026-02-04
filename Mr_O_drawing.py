# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 19:14:19 2026

@author: ompha
"""

import streamlit as st
from urllib.parse import quote

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="MR. O's STEM ACADEMY",
    page_icon="📐📦🗳️",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
section.main { background-color: #f0f4f8; padding: 30px 50px; }
h1 { font-family: 'Poppins', sans-serif; color: #FF6600; font-size: 3rem; text-align: center; }
h2 { font-family: 'Poppins', sans-serif; color: #FF6600; font-size: 2rem; text-align: center; margin-bottom:30px; }
div.stImage { border-radius:15px; box-shadow:0 5px 20px rgba(0,0,0,0.15); transition: transform 0.2s; }
div.stImage:hover { transform: scale(1.05); }
h3 { font-size:1.6rem; color:#0b3d91; margin-top:10px; }
.price { font-size:18px; font-weight:bold; }
.stButton button { background-color:#0b3d91; color:white; font-weight:bold; border-radius:8px; padding:10px 20px; margin-top:5px; }
.stButton button:hover { background-color:#06316a; }
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("<h1>📐 MR. O's STEM ACADEMY</h1>", unsafe_allow_html=True)
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
    ("Eraser", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/eraser.jpg", 8.99),
    ("Erasing Shield", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/erasing_shield.jpg", 26.99),
    ("French Curve", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/french_curve.jpg", 44.99),
    ("Leads", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/leads.jpg", 9.99),
    ("Sharpener", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/sharpener.jpg", 14.99),
    ("Small Compass", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/small_compass.jpg", 74.99),
    ("Stencil", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/stencil.jpg", 32.99),
    ("Drawing Board", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/drawing_board.jpg", 449.99),
]

# ---------------- SESSION STATE ----------------
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Your WhatsApp number
my_number = "27632757157"

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
                return  # Stop further processing so Streamlit reruns automatically

        st.sidebar.markdown(f"**Total: R{total:.2f}**")
        
        # WhatsApp link for all cart items
        cart_items = "\n".join([f"{name} - R{price:.2f}" for name, price in st.session_state.cart])
        wa_message = f"Hello! Mr. O, I would like to order the following items:\n{cart_items}\nTotal: R{total:.2f}"
        wa_url = f"https://wa.me/{my_number}?text={quote(wa_message)}"
        st.sidebar.markdown(f"[📲 Order All via WhatsApp](%s)" % wa_url, unsafe_allow_html=True)
    else:
        st.sidebar.write("Your cart is empty")

display_cart()

# ---------------- PRODUCT GRID ----------------
st.subheader("Our Products")
cols = st.columns(3)

for i, (order, img_url, price) in enumerate(products):
    with cols[i % 3]:
        st.image(img_url, use_container_width=True)
        st.markdown(f"### {order}")
        st.markdown(f"<p class='price'>Price: R{price:.2f}</p>", unsafe_allow_html=True)
        
        # Add to cart button
        if st.button(f"Buy {order}", key=order):
            st.session_state.cart.append((order, price))
            st.success(f"{order} added to cart 🛒")
            # No st.experimental_rerun() needed, Streamlit reruns automatically

# ---------------- FOOTER ----------------
st.divider()
st.markdown("<h4 style='text-align:center; color:#FF6600;'>© 2026 MR. O's STEM ACADEMY | Built with Streamlit</h4>", unsafe_allow_html=True)


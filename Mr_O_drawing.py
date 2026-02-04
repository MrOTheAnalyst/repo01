# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 19:14:19 2026

@author: ompha
"""

import streamlit as st
from urllib.parse import quote

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MR. O's STEM ACADEMY",
    page_icon="📐",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Body background */
section.main {
    background-color: #f0f4f8;
    padding: 30px 50px;
}

/* Hero Title */
h1 {
    font-family: 'Poppins', sans-serif;
    color: #0b3d91;
    font-size: 3rem;
    text-align: center;
    margin-bottom: 0px;
}
h2 {
    font-family: 'Poppins', sans-serif;
    color: #0b3d91;
    font-size: 2rem;
    text-align: center;
    margin-top: 5px;
    margin-bottom: 30px;
}

/* Product image hover */
div.stImage {
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    transition: transform 0.2s;
}
div.stImage:hover {
    transform: scale(1.05);
}

/* Product title */
h3 {
    font-size: 1.6rem;
    color: #0b3d91;
    margin-top: 10px;
}

/* Price */
.price {
    font-size: 18px;
    font-weight: bold;
}

/* Buy button */
.stButton button {
    background-color: #0b3d91;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
    margin-top: 5px;
}
.stButton button:hover {
    background-color: #06316a;
}
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

# ---------------- SIDEBAR CART ----------------
if 'cart' not in st.session_state:
    st.session_state.cart = []

st.sidebar.title("🛒 Your Cart")
total = sum([item[1] for item in st.session_state.cart])
if st.session_state.cart:
    for name, price in st.session_state.cart:
        st.sidebar.write(f"{name} - R{price:.2f}")
    st.sidebar.markdown(f"**Total: R{total:.2f}**")
else:
    st.sidebar.write("Your cart is empty")

# ---------------- PRODUCT GRID ----------------
st.subheader("Our Products")
cols = st.columns(3)

for i, (order, img_url, price) in enumerate(products):
    with cols[i % 3]:
        st.image(img_url, use_container_width=True)
        st.markdown(f"### {order}")
        st.markdown(f"<p class='price'>Price: R{price:.2f}</p>", unsafe_allow_html=True)

        # WhatsApp link
        message = f"Hello! I would like to order: {order} for R{price:.2f}"
        wa_url = f"https://wa.me/27761285492?text={quote(message)}"

        if st.button(f"Buy {order}", key=order):
            st.session_state.cart.append((order, price))
            st.success(f"{order} added to cart 🛒")
            st.markdown(f"[Order via WhatsApp](%s)" % wa_url, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.divider()
st.markdown("<h4 style='text-align:center; color:#0b3d91;'>© 2026 MR. O's STEM ACADEMY | Built with Streamlit</h4>", unsafe_allow_html=True)

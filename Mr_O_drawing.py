# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 19:14:19 2026

@author: ompha
"""

import streamlit as st

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
    background-color: #f9f9f9;
    padding: 20px 40px;
}

/* Product card styling */
div.stImage {
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    transition: transform 0.2s;
}
div.stImage:hover {
    transform: scale(1.05);
}

/* Headings */
h1, h2, h3 {
    font-family: 'Helvetica', sans-serif;
    color: #0b3d91;
}

/* Product titles */
h3 {
    font-size: 1.5rem;
    margin-top: 10px;
}

/* Buttons */
.stButton button {
    background-color: #0b3d91;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 8px 16px;
}
.stButton button:hover {
    background-color: #06316a;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("📐 MR. O's STEM ACADEMY", anchor=False)
st.subheader("Get equipped for less – Shop now!")
st.divider()

# ---------------- PRODUCTS ----------------
products = [
    ("A3 Paper", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/a3_paper.jpg", 1.99),
    ("Big Compass", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/big_compass.jpg", 99.99),
    ("Clutch Pencil", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/clutch_pencil.jpg", 9.99),
    ("Combo Set", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/combo.jpg", 94.99),
    ("Compass Leads", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/compass_leads.jpg", 9.99),
    ("Drawing Bag", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/drawing_bag.jpg", 219.99),
    ("Eraser", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/eraser.jpg", 8.99),
    ("Erasing Shield", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/erasing_shield.jpg", 26.99),
    ("French Curve", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/french_curve.jpg", 44.99),
    ("Leads", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/leads.jpg", 9.99),
    ("Sharpener", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/sharpener.jpg", 14.99),
    ("Small Compass", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/small_compass.jpg", 74.99),
    ("Stencil", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/stencil.jpg", 32.99),
    ("Drawing Board", "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/images/drawing_board.jpg", 449.99),
]

# ---------------- PRODUCT GRID ----------------
st.subheader("Our Products")
cols = st.columns(3)

for i, (order, img_url, price) in enumerate(products):
    with cols[i % 3]:
        try:
            st.image(img_url, use_container_width=True)
        except:
            st.error(f"Cannot load image: {order}")

        st.markdown(f"### {order}")
        st.markdown(f"<p style='font-size:18px; font-weight:bold;'>Price: R{price:.2f}</p>", unsafe_allow_html=True)

        if st.button(f"Buy {order}", key=order):
            st.success(f"{order} added to cart 🛒")

# ---------------- FOOTER ----------------
st.divider()
st.markdown("<h4 style='text-align:center; color:#0b3d91;'>© 2026 MR. O's STEM ACADEMY | Built with Streamlit</h4>", unsafe_allow_html=True)

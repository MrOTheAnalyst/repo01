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

# ---------------- HEADER ----------------
st.title("📐 MR. O's STEM ACADEMY")
st.subheader("Get equipped for less – Shop now!")
st.divider()

# ---------------- PRODUCTS ----------------
# Each image URL points to the "raw" GitHub file
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
cols = st.columns(3)

for i, (order, img_url, price) in enumerate(products):
    with cols[i % 3]:
        try:
            st.image(img_url, use_container_width=True)
        except Exception as e:
            st.error(f"Cannot load image: {order} | Error: {e}")

        st.markdown(f"### {order}")
        st.markdown(f"**Price: R{price:.2f}**")
        if st.button(f"Buy {order}", key=order):
            st.success(f"{order} added to cart 🛒")

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 MR. O's STEM ACADEMY | Built with Streamlit")

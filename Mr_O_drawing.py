# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 19:14:19 2026

@author: ompha
"""

import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MR. O's STEM ACADEMY",
    page_icon="📐",
    layout="wide"
)

# ---------------- PATH FIX ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")

# ---------------- HEADER ----------------
st.title("📐 MR. O's STEM ACADEMY")
st.subheader("Get equipped for less – Shop now!")
st.divider()

# ---------------- PRODUCTS ----------------
products = [
    ("A3 Paper", "a3_paper.jpg", 1.99),
    ("Big Compass", "big_compass.jpg", 99.99),
    ("Clutch Pencil", "clutch_pencil.jpg", 9.99),
    ("Combo Set", "combo.jpg", 94.99),
    ("Compass Leads", "compass_leads.jpg", 9.99),
    ("Drawing Bag", "drawing_bag.jpg", 219.99),
    ("Eraser", "eraser.jpg", 8.99),
    ("Erasing Shield", "erasing_shield.jpg", 26.99),
    ("French Curve", "french_curve.jpg", 44.99),
    ("Leads", "leads.jpg", 9.99),
    ("Sharpener", "sharpener.jpg", 14.99),
    ("Small Compass", "small_compass.jpg", 74.99),
    ("Stencil", "stencil.jpg", 32.99),
    ("Drawing Board", "drawing_board.jpg", 449.99),
]

# ---------------- PRODUCT GRID ----------------
cols = st.columns(3)

for i, (order, img_file, price) in enumerate(products):
    with cols[i % 3]:
        img_path = os.path.join(IMAGE_DIR, img_file)

        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.error(f"Missing image: {img_file}")

        st.markdown(f"### {order}")
        st.markdown(f"**Price: R{price:.2f}**")

        if st.button(f"Buy {order}", key=order):
            st.success(f"{order} added to cart 🛒")

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 MR. O's STEM ACADEMY | Built with Streamlit")

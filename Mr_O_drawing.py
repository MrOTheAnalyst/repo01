# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 19:14:19 2026

@author: ompha
"""

import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="MR. O's STEM ACADEMY",
    page_icon="📐",
    layout="wide"
)

st.title("📐 MR. O's STEM ACADEMY")
st.subheader("Get equipped for less – Shop now!")
st.divider()

products = [
    ("A3 Paper", "images/a3_paper.jpg", 1.50),
    ("Big Compass", "images/big_compass.jpg", 99.99),
    ("Clutch Pencil", "images/clutch_pencil.jpg", 9.99),
    ("Combo Set", "images/combo.jpg", 94.99),
    ("Compass Leads", "images/compass_leads.jpg", 9.99),
    ("Drawing Bag", "images/drawing_bag.jpg", 219.99),
    ("Eraser", "images/eraser.jpg", 8.99),
    ("Erasing Shield", "images/erasing_shield.jpg", 26.99),
    ("French Curve", "images/french_curve.jpg", 44.99),
    ("Leads", "images/leads.jpg", 9.99),
    ("Sharpener", "images/sharpener.jpg", 14.99),
    ("Small Compass", "images/small_compass.jpg", 74.99),
    ("Stencil", "images/stencil.jpg", 32.99),
]

cols = st.columns(3)

for i, (name, img_path, price) in enumerate(products):
    with cols[i % 3]:
        if os.path.exists(img_path):
            image = Image.open(img_path)
            st.image(image, use_container_width=True)
        else:
            st.warning("Image not found")

        st.markdown(f"### {name}")
        st.markdown(f"**Price: R{price:.2f}**")
        st.button(f"Buy {name}")

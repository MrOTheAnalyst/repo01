# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 19:14:19 2026

@author: ompha
"""

import streamlit as st

# Page config
st.set_page_config(
    page_title="MR. O's STEM ACADEMY",
    page_icon="📐",
    layout="wide"
)

# Title & subheading
st.title("📐 MR. O's STEM ACADEMY")
st.subheader("Get equipped for less – Shop now!")

st.markdown("---")

# Product list
products = [
    ("A3 Paper", "images/A3 paper.jpg", 1.50),
    ("Big Compass", "images/Big compass.jpg", 99.99),
    ("Clutch Pencil", "images/clutch pencil.jpg", 9.99),
    ("Combo Set", "images/combo.webp", 94.99),
    ("Compass Leads", "images/compass leads.avif", 9.99),
    ("Drawing Bag", "images/drawing bag.webp", 219.99),
    ("Eraser", "images/eraser.avif", 8.99),
    ("Erasing Shield", "images/erasing shield.jpg", 26.99),
    ("French Curve", "images/french.jpg", 44.99),
    ("Leads", "images/leads.avif", 9.99),
    ("Sharpener", "images/sharpener.avif", 14.99),
    ("Small Compass", "images/small compass.avif", 74.99),
    ("Stencil", "images/stencil.webp", 32.99),
]

# Display products in columns
cols = st.columns(3)

for index, product in enumerate(products):
    name, image, price = product
    with cols[index % 3]:
        st.image(image, use_container_width=True)
        st.markdown(f"### {name}")
        st.markdown(f"**Price: R{price:.2f}**")
        st.button(f"Buy {name}")

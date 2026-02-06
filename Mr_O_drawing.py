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

# ---------------- CSS ----------------
st.markdown("""
<style>
section.main { background-color: #f0f4f8; padding: 30px 50px; }
h1 { color: #FF6600; font-size: 3rem; text-align: center; }
h2 { color: #FF6600; text-align: center; margin-bottom:30px; }
.price { font-size:18px; font-weight:bold; }
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "cart" not in st.session_state:
    st.session_state.cart = {}

# ---------------- PRODUCTS (RANDS ONLY) ----------------
products = [
    {"id": "a3", "name": "A3 Paper", "price": 5},
    {"id": "big_compass", "name": "Big Compass", "price": 100},
    {"id": "clutch", "name": "Clutch Pencil", "price": 10},
    {"id": "combo", "name": "Combo Set", "price": 95},
    {"id": "leads", "name": "Leads", "price": 10},
    {"id": "bag", "name": "Drawing Bag", "price": 220},
    {"id": "board", "name": "Drawing Board", "price": 450},
]

# ---------------- WHATSAPP ----------------
my_number = "27632757157"

def format_price(rands):
    return f"R{rands}"

# ---------------- HERO ----------------
st.markdown("<h1>MR. O's STEM ACADEMY</h1>", unsafe_allow_html=True)
st.markdown("<h2>Get Equipped for Less – Shop Now!</h2>", unsafe_allow_html=True)
st.divider()

# ---------------- SIDEBAR CART ----------------
st.sidebar.title("🛒 Your Cart")

if not st.session_state.cart:
    st.sidebar.write("Your cart is empty")
else:
    total = 0
    wa_lines = []

    for pid, item in st.session_state.cart.items():
        line_total = item["price"] * item["qty"]
        total += line_total

        col1, col2 = st.sidebar.columns([3,1])
        col1.write(
            f"{item['name']} x{item['qty']} — {format_price(line_total)}"
        )

        if col2.button("❌", key=f"remove_{pid}"):
            del st.session_state.cart[pid]
            st.rerun()

        wa_lines.append(
            f"{item['name']} x{item['qty']} - {format_price(line_total)}"
        )

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### Total: {format_price(total)}")

    wa_message = (
        "Hello Mr. O! I would like to order:\n" +
        "\n".join(wa_lines) +
        f"\n\nTotal: {format_price(total)}"
    )

    wa_url = f"https://wa.me/{my_number}?text={quote(wa_message)}"

    st.sidebar.markdown(f"""
    <a href="{wa_url}" target="_blank">
        <button style="
            background-color:#0b3d91;
            color:white;
            padding:12px 25px;
            border:none;
            border-radius:8px;
            font-weight:bold;
            font-size:16px;
            cursor:pointer;">
            📲 Order via WhatsApp
        </button>
    </a>
    """, unsafe_allow_html=True)

# ---------------- PRODUCT GRID ----------------
st.subheader("Our Products 📦")

cols = st.columns(3)

for i, p in enumerate(products):
    with cols[i % 3]:
        st.markdown(f"### {p['name']}")
        st.markdown(f"<p class='price'>Price: {format_price(p['price'])}</p>", unsafe_allow_html=True)

        if st.button("Add to Cart", key=f"add_{p['id']}"):
            if p["id"] in st.session_state.cart:
                st.session_state.cart[p["id"]]["qty"] += 1
            else:
                st.session_state.cart[p["id"]] = {
                    "name": p["name"],
                    "price": p["price"],
                    "qty": 1
                }
            st.rerun()

# ---------------- FOOTER ----------------
st.divider()
st.markdown(
    "<h4 style='text-align:center; color:#FF6600;'>© 2026 MR. O's STEM ACADEMY | Free Delivery 🚚</h4>",
    unsafe_allow_html=True
)

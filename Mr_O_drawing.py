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
.qty-btn button { width: 100%; }
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "cart" not in st.session_state:
    st.session_state.cart = {}

if "customer_name" not in st.session_state:
    st.session_state.customer_name = ""

# ---------------- PRODUCTS (RANDS ONLY) ----------------
products = [
    {"id": "a3", "name": "A3 Paper", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/a3_paper.jpg", "price": 2},
    {"id": "big_compass", "name": "Big Compass", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/big_compass.jpg", "price": 100},
    {"id": "clutch", "name": "Clutch Pencil", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/clutch_pencil.jpg", "price": 10},
    {"id": "combo", "name": "Combo Set", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/combo.jpg", "price": 95},
    {"id": "leads", "name": "Compass Leads", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/compass_leads.jpg", "price": 10},
    {"id": "bag", "name": "Drawing Bag", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/drawing_bag.jpg", "price": 220},
    {"id": "eraser", "name": "Eraser", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/eraser.jpg", "price": 9},
    {"id": "shield", "name": "Erasing Shield", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/erasing_shield.jpg", "price": 27},
    {"id": "curve", "name": "French Curve", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/french_curve.jpg", "price": 45},
    {"id": "sharpener", "name": "Sharpener", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/sharpener.jpg", "price": 15},
    {"id": "small_compass", "name": "Small Compass", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/small_compass.jpg", "price": 75},
    {"id": "stencil", "name": "Stencil", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/stencil.jpg", "price": 33},
    {"id": "board", "name": "Drawing Board", "img": "https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/drawing_board.jpg", "price": 450},
]

# ---------------- HELPERS ----------------
def money(r):
    return f"R{r}"

my_number = "27632757157"

# ---------------- HERO ----------------
st.markdown("<h1>MR. O's STEM ACADEMY</h1>", unsafe_allow_html=True)
st.markdown("<h2>Get Equipped for Less – Shop Now!</h2>", unsafe_allow_html=True)
st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🧾 Customer Details")
st.session_state.customer_name = st.sidebar.text_input(
    "Customer name",
    value=st.session_state.customer_name,
    placeholder="Enter your name"
)

st.sidebar.divider()
st.sidebar.title("🛒 Your Cart")

if not st.session_state.cart:
    st.sidebar.write("Your cart is empty")
else:
    total = 0
    wa_lines = []

    for pid, item in st.session_state.cart.items():
        line_total = item["price"] * item["qty"]
        total += line_total

        col1, col2, col3 = st.sidebar.columns([3,1,1])

        col1.write(f"{item['name']} ({money(item['price'])})")
        col2.write(f"Qty: {item['qty']}")

        with col3:
            if st.button("➕", key=f"plus_{pid}"):
                item["qty"] += 1
                st.rerun()
            if st.button("➖", key=f"minus_{pid}"):
                item["qty"] -= 1
                if item["qty"] <= 0:
                    del st.session_state.cart[pid]
                st.rerun()

        wa_lines.append(
            f"{item['name']} x{item['qty']} - {money(line_total)}"
        )

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### Total: {money(total)}")

    customer = st.session_state.customer_name or "Customer"

    wa_message = (
        f"Hello Mr. O!\n\n"
        f"Customer: {customer}\n\n"
        "Order:\n" +
        "\n".join(wa_lines) +
        f"\n\nTotal: {money(total)}"
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
        st.image(p["img"], use_container_width=True)
        st.markdown(f"### {p['name']}")
        st.markdown(f"<p class='price'>Price: {money(p['price'])}</p>", unsafe_allow_html=True)

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
    "<h4 style='text-align:center; color:#FF6600;'>MR. O's STEM ACADEMY | Free Delivery 🚚</h4>",
    unsafe_allow_html=True
)


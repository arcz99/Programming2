import sqlite3
import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(page_title="Sales Dashboard", layout="centered")
st.title("Streamlit Sales Dashboard")

DB_FILE = "sales.db"

# 1. Load data
@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df

# 2. Add new record
with st.expander("➕ Add New Sale"):
    product = st.text_input("Product")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    price = st.number_input("Price", min_value=0.0, step=0.01)
    date = st.date_input("Date")
    if st.button("Add Sale"):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
                       (product, quantity, price, date.strftime("%Y-%m-%d")))
        conn.commit()
        conn.close()
        st.success("Sale added successfully!")
        st.balloons()

# 3. Load and filter data
data = load_data()

st.subheader("Filtered Sales Data")

if data.empty:
    st.warning("No sales data available.")
else:
    products = data['product'].unique()
    selected_product = st.selectbox("Filter by product", options=["All"] + sorted(products.tolist()))

    if selected_product != "All":
        filtered_data = data[data['product'] == selected_product]
    else:
        filtered_data = data

    st.dataframe(filtered_data)

    # Convert date column to datetime if not already
    filtered_data['date'] = pd.to_datetime(filtered_data['date'])

    # 4a. Daily sales (quantity * price)
    st.subheader("📅 Daily Sales (Revenue)")
    daily_sales = filtered_data.copy()
    daily_sales["revenue"] = daily_sales["quantity"] * daily_sales["price"]
    daily_summary = daily_sales.groupby("date")["revenue"].sum().reset_index()

    chart1 = alt.Chart(daily_summary).mark_line(point=True).encode(
        x="date:T",
        y="revenue:Q"
    ).properties(title="Revenue Over Time")
    st.altair_chart(chart1, use_container_width=True)

    # 4b. Sum of sold products by type
    st.subheader("Total Quantity by Product")
    product_summary = filtered_data.groupby("product")["quantity"].sum().reset_index()

    chart2 = alt.Chart(product_summary).mark_bar().encode(
        x="product:N",
        y="quantity:Q",
        color="product:N"
    ).properties(title="Total Quantity per Product")
    st.altair_chart(chart2, use_container_width=True)
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("E-Commerce Sales Dashboard")

df = pd.read_csv("data/ecommerce_sales.csv")

df["Sales"] = df["Price"] * df["Quantity"]

# KPIs

total_sales = df["Sales"].sum()
total_orders = df["OrderID"].nunique()

st.metric("Total Sales", f"₹{total_sales}")
st.metric("Total Orders", total_orders)

# Category Sales

category_sales = df.groupby("Category")["Sales"].sum().reset_index()

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Category Wise Sales"
)

st.plotly_chart(fig1)

# Region Sales

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig2 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Region Wise Sales"
)

st.plotly_chart(fig2)

# Product Sales

product_sales = df.groupby("Product")["Sales"].sum().reset_index()

fig3 = px.bar(
    product_sales,
    x="Product",
    y="Sales",
    title="Product Performance"
)

st.plotly_chart(fig3)
import streamlit as st
import pandas as pd
import plotly.express as px

# Dataset Load
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(df["Order Date"])

st.title("AI-Driven Business Intelligence Dashboard")

# ==========================
# KPI Tracking
# ==========================

st.header("KPI Tracking")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", round(df["Sales"].sum(),2))
col2.metric("Total Profit", round(df["Profit"].sum(),2))
col3.metric("Total Orders", df["Order ID"].nunique())

# ==========================
# Sales by Region
# ==========================

st.header("Regional Sales")

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig1 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region"
)

st.plotly_chart(fig1)

# ==========================
# Forecast Chart
# ==========================

st.header("Revenue Forecast")

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df = df.dropna(subset=["Order Date"])

monthly_sales = df.set_index("Order Date").resample("M")["Sales"].sum().reset_index()

fig2 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig2)

# ==========================
# Customer Segmentation View
# ==========================

st.header("Customer Segmentation")

customer = df.groupby("Customer ID")[["Sales","Profit"]].sum().reset_index()

fig3 = px.scatter(
    customer,
    x="Sales",
    y="Profit",
    title="Customer Segments"
)

st.plotly_chart(fig3)

# ==========================
# Risk Heatmap
# ==========================

st.header("Risk Heatmap")

pivot = df.pivot_table(
    values="Profit",
    index="Category",
    columns="Region",
    aggfunc="sum"
)

fig4 = px.imshow(
    pivot,
    text_auto=True,
    title="Profit Heatmap"
)

st.plotly_chart(fig4)
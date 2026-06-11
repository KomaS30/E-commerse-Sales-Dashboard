
import pandas as pd

df = pd.read_csv("data/ecommerce_sales.csv")

# Total Sales

df["Sales"] = df["Price"] * df["Quantity"]

print("Total Sales:", df["Sales"].sum())

print("\nCategory Wise Sales")

print(df.groupby("Category")["Sales"].sum())

print("\nRegion Wise Sales")

print(df.groupby("Region")["Sales"].sum())
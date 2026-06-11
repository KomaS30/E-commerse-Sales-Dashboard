import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/ecommerce_sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

df["Sales"] = df["Price"] * df["Quantity"]

monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()

X = monthly_sales[["Month"]]
y = monthly_sales["Sales"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

future_month = [[12]]

prediction = model.predict(future_month)

print("Predicted Sales:", prediction[0])
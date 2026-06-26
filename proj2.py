import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("Dataset for Data Analytics (2).xlsx")

print("\n--------- DATASET OVERVIEW ---------")
print("Shape of Dataset:", df.shape)

print("\nFirst 5 Records")
print(df.head())


# DATA CLEANING

print("\n--------- MISSING VALUES ---------")
print(df.isnull().sum())

# Fill missing coupon values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDuplicates Removed Successfully")

# Standardize text columns
text_columns = [
    "Product",
    "PaymentMethod",
    "OrderStatus",
    "CouponCode",
    "ReferralSource"
]

for col in text_columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.title()
    )

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Round numeric columns
df["UnitPrice"] = df["UnitPrice"].round(2)
df["TotalPrice"] = df["TotalPrice"].round(2)

print("\n------- DATA TYPES ---------")
print(df.dtypes)

# DESCRIPTIVE STATISTICS

print("\n--------- DESCRIPTIVE STATISTICS ---------")
print(df.describe())

print("\nMean")
print(df.select_dtypes(include=np.number).mean())

print("\nMedian")
print(df.select_dtypes(include=np.number).median())

print("\nMode")
print(df.select_dtypes(include=np.number).mode())

# PRODUCT REVENUE ANALYSIS

top_products = (
    df.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--------- TOP PRODUCTS ---------")
print(top_products)

plt.figure(figsize=(12,6))

top_products.plot(kind="bar")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Products")
plt.ylabel("Revenue")

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# Analysis PAYMENT METHOD 

payment = df["PaymentMethod"].value_counts()

print("\n--------- PAYMENT METHODS ---------")
print(payment)

plt.figure(figsize=(10,6))

payment.plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Count")

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()


#Analysis ORDER STATUS 


status = df["OrderStatus"].value_counts()

print("\n--------- ORDER STATUS ---------")
print(status)

plt.figure(figsize=(8,5))

status.plot(kind="bar")

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# MONTHLY SALES TREND

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["TotalPrice"]
    .sum()
)

print("\n--------- MONTHLY SALES ---------")
print(monthly_sales)

plt.figure(figsize=(12,6))

monthly_sales.plot(marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# OUTLIER DETECTION


Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - (1.5 * IQR)
upper = Q3 + (1.5 * IQR)

outliers = df[
    (df["TotalPrice"] < lower) |
    (df["TotalPrice"] > upper)
]

print("\n--------- OUTLIERS ---------")
print("Number of Outliers:", len(outliers))

plt.figure(figsize=(10,5))

sns.boxplot(x=df["TotalPrice"])

plt.title("Outlier Detection Using Boxplot")

plt.tight_layout()
plt.show()


# DISTRIBUTION OF TOTAL PRICE


plt.figure(figsize=(10,5))

plt.hist(df["TotalPrice"], bins=20)

plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# CORRELATION ANALYSIS


numeric_data = df.select_dtypes(include=np.number)

correlation = numeric_data.corr()

print("\n--------- CORRELATION MATRIX ---------")
print(correlation)

plt.figure(figsize=(10,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()


# BUSINESS INSIGHTS


print("\n--------- BUSINESS INSIGHTS ---------")

print("Total Orders:",
      len(df))

print("Total Revenue:",
      round(df["TotalPrice"].sum(),2))

print("Average Order Value:",
      round(df["TotalPrice"].mean(),2))

print("Most Sold Product:",
      df["Product"].mode()[0])

print("Most Used Payment Method:",
      df["PaymentMethod"].mode()[0])

print("Most Common Order Status:",
      df["OrderStatus"].mode()[0])

print("\nEDA Project Completed Successfully.")


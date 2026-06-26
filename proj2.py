
# # ==========================================================
# # PROJECT 2: EXPLORATORY DATA ANALYSIS (EDA)
# # Author: Internship Project
# # Tools: Python, Pandas, NumPy, Matplotlib, Seaborn
# # ==========================================================

# # Import libraries
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # ==========================================================
# # 1. LOAD DATASET
# # ==========================================================

# df = pd.read_excel("Dataset for Data Analytics (2).xlsx")

# print("\n========== DATASET OVERVIEW ==========")
# print("Rows and Columns:", df.shape)
# print("\nFirst 5 Records:")
# print(df.head())

# # ==========================================================
# # 2. DATA CLEANING
# # ==========================================================

# print("\n========== MISSING VALUES ==========")
# print(df.isnull().sum())

# # Replace missing coupon codes
# df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# # Remove duplicate rows
# df = df.drop_duplicates()

# # Check data types
# print("\n========== DATA TYPES ==========")
# print(df.dtypes)

# # Standardize text columns
# text_columns = [
#     "Product",
#     "PaymentMethod",
#     "OrderStatus",
#     "CouponCode",
#     "ReferralSource"
# ]

# for col in text_columns:
#     df[col] = df[col].astype(str).str.strip().str.title()

# # Round decimal values
# df["UnitPrice"] = df["UnitPrice"].round(2)
# df["TotalPrice"] = df["TotalPrice"].round(2)

# print("\nDataset cleaned successfully.")

# # ==========================================================
# # 3. DESCRIPTIVE STATISTICS
# # ==========================================================

# print("\n========== DESCRIPTIVE STATISTICS ==========")
# print(df.describe())

# print("\nMean Values")
# print(df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].mean())

# print("\nMedian Values")
# print(df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].median())

# print("\nMode Values")
# print(df[["Quantity","ItemsInCart"]].mode())

# # ==========================================================
# # 4. PRODUCT ANALYSIS
# # ==========================================================

# print("\n========== TOP PRODUCTS ==========")
# top_products = df["Product"].value_counts()
# print(top_products)

# # ==========================================================
# # 5. PAYMENT METHOD ANALYSIS
# # ==========================================================

# print("\n========== PAYMENT METHODS ==========")
# payment = df["PaymentMethod"].value_counts()
# print(payment)

# # ==========================================================
# # 6. ORDER STATUS ANALYSIS
# # ==========================================================

# print("\n========== ORDER STATUS ==========")
# status = df["OrderStatus"].value_counts()
# print(status)

# # ==========================================================
# # 7. MONTHLY SALES TREND
# # ==========================================================

# df["Date"] = pd.to_datetime(df["Date"])
# df["Month"] = df["Date"].dt.to_period("M")

# monthly_sales = df.groupby("Month")["TotalPrice"].sum()

# print("\n========== MONTHLY SALES ==========")
# print(monthly_sales)

# # ==========================================================
# # 8. OUTLIER DETECTION
# # ==========================================================

# Q1 = df["TotalPrice"].quantile(0.25)
# Q3 = df["TotalPrice"].quantile(0.75)

# IQR = Q3 - Q1

# lower_limit = Q1 - 1.5 * IQR
# upper_limit = Q3 + 1.5 * IQR

# outliers = df[
#     (df["TotalPrice"] < lower_limit) |
#     (df["TotalPrice"] > upper_limit)
# ]

# print("\n========== OUTLIERS ==========")
# print("Number of Outliers:", len(outliers))

# # ==========================================================
# # 9. CORRELATION ANALYSIS
# # ==========================================================

# numeric_data = df.select_dtypes(include=np.number)

# print("\n========== CORRELATION ==========")
# print(numeric_data.corr())

# # ==========================================================
# # 10. DATA VISUALIZATION
# # ==========================================================

# # Sales Trend
# plt.figure(figsize=(10,5))
# monthly_sales.plot()
# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.xticks(rotation=45)
# plt.show()

# # Product Distribution
# plt.figure(figsize=(10,5))
# df["Product"].value_counts().plot(kind="bar")
# plt.title("Product Distribution")
# plt.xticks(rotation=45)
# plt.show()

# # Payment Method
# plt.figure(figsize=(7,7))
# df["PaymentMethod"].value_counts().plot(
#     kind="pie",
#     autopct="%1.1f%%"
# )
# plt.ylabel("")
# plt.title("Payment Method Distribution")
# plt.show()

# # Total Price Distribution
# plt.figure(figsize=(8,5))
# plt.hist(df["TotalPrice"], bins=20)
# plt.title("Total Price Distribution")
# plt.xlabel("Total Price")
# plt.ylabel("Frequency")
# plt.show()

# # Boxplot for Outliers
# plt.figure(figsize=(8,5))
# sns.boxplot(x=df["TotalPrice"])
# plt.title("Outlier Detection")
# plt.show()

# # Correlation Heatmap
# plt.figure(figsize=(8,5))
# sns.heatmap(
#     numeric_data.corr(),
#     annot=True
# )
# plt.title("Correlation Heatmap")
# plt.show()

# # ==========================================================
# # 11. BUSINESS INSIGHTS
# # ==========================================================

# print("\n========== KEY OBSERVATIONS ==========")

# print("1. Total Orders:", len(df))
# print("2. Total Revenue:", df["TotalPrice"].sum())
# print("3. Average Order Value:", round(df["TotalPrice"].mean(),2))
# print("4. Most Sold Product:",
#       df["Product"].mode()[0])
# print("5. Most Used Payment Method:",
#       df["PaymentMethod"].mode()[0])
# print("6. Most Common Order Status:",
#       df["OrderStatus"].mode()[0])

# print("\nEDA Project Completed Successfully.")




# ==========================================================
# PROJECT 2: EXPLORATORY DATA ANALYSIS (EDA)
# Internship Project
# Tools: Python, Pandas, NumPy, Matplotlib, Seaborn
# ==========================================================

# ------------------------
# Import Libraries
# ------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------
# Load Dataset
# ------------------------
df = pd.read_excel("Dataset for Data Analytics (2).xlsx")

print("\n========== DATASET OVERVIEW ==========")
print("Shape of Dataset:", df.shape)

print("\nFirst 5 Records")
print(df.head())

# ==========================================================
# DATA CLEANING
# ==========================================================

print("\n========== MISSING VALUES ==========")
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

print("\n========== DATA TYPES ==========")
print(df.dtypes)

# ==========================================================
# DESCRIPTIVE STATISTICS
# ==========================================================

print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())

print("\nMean")
print(df.select_dtypes(include=np.number).mean())

print("\nMedian")
print(df.select_dtypes(include=np.number).median())

print("\nMode")
print(df.select_dtypes(include=np.number).mode())

# ==========================================================
# PRODUCT REVENUE ANALYSIS
# ==========================================================

top_products = (
    df.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP PRODUCTS ==========")
print(top_products)

plt.figure(figsize=(12,6))

top_products.plot(kind="bar")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Products")
plt.ylabel("Revenue")

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# ==========================================================
# PAYMENT METHOD ANALYSIS
# ==========================================================

payment = df["PaymentMethod"].value_counts()

print("\n========== PAYMENT METHODS ==========")
print(payment)

plt.figure(figsize=(10,6))

payment.plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Count")

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# ==========================================================
# ORDER STATUS ANALYSIS
# ==========================================================

status = df["OrderStatus"].value_counts()

print("\n========== ORDER STATUS ==========")
print(status)

plt.figure(figsize=(8,5))

status.plot(kind="bar")

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# ==========================================================
# MONTHLY SALES TREND
# ==========================================================

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["TotalPrice"]
    .sum()
)

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

plt.figure(figsize=(12,6))

monthly_sales.plot(marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ==========================================================
# OUTLIER DETECTION
# ==========================================================

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - (1.5 * IQR)
upper = Q3 + (1.5 * IQR)

outliers = df[
    (df["TotalPrice"] < lower) |
    (df["TotalPrice"] > upper)
]

print("\n========== OUTLIERS ==========")
print("Number of Outliers:", len(outliers))

plt.figure(figsize=(10,5))

sns.boxplot(x=df["TotalPrice"])

plt.title("Outlier Detection Using Boxplot")

plt.tight_layout()
plt.show()

# ==========================================================
# DISTRIBUTION OF TOTAL PRICE
# ==========================================================

plt.figure(figsize=(10,5))

plt.hist(df["TotalPrice"], bins=20)

plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# ==========================================================
# CORRELATION ANALYSIS
# ==========================================================

numeric_data = df.select_dtypes(include=np.number)

correlation = numeric_data.corr()

print("\n========== CORRELATION MATRIX ==========")
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

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

print("\n========== BUSINESS INSIGHTS ==========")

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


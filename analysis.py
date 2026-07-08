import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

print("\nData Types:")
print(df.dtypes)

df["ADDRESSLINE2"] = df["ADDRESSLINE2"].fillna("Unknown")
df["STATE"] = df["STATE"].fillna("Unknown")
df["POSTALCODE"] = df["POSTALCODE"].fillna("Unknown")
df["TERRITORY"] = df["TERRITORY"].fillna("Unknown")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

print("\nOrders by Country:")
print(df["COUNTRY"].value_counts())

print("\nOrder Status:")
print(df["STATUS"].value_counts())

df.to_csv("cleaned_sales_data.csv", index=False)

top_countries = df["COUNTRY"].value_counts().head(5)

top_countries.plot(kind="bar")

plt.title("Top 5 Countries by Order Count")
plt.xlabel("Country")
plt.ylabel("Number of Orders")

plt.show()
df.to_csv("cleaned_sales_data.csv", index=False)


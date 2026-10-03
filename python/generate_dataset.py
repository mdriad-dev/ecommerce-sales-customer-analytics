import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

project_folder = Path(__file__).parent.parent
raw_folder = project_folder / "data" / "raw"

raw_folder.mkdir(parents=True, exist_ok=True)

customers = [
    ("C001", "Rahim Ahmed", "Male", 24, "Dhaka", "Central"),
    ("C002", "Nusrat Jahan", "Female", 29, "Chattogram", "East"),
    ("C003", "Tanvir Hasan", "Male", 34, "Dhaka", "Central"),
    ("C004", "Sadia Islam", "Female", 26, "Sylhet", "East"),
    ("C005", "Fahim Rahman", "Male", 31, "Rajshahi", "North"),
    ("C006", "Mim Akter", "Female", 23, "Khulna", "South"),
    ("C007", "Arif Hossain", "Male", 38, "Dhaka", "Central"),
    ("C008", "Jannatul Ferdous", "Female", 27, "Barishal", "South"),
    ("C009", "Sakib Khan", "Male", 22, "Cumilla", "East"),
    ("C010", "Tania Sultana", "Female", 35, "Rangpur", "North"),
    ("C011", "Mehedi Hasan", "Male", 28, "Chattogram", "East"),
    ("C012", "Sumaiya Noor", "Female", 30, "Dhaka", "Central"),
    ("C013", "Imran Kabir", "Male", 41, "Rajshahi", "North"),
    ("C014", "Rima Yasmin", "Female", 25, "Khulna", "South"),
    ("C015", "Nayeem Islam", "Male", 33, "Sylhet", "East"),
]

products = [
    ("P001", "Laptop", "Electronics", 85000),
    ("P002", "Headphones", "Electronics", 3500),
    ("P003", "Smartphone", "Electronics", 45000),
    ("P004", "Office Chair", "Furniture", 12000),
    ("P005", "Desk", "Furniture", 18000),
    ("P006", "Keyboard", "Electronics", 2500),
    ("P007", "Monitor", "Electronics", 22000),
    ("P008", "Backpack", "Accessories", 2800),
    ("P009", "Mouse", "Electronics", 1500),
    ("P010", "Bookshelf", "Furniture", 9500),
    ("P011", "Webcam", "Electronics", 5500),
    ("P012", "USB Hub", "Accessories", 1800),
]

payment_methods = [
    "Cash",
    "Card",
    "bKash",
    "Nagad",
    "Bank Transfer"
]

order_statuses = [
    "Completed",
    "Completed",
    "Completed",
    "Pending",
    "Cancelled"
]

columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Name",
    "Gender",
    "Age",
    "City",
    "Region",
    "Product_ID",
    "Product_Name",
    "Category",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Payment_Method",
    "Order_Status"
]

rows = []

start_date = datetime(2026, 1, 1)

for i in range(1, 1201):

    customer = random.choice(customers)
    product = random.choice(products)

    order_date = start_date + timedelta(
        days=random.randint(0, 273)
    )

    quantity = random.choice([1, 1, 1, 2, 2, 3, 4, 5])
    discount = random.choice([0, 0, 0, 5, 10, 15])

    rows.append([
        f"ORD{i:04d}",
        order_date.strftime("%Y-%m-%d"),
        customer[0],
        customer[1],
        customer[2],
        customer[3],
        customer[4],
        customer[5],
        product[0],
        product[1],
        product[2],
        quantity,
        product[3],
        discount,
        random.choice(payment_methods),
        random.choice(order_statuses)
    ])

df = pd.DataFrame(rows, columns=columns)

# Data quality issues for cleaning practice

df.loc[96, "City"] = df.loc[96, "City"].lower()
df.loc[112, "Customer_Name"] = " " + df.loc[112, "Customer_Name"] + " "
df.loc[126, "Gender"] = df.loc[126, "Gender"].upper()
df.loc[148, "Order_Date"] = "15/06/2026"
df.loc[172, "Quantity"] = 0
df.loc[180, "City"] = None
df.loc[190, "Customer_Name"] = None
df.loc[210, "Discount"] = None

# Duplicate rows

duplicates = df.iloc[[25, 149, 399]].copy()

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

output_file = raw_folder / "ecommerce_sales_raw.csv"

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8"
)

print("Dataset created successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("File:", output_file)
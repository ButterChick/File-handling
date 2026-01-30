import pyodbc
import random
from datetime import date, timedelta

# ---------------- CONNECTION ----------------
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\SQLEXPRESS;"
    "DATABASE=PracticeDB;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# ---------------- HELPERS ----------------
def random_date():
    start = date(2024, 1, 1)
    end = date(2025, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

regions = ["EMEA", "NA", "APAC"]
statuses = ["processing", "shipped", "cancelled"]
categories = ["Widgets", "Gadgets"]
countries = ["US", "DE", "IN"]

# ---------------- SUPPLIERS ----------------
for i in range(510, 520):
    cursor.execute(
        "INSERT INTO suppliers VALUES (?, ?, ?)",
        i, f"Supplier {i}", random.choice(countries)
    )

# ---------------- PRODUCTS ----------------
for i in range(210, 220):
    cursor.execute(
        "INSERT INTO products VALUES (?, ?, ?, ?)",
        i,
        f"Product {i}",
        random.randint(510, 519),
        random.choice(categories)
    )

# ---------------- CUSTOMERS ----------------
for i in range(10, 30):
    cursor.execute(
        "INSERT INTO customers VALUES (?, ?, ?, ?)",
        i,
        f"Customer {i}",
        f"customer{i}@example.com",
        random.choice(regions)
    )

# ---------------- SCD TYPE 2 ----------------
sk = 9100
for i in range(10, 30):
    cursor.execute(
        "INSERT INTO dim_customer_scd VALUES (?, ?, ?, ?, ?, ?)",
        sk,
        i,
        f"Customer {i}",
        random.choice(regions),
        "2024-01-01",
        None
    )
    sk += 1

# ---------------- ORDERS ----------------
order_ids = []
for i in range(200, 230):
    cursor.execute(
        "INSERT INTO orders VALUES (?, ?, ?, ?)",
        i,
        random.randint(10, 29),
        random_date(),
        random.choice(statuses)
    )
    order_ids.append(i)

# ---------------- ORDER ITEMS ----------------
oi = 3000
for order_id in order_ids:
    for _ in range(random.randint(1, 2)):
        cursor.execute(
            "INSERT INTO order_items VALUES (?, ?, ?, ?, ?)",
            oi,
            order_id,
            random.randint(210, 219),
            random.randint(1, 5),
            round(random.uniform(10, 50), 2)
        )
        oi += 1

# ---------------- COMMIT ----------------
conn.commit()
cursor.close()
conn.close()

print("✅ SQL Server: 100+ records inserted successfully")
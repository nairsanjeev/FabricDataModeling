# Fabric Notebook — Generate Sample Data for Data Modeling Demo
# ============================================================
# This notebook creates sample retail data in your Fabric Lakehouse.
# It generates BOTH a flat denormalized table (for the bad model)
# and proper star schema tables (for the good model).
#
# Run this in a Fabric notebook connected to your lakehouse.
# ============================================================

# %% Cell 1 — Import libraries and set configuration
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration
NUM_ORDERS = 15000
DATE_START = datetime(2023, 1, 1)
DATE_END = datetime(2025, 12, 31)
RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

print(f"Generating {NUM_ORDERS} sales orders from {DATE_START.date()} to {DATE_END.date()}")

# %% Cell 2 — Define dimension data

# --- Products (50 products across 5 categories) ---
products = []
product_key = 1

categories = {
    "Electronics": {
        "subcategories": {
            "Laptops": [("ThinkPad X1 Carbon", "Lenovo", 899, 1299), ("MacBook Air", "Apple", 799, 1199), ("Surface Laptop", "Microsoft", 749, 1099), ("Dell XPS 13", "Dell", 849, 1249)],
            "Phones": [("iPhone 15", "Apple", 599, 899), ("Galaxy S24", "Samsung", 549, 849), ("Pixel 8", "Google", 449, 699)],
            "Accessories": [("AirPods Pro", "Apple", 129, 249), ("Surface Mouse", "Microsoft", 19, 35), ("USB-C Hub", "Anker", 25, 49)]
        }
    },
    "Clothing": {
        "subcategories": {
            "Tops": [("Classic Polo", "Ralph Lauren", 29, 79), ("Oxford Shirt", "Brooks Brothers", 39, 89), ("Performance Tee", "Nike", 15, 35), ("Cashmere Sweater", "J.Crew", 69, 149)],
            "Bottoms": [("Slim Chinos", "Dockers", 25, 59), ("Athletic Joggers", "Adidas", 29, 65), ("Denim Jeans", "Levi's", 35, 79)],
            "Outerwear": [("Down Jacket", "Patagonia", 99, 229), ("Rain Shell", "Columbia", 49, 119), ("Fleece Vest", "North Face", 39, 89)]
        }
    },
    "Home & Garden": {
        "subcategories": {
            "Kitchen": [("Coffee Maker", "Breville", 89, 199), ("Stand Mixer", "KitchenAid", 199, 399), ("Air Fryer", "Ninja", 59, 129)],
            "Furniture": [("Standing Desk", "Uplift", 349, 699), ("Ergonomic Chair", "Herman Miller", 499, 999), ("Bookshelf", "IKEA", 49, 129)],
            "Garden": [("Robot Mower", "Husqvarna", 499, 999), ("Tool Set", "Fiskars", 29, 69), ("Planter Box", "Gardeners", 19, 45)]
        }
    },
    "Sports & Outdoors": {
        "subcategories": {
            "Fitness": [("Yoga Mat", "Manduka", 29, 79), ("Dumbbells Set", "Bowflex", 149, 349), ("Resistance Bands", "TheraBand", 12, 29)],
            "Outdoor": [("Hiking Boots", "Merrell", 69, 149), ("Camping Tent", "REI", 129, 299), ("Backpack 40L", "Osprey", 89, 189)],
            "Team Sports": [("Basketball", "Wilson", 15, 35), ("Soccer Ball", "Adidas", 19, 39), ("Tennis Racket", "Wilson", 79, 179)]
        }
    },
    "Food & Beverage": {
        "subcategories": {
            "Coffee & Tea": [("Espresso Beans 1lb", "Lavazza", 8, 16), ("Green Tea Box", "Twinings", 4, 9), ("Cold Brew Kit", "Toddy", 19, 39)],
            "Snacks": [("Trail Mix 2lb", "Kirkland", 6, 14), ("Protein Bars 12pk", "KIND", 12, 24), ("Dark Chocolate", "Lindt", 3, 7)],
            "Specialty": [("Olive Oil 750ml", "Colavita", 9, 19), ("Hot Sauce Set", "Cholula", 12, 25)]
        }
    }
}

for cat_name, cat_data in categories.items():
    for subcat_name, items in cat_data["subcategories"].items():
        for prod_name, brand, cost, price in items:
            products.append({
                "ProductKey": product_key,
                "ProductName": prod_name,
                "Category": cat_name,
                "Subcategory": subcat_name,
                "Brand": brand,
                "UnitCost": cost,
                "UnitPrice": price
            })
            product_key += 1

df_products = pd.DataFrame(products)
print(f"Products: {len(df_products)} items across {len(categories)} categories")

# --- Customers (200 customers) ---
segments = ["Enterprise", "Mid-Market", "Small Business", "Consumer"]
loyalty_tiers = ["Platinum", "Gold", "Silver", "Bronze"]
states_cities = [
    ("New York", "NY", "Northeast"), ("Los Angeles", "CA", "West"),
    ("Chicago", "IL", "Midwest"), ("Houston", "TX", "South"),
    ("Phoenix", "AZ", "West"), ("Philadelphia", "PA", "Northeast"),
    ("San Antonio", "TX", "South"), ("San Diego", "CA", "West"),
    ("Dallas", "TX", "South"), ("Seattle", "WA", "Pacific"),
    ("Portland", "OR", "Pacific"), ("Denver", "CO", "West"),
    ("Boston", "MA", "Northeast"), ("Atlanta", "GA", "South"),
    ("Miami", "FL", "South"), ("Minneapolis", "MN", "Midwest"),
    ("Detroit", "MI", "Midwest"), ("Nashville", "TN", "South"),
    ("Charlotte", "NC", "South"), ("San Francisco", "CA", "Pacific")
]

first_names = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda",
               "David", "Elizabeth", "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
               "Thomas", "Sarah", "Christopher", "Karen", "Daniel", "Lisa", "Matthew", "Nancy",
               "Anthony", "Betty", "Mark", "Margaret", "Andrew", "Sandra", "Paul", "Ashley",
               "Steven", "Dorothy", "Kevin", "Kimberly", "Brian", "Emily", "George", "Donna"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
              "Rodriguez", "Martinez", "Anderson", "Taylor", "Thomas", "Moore", "Jackson", "Martin",
              "Lee", "Thompson", "White", "Harris", "Clark", "Lewis", "Robinson", "Walker"]

customers = []
for i in range(1, 201):
    city, state, region = random.choice(states_cities)
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    customers.append({
        "CustomerKey": i,
        "CustomerName": f"{fname} {lname}",
        "Email": f"{fname.lower()}.{lname.lower()}{i}@example.com",
        "City": city,
        "State": state,
        "Country": "United States",
        "Region": region,
        "Segment": random.choices(segments, weights=[15, 25, 30, 30])[0],
        "LoyaltyTier": random.choices(loyalty_tiers, weights=[10, 20, 35, 35])[0]
    })

df_customers = pd.DataFrame(customers)
print(f"Customers: {len(df_customers)} across {len(set(c['Segment'] for c in customers))} segments")

# --- Stores (10 stores) ---
stores = [
    {"StoreKey": 1, "StoreName": "Contoso Flagship NYC", "City": "New York", "State": "NY", "Country": "United States", "Region": "Northeast", "StoreType": "Flagship", "OpenDate": "2018-03-15", "SquareFootage": 25000},
    {"StoreKey": 2, "StoreName": "Contoso LA Premium", "City": "Los Angeles", "State": "CA", "Country": "United States", "Region": "West", "StoreType": "Premium", "OpenDate": "2019-06-01", "SquareFootage": 18000},
    {"StoreKey": 3, "StoreName": "Contoso Chicago Central", "City": "Chicago", "State": "IL", "Country": "United States", "Region": "Midwest", "StoreType": "Standard", "OpenDate": "2017-09-20", "SquareFootage": 12000},
    {"StoreKey": 4, "StoreName": "Contoso Houston South", "City": "Houston", "State": "TX", "Country": "United States", "Region": "South", "StoreType": "Standard", "OpenDate": "2020-01-10", "SquareFootage": 14000},
    {"StoreKey": 5, "StoreName": "Contoso Seattle Tech", "City": "Seattle", "State": "WA", "Country": "United States", "Region": "Pacific", "StoreType": "Premium", "OpenDate": "2019-11-05", "SquareFootage": 16000},
    {"StoreKey": 6, "StoreName": "Contoso Boston Harbor", "City": "Boston", "State": "MA", "Country": "United States", "Region": "Northeast", "StoreType": "Standard", "OpenDate": "2020-04-15", "SquareFootage": 11000},
    {"StoreKey": 7, "StoreName": "Contoso Miami Beach", "City": "Miami", "State": "FL", "Country": "United States", "Region": "South", "StoreType": "Premium", "OpenDate": "2021-02-28", "SquareFootage": 15000},
    {"StoreKey": 8, "StoreName": "Contoso Denver Mountain", "City": "Denver", "State": "CO", "Country": "United States", "Region": "West", "StoreType": "Standard", "OpenDate": "2021-07-01", "SquareFootage": 10000},
    {"StoreKey": 9, "StoreName": "Contoso Portland Green", "City": "Portland", "State": "OR", "Country": "United States", "Region": "Pacific", "StoreType": "Standard", "OpenDate": "2022-03-10", "SquareFootage": 9000},
    {"StoreKey": 10, "StoreName": "Contoso Atlanta Metro", "City": "Atlanta", "State": "GA", "Country": "United States", "Region": "South", "StoreType": "Outlet", "OpenDate": "2022-08-15", "SquareFootage": 20000}
]
df_stores = pd.DataFrame(stores)
print(f"Stores: {len(df_stores)} across {len(set(s['Region'] for s in stores))} regions")

# --- Promotions (6 promotions) ---
promotions = [
    {"PromotionKey": 0, "PromotionName": "No Promotion", "DiscountPercent": 0, "StartDate": "2023-01-01", "EndDate": "2025-12-31", "PromotionCategory": "None"},
    {"PromotionKey": 1, "PromotionName": "Summer Blowout", "DiscountPercent": 25, "StartDate": "2024-06-01", "EndDate": "2024-08-31", "PromotionCategory": "Seasonal"},
    {"PromotionKey": 2, "PromotionName": "Black Friday Deal", "DiscountPercent": 35, "StartDate": "2024-11-25", "EndDate": "2024-12-02", "PromotionCategory": "Holiday"},
    {"PromotionKey": 3, "PromotionName": "Loyalty Member Exclusive", "DiscountPercent": 15, "StartDate": "2023-01-01", "EndDate": "2025-12-31", "PromotionCategory": "Loyalty"},
    {"PromotionKey": 4, "PromotionName": "New Customer Welcome", "DiscountPercent": 20, "StartDate": "2023-01-01", "EndDate": "2025-12-31", "PromotionCategory": "Acquisition"},
    {"PromotionKey": 5, "PromotionName": "End of Season Clearance", "DiscountPercent": 40, "StartDate": "2024-09-01", "EndDate": "2024-09-30", "PromotionCategory": "Clearance"}
]
df_promotions = pd.DataFrame(promotions)
print(f"Promotions: {len(df_promotions)}")

# %% Cell 3 — Generate Calendar dimension

date_range = pd.date_range(start=DATE_START, end=DATE_END, freq='D')
calendar_data = []

for d in date_range:
    fiscal_month = (d.month - 6) % 12  # Fiscal year starts July
    fiscal_year = d.year if d.month >= 7 else d.year - 1
    fiscal_quarter = (fiscal_month // 3) + 1

    calendar_data.append({
        "DateKey": int(d.strftime("%Y%m%d")),
        "Date": d.strftime("%Y-%m-%d"),
        "Year": d.year,
        "Quarter": f"Q{d.quarter}",
        "QuarterNumber": d.quarter,
        "Month": d.strftime("%B"),
        "MonthNumber": d.month,
        "MonthYear": d.strftime("%b %Y"),
        "Week": d.isocalendar()[1],
        "DayOfWeek": d.strftime("%A"),
        "DayOfWeekNumber": d.weekday() + 1,
        "IsWeekend": 1 if d.weekday() >= 5 else 0,
        "IsHoliday": 0,  # Simplified
        "FiscalYear": f"FY{fiscal_year + 1}",
        "FiscalYearNumber": fiscal_year + 1,
        "FiscalQuarter": f"FQ{fiscal_quarter}",
        "FiscalQuarterNumber": fiscal_quarter,
        "YearMonth": int(d.strftime("%Y%m"))
    })

df_calendar = pd.DataFrame(calendar_data)
print(f"Calendar: {len(df_calendar)} days from {DATE_START.date()} to {DATE_END.date()}")

# %% Cell 4 — Generate Sales fact table

sales = []
order_key = 1

# Generate dates weighted toward more recent (business growing)
all_dates = pd.date_range(start=DATE_START, end=DATE_END, freq='D')
date_weights = np.linspace(0.5, 1.5, len(all_dates))
date_weights = date_weights / date_weights.sum()

for _ in range(NUM_ORDERS):
    # Pick a random date (weighted toward recent)
    order_date = pd.Timestamp(np.random.choice(all_dates, p=date_weights))
    date_key = int(order_date.strftime("%Y%m%d"))

    # Pick random dimensions
    product = df_products.iloc[random.randint(0, len(df_products) - 1)]
    customer = df_customers.iloc[random.randint(0, len(df_customers) - 1)]
    store = df_stores.iloc[random.randint(0, len(df_stores) - 1)]

    # Determine promotion (70% no promo, 30% some promo)
    if random.random() < 0.7:
        promo_key = 0
        discount_pct = 0
    else:
        promo = df_promotions.iloc[random.randint(1, len(df_promotions) - 1)]
        promo_key = promo["PromotionKey"]
        discount_pct = promo["DiscountPercent"]

    quantity = random.choices([1, 2, 3, 4, 5], weights=[40, 30, 15, 10, 5])[0]
    unit_price = product["UnitPrice"]
    unit_cost = product["UnitCost"]
    discount_amount = round(unit_price * quantity * (discount_pct / 100), 2)
    sales_amount = round(unit_price * quantity - discount_amount, 2)
    cost_amount = round(unit_cost * quantity, 2)

    sales.append({
        "OrderKey": order_key,
        "DateKey": date_key,
        "CustomerKey": int(customer["CustomerKey"]),
        "ProductKey": int(product["ProductKey"]),
        "StoreKey": int(store["StoreKey"]),
        "PromotionKey": int(promo_key),
        "Quantity": quantity,
        "UnitPrice": float(unit_price),
        "DiscountAmount": discount_amount,
        "SalesAmount": sales_amount,
        "CostAmount": cost_amount
    })
    order_key += 1

df_sales = pd.DataFrame(sales)
print(f"Sales: {len(df_sales)} orders, Total Revenue: ${df_sales['SalesAmount'].sum():,.2f}")

# %% Cell 5 — Create FLAT denormalized table (for the Bad Model)

# Merge everything into one ugly flat table with abbreviated column names
df_flat = df_sales.merge(df_products, on="ProductKey") \
                  .merge(df_customers, on="CustomerKey", suffixes=('', '_cust')) \
                  .merge(df_stores, on="StoreKey", suffixes=('', '_store')) \
                  .merge(df_promotions, on="PromotionKey") \
                  .merge(df_calendar, on="DateKey")

# Rename to ugly abbreviated names (simulating a poorly modeled source)
flat_rename = {
    "OrderKey": "id",
    "Date": "dt",
    "Year": "yr",
    "Month": "mo",
    "MonthNumber": "mo_num",
    "Quarter": "qtr",
    "DayOfWeek": "dow",
    "IsWeekend": "is_wknd",
    "FiscalYear": "fy",
    "CustomerName": "cust_nm",
    "Email": "cust_email",
    "City": "cust_city",
    "State": "cust_st",
    "Region": "cust_region",
    "Segment": "cust_seg",
    "LoyaltyTier": "cust_loyalty",
    "ProductName": "prod_nm",
    "Category": "prod_cat",
    "Subcategory": "prod_subcat",
    "Brand": "prod_brand",
    "Quantity": "qty",
    "UnitPrice": "unit_px",
    "UnitCost": "unit_cst",
    "DiscountAmount": "disc_amt",
    "SalesAmount": "amt",
    "CostAmount": "cst_amt",
    "StoreName": "store_nm",
    "City_store": "store_city",
    "State_store": "store_st",
    "Region_store": "store_region",
    "StoreType": "store_type",
    "SquareFootage": "store_sqft",
    "PromotionName": "promo_nm",
    "DiscountPercent": "disc_pct",
    "PromotionCategory": "promo_cat"
}

# Select and rename columns for the flat table
flat_columns = list(flat_rename.keys())
df_flat_final = df_flat[[c for c in flat_columns if c in df_flat.columns]].copy()
df_flat_final = df_flat_final.rename(columns={k: v for k, v in flat_rename.items() if k in df_flat_final.columns})

print(f"Flat table: {len(df_flat_final)} rows, {len(df_flat_final.columns)} columns")
print(f"Columns: {list(df_flat_final.columns)}")

# %% Cell 6 — Write all tables to Lakehouse as Delta tables

# Convert to Spark DataFrames and save as Delta tables
spark_sales = spark.createDataFrame(df_sales)
spark_products = spark.createDataFrame(df_products)
spark_customers = spark.createDataFrame(df_customers)
spark_stores = spark.createDataFrame(df_stores)
spark_promotions = spark.createDataFrame(df_promotions)
spark_calendar = spark.createDataFrame(df_calendar)
spark_flat = spark.createDataFrame(df_flat_final)

# Write star schema tables
spark_sales.write.mode("overwrite").format("delta").saveAsTable("sales")
spark_products.write.mode("overwrite").format("delta").saveAsTable("product")
spark_customers.write.mode("overwrite").format("delta").saveAsTable("customer")
spark_stores.write.mode("overwrite").format("delta").saveAsTable("store")
spark_promotions.write.mode("overwrite").format("delta").saveAsTable("promotion")
spark_calendar.write.mode("overwrite").format("delta").saveAsTable("calendar")

# Write flat denormalized table
spark_flat.write.mode("overwrite").format("delta").saveAsTable("sales_data_flat")

print("✅ All tables written to Lakehouse successfully!")
print()
print("Star Schema Tables:")
print("  - sales (fact table)")
print("  - product (dimension)")
print("  - customer (dimension)")
print("  - store (dimension)")
print("  - calendar (dimension)")
print("  - promotion (dimension)")
print()
print("Flat Table:")
print("  - sales_data_flat (denormalized)")

# %% Cell 7 — Verify the data

print("=" * 60)
print("DATA VERIFICATION")
print("=" * 60)

for table_name in ["sales", "product", "customer", "store", "promotion", "calendar", "sales_data_flat"]:
    df = spark.sql(f"SELECT COUNT(*) as cnt FROM {table_name}")
    count = df.collect()[0]["cnt"]
    print(f"  {table_name}: {count:,} rows")

print()
print("Sample sales data:")
spark.sql("SELECT * FROM sales LIMIT 5").show()

print("Sample flat data:")
spark.sql("SELECT * FROM sales_data_flat LIMIT 3").show(truncate=False)

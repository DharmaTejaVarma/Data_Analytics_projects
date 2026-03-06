# Set up project structure
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create directories
base_dir = r"d:\Data_Analyst\E-Commerce Revenue & Customer Intelligence System\Scripts\Ecommerce-Revenue-Analytics"
dirs = [
    os.path.join(base_dir, 'data'),
    os.path.join(base_dir, 'notebooks'),
    os.path.join(base_dir, 'scripts'),
    os.path.join(base_dir, 'visuals')
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Generate dummy data
np.random.seed(42)

# 1. customers.csv
n_customers = 15000
customers = pd.DataFrame({
    'customer_id': range(1, n_customers + 1),
    'name': [f'Customer_{i}' for i in range(1, n_customers + 1)],
    'email': [f'customer_{i}@example.com' for i in range(1, n_customers + 1)],
    'signup_date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n_customers)],
    'country': np.random.choice(['USA', 'UK', 'Canada', 'Australia', 'Germany'], n_customers)
})
# Inject some missing values
customers.loc[np.random.choice(customers.index, 50), 'country'] = np.nan
customers.to_csv(os.path.join(base_dir, 'data', 'customers.csv'), index=False)

# 2. orders.csv
n_orders = 60000
orders = pd.DataFrame({
    'order_id': range(1001, 1001 + n_orders),
    'customer_id': np.random.choice(customers['customer_id'], n_orders),
    'order_date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n_orders)],
    'status': np.random.choice(['Completed', 'Processing', 'Cancelled'], n_orders, p=[0.85, 0.1, 0.05])
})
# Inject some duplicated rows
orders = pd.concat([orders, orders.sample(100)]).reset_index(drop=True)
# Inject messy date formats for cleaning
messy_idx = np.random.choice(orders.index, 200, replace=False)
orders.loc[messy_idx, 'order_date'] = orders.loc[messy_idx, 'order_date'].dt.strftime('%d-%m-%Y')
orders.to_csv(os.path.join(base_dir, 'data', 'orders.csv'), index=False)

# 3. order_items.csv
n_items = 150000
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Toys']
order_items = pd.DataFrame({
    'order_item_id': range(1, n_items + 1),
    'order_id': np.random.choice(orders['order_id'], n_items),
    'product_id': np.random.randint(100, 500, n_items),
    'category': np.random.choice(categories, n_items),
    'price': np.round(np.random.uniform(10.0, 500.0, n_items), 2),
    'quantity': np.random.randint(1, 5, n_items)
})
order_items.to_csv(os.path.join(base_dir, 'data', 'order_items.csv'), index=False)

# 4. refunds.csv
n_refunds = 4000
refunds = pd.DataFrame({
    'refund_id': range(1, n_refunds + 1),
    'order_id': np.random.choice(orders[orders['status'] == 'Completed']['order_id'], n_refunds),
    'refund_date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n_refunds)],
    'refund_amount': np.round(np.random.uniform(10.0, 200.0, n_refunds), 2),
    'reason': np.random.choice(['Defective', 'Wrong Item', 'Changed Mind'], n_refunds)
})
# Make sure refund date is after order date (roughly)
refunds.to_csv(os.path.join(base_dir, 'data', 'refunds.csv'), index=False)

# 5. traffic.csv
n_traffic_records = 365
start_date = datetime(2023, 1, 1)
traffic = pd.DataFrame({
    'date': [start_date + timedelta(days=i) for i in range(n_traffic_records)],
    'website_visits': np.random.randint(1000, 5000, n_traffic_records),
    'marketing_channel': np.random.choice(['Organic', 'Paid Search', 'Social Media', 'Email'], n_traffic_records)
})
# Standardize column names later (we make this messy intentionally)
traffic.rename(columns={'website_visits': 'Website Visits', 'marketing_channel': 'Marketing-Channel', 'date': 'Date'}, inplace=True)
traffic.to_csv(os.path.join(base_dir, 'data', 'traffic.csv'), index=False)

print("Project structure and dummy datasets generated successfully.")

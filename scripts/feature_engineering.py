import pandas as pd

def calculate_item_revenue(order_items):
    """Create revenue column (price * quantity)."""
    df = order_items.copy()
    if 'price' in df.columns and 'quantity' in df.columns:
        df['revenue'] = df['price'] * df['quantity']
    return df

def merge_orders_and_items(orders, order_items):
    """Merge order_items with orders."""
    merged = pd.merge(order_items, orders, on='order_id', how='left')
    return merged

def create_date_features(df, date_col='order_date'):
    """Create month/year features from a datetime column."""
    if date_col in df.columns:
        df['order_year'] = df[date_col].dt.year
        df['order_month'] = df[date_col].dt.month
        df['order_year_month'] = df[date_col].dt.to_period('M')
    return df

def calculate_customer_lifetime_revenue(merged_df):
    """Calculate customer lifetime revenue (CLV)."""
    if 'customer_id' in merged_df.columns and 'revenue' in merged_df.columns:
        # Filter for completed orders
        completed = merged_df[merged_df['status'] == 'Completed']
        clv = completed.groupby('customer_id')['revenue'].sum().reset_index()
        clv.rename(columns={'revenue': 'lifetime_revenue'}, inplace=True)
        return clv
    return pd.DataFrame()

def apply_feature_engineering(orders_clean, order_items_clean):
    """Wrapper to apply all feature engineering steps."""
    items = calculate_item_revenue(order_items_clean)
    merged = merge_orders_and_items(orders_clean, items)
    merged = create_date_features(merged, 'order_date')
    clv = calculate_customer_lifetime_revenue(merged)
    
    return merged, clv

import pandas as pd
import numpy as np

def clean_column_names(df):
    """Standardize column names to lowercase with underscores."""
    df.columns = df.columns.astype(str).str.lower().str.replace(' ', '_').str.replace('-', '_')
    return df

def clean_customers(df):
    """Clean customers dataframe."""
    df = clean_column_names(df)
    
    # Handle missing values (fill NaN country with 'Unknown')
    if 'country' in df.columns:
        df['country'] = df['country'].fillna('Unknown')
        
    # Convert date columns to datetime
    if 'signup_date' in df.columns:
        df['signup_date'] = pd.to_datetime(df['signup_date'])
        
    # Remove duplicates
    df = df.drop_duplicates()
    return df

def clean_orders(df):
    """Clean orders dataframe."""
    df = clean_column_names(df)
    
    # Remove obvious duplicates
    df = df.drop_duplicates(subset=['order_id'], keep='first')
        
    # Convert date columns to datetime
    # Some dates are in '%d-%m-%Y' and some are in '%Y-%m-%d %H:%M:%S'
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True)
        
    return df

def clean_traffic(df):
    """Clean traffic dataframe."""
    df = clean_column_names(df)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Convert date columns
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        
    return df

def clean_order_items(df):
    """Clean order items dataframe."""
    df = clean_column_names(df)
    df = df.drop_duplicates()
    return df

def clean_refunds(df):
    """Clean refunds dataframe."""
    df = clean_column_names(df)
    df = df.drop_duplicates()
    if 'refund_date' in df.columns:
        df['refund_date'] = pd.to_datetime(df['refund_date'])
    return df

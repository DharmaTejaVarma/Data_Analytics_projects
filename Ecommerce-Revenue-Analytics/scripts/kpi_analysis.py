import pandas as pd

def calculate_total_revenue(merged_df):
    """Calculate total revenue from completed orders."""
    completed = merged_df[merged_df['status'] == 'Completed']
    return completed['revenue'].sum()

def calculate_aov(merged_df):
    """Calculate Average Order Value (AOV) for completed orders."""
    completed = merged_df[merged_df['status'] == 'Completed']
    if completed['order_id'].nunique() == 0:
        return 0
    return completed['revenue'].sum() / completed['order_id'].nunique()

def calculate_conversion_rate(orders_df, traffic_df):
    """
    Calculate conversion rate.
    Uses unique orders count / total website visits.
    """
    total_orders = orders_df['order_id'].nunique()
    total_visits = traffic_df['website_visits'].sum()
    if total_visits == 0:
        return 0
    return (total_orders / total_visits) * 100

def calculate_refund_rate(orders_df, refunds_df):
    """
    Calculate Refund Rate based on number of orders vs number of refunds.
    """
    total_completed_orders = orders_df[orders_df['status'] == 'Completed']['order_id'].nunique()
    total_refunds = refunds_df['refund_id'].nunique()
    if total_completed_orders == 0:
        return 0
    return (total_refunds / total_completed_orders) * 100

def get_revenue_by_category(merged_df):
    """Group revenue by product category from completed orders."""
    completed = merged_df[merged_df['status'] == 'Completed']
    return completed.groupby('category')['revenue'].sum().sort_values(ascending=False).reset_index()

def get_revenue_by_marketing_channel(merged_df, traffic_df):
    """
    Estimate revenue by marketing channel.
    This groups traffic by marketing channel and estimates the impact by 
    calculating the share of website visits per channel.
    """
    # Group website visits by marketing channel
    channel_visits = traffic_df.groupby('marketing_channel')['website_visits'].sum().reset_index()
    total_visits = channel_visits['website_visits'].sum()
    
    # Simple attribution based on traffic share
    channel_visits['visit_share'] = channel_visits['website_visits'] / total_visits
    
    total_revenue = calculate_total_revenue(merged_df)
    channel_visits['estimated_revenue'] = channel_visits['visit_share'] * total_revenue
    
    return channel_visits.sort_values(by='estimated_revenue', ascending=False)

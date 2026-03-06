
# Data_Analytics_projects

# Ecommerce Revenue Analytics

## Project Overview
This repository contains a professional Data Analytics project focused on examining E-commerce sales data, computing key performance metrics (KPIs), and building an end-to-end data processing pipeline utilizing Python. Designed as a portfolio project, it demonstrates best practices in clean code architecture, data cleaning, feature engineering, and data visualization.

## Objectives
- Clean raw e-commerce data (handling missing values, standardizing dates).
- Engineer features (Customer Lifetime Value, Revenue per item, Date metrics).
- Calculate critical business KPIs (Average Order Value, Conversion Rate).
- Visualize findings with Python plotting libraries to distill actionable business insights.

## Project Structure
```text
Ecommerce-Revenue-Analytics
│
├── data/                  # Contains raw datasets (mock data)
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── refunds.csv
│   └── traffic.csv
│
├── notebooks/             # Jupyter notebooks for interactive analysis
│   └── analysis.ipynb
│
├── scripts/               # Modularized Python scripts
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── kpi_analysis.py
│
├── visuals/               # Generated charts and graphs (.png)
│   ├── revenue_trend.png
│   ├── category_revenue.png
│   └── conversion_rate.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Dataset Description
The project relies on a relational dataset consisting of 5 tabular files:
1. **customers.csv**: Customer demographic and signup data (15,000+ rows).
2. **orders.csv**: Transactional log of orders (60,000+ rows).
3. **order_items.csv**: Line-item details (quantities, prices, categories - 150,000+ rows).
4. **refunds.csv**: Logged refunds and reasons.
5. **traffic.csv**: Website visits and marketing channel attribution.

*(Note: Data is mock-generated at scale for demonstration purposes)*

## Tools Used
- **Python 3**: Core programming language.
- **Pandas**: Data manipulation, aggregation, and analysis.
- **NumPy**: Numerical operations.
- **Matplotlib/Seaborn**: Data visualization and aesthetic charting.
- **Jupyter Notebook**: Interactive execution and storytelling.

## Key Business Insights
1. **Revenue Trends**: We observed variable revenue across the year with specific months outperforming others, likely due to seasonal variations or marketing campaigns.
2. **Top Product Categories**: Certain categories generated the vast majority of revenue, suggesting a need to focus inventory and advertising spend on these high-performers.
3. **Conversion vs Drop-off**: A large portion of web traffic does not convert, providing an opportunity for A/B testing checkout flows or retargeting marketing. 

## How to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd Ecommerce-Revenue-Analytics
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Analysis**:
   - Start a Jupyter server: `jupyter notebook`
   - Open `notebooks/analysis.ipynb` and run all cells sequentially.
   - Alternatively, execute the notebook from the command line:
     ```bash
     jupyter nbconvert --to notebook --execute notebooks/analysis.ipynb
     ```
4. **View Visualizations**:
   The generated charts are saved directly into the `visuals/` directory.

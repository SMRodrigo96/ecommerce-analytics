# E-Commerce Customer Analytics

Customer analytics project using transactional e-commerce data.

This project explores customer purchasing behavior through:

- Exploratory Data Analysis (EDA)
- Revenue analysis
- Product performance analysis
- Geographic sales analysis
- RFM customer segmentation
- KMeans clustering

---

# Dataset

The dataset used is the Online Retail dataset containing over 500,000 e-commerce transactions between 2010 and 2011.

Main features include:

- Invoice number
- Product description
- Quantity purchased
- Invoice date
- Unit price
- Customer ID
- Country

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

# Project Structure

```bash
ecommerce-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── outputs/
│   └── charts/
│
├── src/
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   ├── data_visualization.py
│   └── customer_segmentation.py
│
└── README.md
```

---

# Key Insights

- Most customers purchase infrequently.
- A small segment of customers generates most revenue.
- The United Kingdom dominates sales volume.
- Customer spending behavior is highly skewed.
- KMeans clustering successfully identified distinct customer segments.

---

# Customer Segmentation Example

(Add customer_segments.png screenshot here)

---

# Future Improvements

- Interactive dashboard using Streamlit or Power BI
- Predictive customer lifetime value modeling
- Advanced customer retention analysis

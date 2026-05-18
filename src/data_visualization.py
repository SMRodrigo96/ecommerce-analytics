import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Style
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Output folder
OUTPUT_PATH = Path("outputs/charts")
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def load_data():
    """
    Load cleaned dataset.
    """
    df = pd.read_csv("data/processed/online_retail_clean.csv")
    return df


def revenue_by_month(df):
    """
    Plot monthly revenue trend.
    """

    monthly_sales = (
        df.groupby(["year", "month"])["total_price"]
        .sum()
        .reset_index()
    )

    monthly_sales["date"] = pd.to_datetime(
        monthly_sales["year"].astype(str)
        + "-"
        + monthly_sales["month"].astype(str)
    )

    plt.figure()

    sns.lineplot(
        data=monthly_sales,
        x="date",
        y="total_price",
        marker="o"
    )

    plt.title("Monthly Revenue Trend", fontsize=16)
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(OUTPUT_PATH / "monthly_revenue.png")
    plt.show()


def top_products_chart(df):
    """
    Plot top products by revenue.
    """

    top_products = (
        df.groupby("description")["total_price"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure()

    sns.barplot(
        x=top_products.values,
        y=top_products.index
    )

    plt.title("Top 10 Products by Revenue", fontsize=16)
    plt.xlabel("Revenue")
    plt.ylabel("Product")

    plt.tight_layout()

    plt.savefig(OUTPUT_PATH / "top_products.png")
    plt.show()


def revenue_by_country(df):
    """
    Plot top countries by revenue.
    """

    countries = (
        df.groupby("country")["total_price"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure()

    sns.barplot(
        x=countries.values,
        y=countries.index
    )

    plt.title("Top 10 Countries by Revenue", fontsize=16)
    plt.xlabel("Revenue")
    plt.ylabel("Country")

    plt.tight_layout()

    plt.savefig(OUTPUT_PATH / "top_countries.png")
    plt.show()


def main():

    print("Loading dataset...")
    df = load_data()

    print("Generating charts...")

    revenue_by_month(df)
    top_products_chart(df)
    revenue_by_country(df)

    print("Charts saved successfully.")


if __name__ == "__main__":
    main()
import pandas as pd

def load_data():
    print("Loading cleaned dataset...")
    df = pd.read_csv("data/processed/online_retail_clean.csv")
    print("Dataset loaded.")
    return df


def basic_info(df):

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nFirst rows:")
    print(df.head())


def sales_metrics(df):

    print("\n--- SALES METRICS ---")

    total_revenue = df["total_price"].sum()
    total_orders = df["invoice"].nunique()
    total_customers = df["customer_id"].nunique()

    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Orders: {total_orders}")
    print(f"Total Customers: {total_customers}")


def top_products(df):

    print("\n--- TOP PRODUCTS ---")

    top_products = (
        df.groupby("description")["total_price"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top_products)


def top_countries(df):

    print("\n--- TOP COUNTRIES ---")

    countries = (
        df.groupby("country")["total_price"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(countries)


def main():

    df = load_data()

    basic_info(df)

    sales_metrics(df)

    top_products(df)

    top_countries(df)


if __name__ == "__main__":
    main()
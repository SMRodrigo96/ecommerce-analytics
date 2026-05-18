import pandas as pd
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/online_retail_II.xlsx")
PROCESSED_DATA_PATH = Path("data/processed/online_retail_clean.csv")


def load_data():
    print("Loading dataset...")

    df = pd.read_excel(
        RAW_DATA_PATH,
        sheet_name="Year 2010-2011",
        engine="openpyxl"
    )

    print("Dataset loaded successfully.")
    return df


def initial_inspection(df):

    print("\nDataset Shape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())


def normalize_columns(df):

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def clean_data(df):

    print("\nCleaning dataset...")

    initial_rows = len(df)

    df = df.dropna(subset=["customer_id"])
    df = df[~df["invoice"].astype(str).str.startswith("C")]
    df = df[df["quantity"] > 0]
    df = df[df["price"] > 0]

    df = df.drop_duplicates()

    final_rows = len(df)

    print(f"Rows removed: {initial_rows - final_rows}")
    print(f"Rows remaining: {final_rows}")

    return df


def create_features(df):

    print("\nCreating features...")

    df["invoicedate"] = pd.to_datetime(df["invoicedate"])
    df["total_price"] = df["quantity"] * df["price"]

    df["year"] = df["invoicedate"].dt.year
    df["month"] = df["invoicedate"].dt.month

    return df


def save_data(df):

    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(PROCESSED_DATA_PATH, index=False)

    print("\nClean dataset saved.")
    print(f"Location: {PROCESSED_DATA_PATH}")


def main():

    df = load_data()

    initial_inspection(df)

    df = normalize_columns(df)

    df = clean_data(df)

    df = create_features(df)

    save_data(df)


if __name__ == "__main__":
    main()
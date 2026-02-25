import pandas as pd
from pathlib import Path


def load_data():
    """
    Load Online Retail II dataset from Excel file.
    """
    data_path = Path("data/raw/online_retail_II.xlsx")

    try:
        df = pd.read_excel(data_path, sheet_name="Year 2010-2011")
        print("Dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def initial_inspection(df):
    """
    Perform basic inspection of the dataset.
    """
    print("\n--- Dataset Info ---")
    print(df.info())

    print("\n--- First 5 Rows ---")
    print(df.head())

    print("\n--- Missing Values ---")
    print(df.isnull().sum())


if __name__ == "__main__":
    df = load_data()

    if df is not None:
        initial_inspection(df)
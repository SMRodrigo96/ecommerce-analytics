import pandas as pd
import numpy as np

from datetime import timedelta

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    """
    Load cleaned ecommerce dataset.
    """

    df = pd.read_csv("data/processed/online_retail_clean.csv")

    df["invoicedate"] = pd.to_datetime(df["invoicedate"])

    return df


def create_rfm(df):
    """
    Create RFM metrics table.
    """

    snapshot_date = df["invoicedate"].max() + timedelta(days=1)

    rfm = df.groupby("customer_id").agg({
        "invoicedate": lambda x: (snapshot_date - x.max()).days,
        "invoice": "nunique",
        "total_price": "sum"
    })

    rfm.columns = ["recency", "frequency", "monetary"]

    return rfm


def preprocess_rfm(rfm):
    """
    Preprocess RFM data for clustering.
    """

    # Remove invalid values
    rfm = rfm[(rfm["monetary"] > 0)]

    # Log transformation
    rfm_log = np.log1p(rfm)

    # Scaling
    scaler = StandardScaler()

    rfm_scaled = scaler.fit_transform(rfm_log)

    return rfm, rfm_scaled


def apply_kmeans(rfm, rfm_scaled):
    """
    Apply KMeans clustering.
    """

    kmeans = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    kmeans.fit(rfm_scaled)

    rfm["cluster"] = kmeans.labels_

    return rfm


def cluster_summary(rfm):
    """
    Show cluster statistics.
    """

    summary = rfm.groupby("cluster").agg({
        "recency": "mean",
        "frequency": "mean",
        "monetary": "mean"
    })

    print("\nCluster Summary:")
    print(summary)


def plot_clusters(rfm):
    """
    Visualize customer clusters.
    """

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=rfm,
        x="frequency",
        y="monetary",
        hue="cluster",
        palette="Set2",
        s=100
    )

    plt.title("Customer Segments")
    plt.xlabel("Frequency")
    plt.ylabel("Monetary")

    plt.yscale("log")

    plt.tight_layout()

    plt.savefig("outputs/charts/customer_segments.png")

    plt.show()


def main():

    print("Loading dataset...")
    df = load_data()

    print("Creating RFM table...")
    rfm = create_rfm(df)

    print("Preprocessing RFM...")
    rfm, rfm_scaled = preprocess_rfm(rfm)

    print("Applying KMeans...")
    rfm = apply_kmeans(rfm, rfm_scaled)

    cluster_summary(rfm)

    print("Generating cluster visualization...")
    plot_clusters(rfm)

    # Save results
    rfm.to_csv(
        "data/processed/customer_segments.csv",
        index=True
    )

    print("\nCustomer segments saved.")


if __name__ == "__main__":
    main()
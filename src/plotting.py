import os
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def compare_loop_vectorized(
    df: pd.DataFrame,
    sample_size: int = 10000,
    runs: int = 5
) -> dict:
    """
    Compare loop and vectorized calculations using a fixed-seed sample.

    Parameters:
        df: Filtered Customs 2015 DataFrame.
        sample_size: Number of records used for the comparison.
        runs: Number of timing runs.

    Returns:
        A dictionary containing comparison results and median times.
    """

    # Select a fixed sample so the comparison is reproducible.
    sample = df.sample(
        n=min(sample_size, len(df)),
        random_state=42
    )

    # Convert the dutiable value column into a NumPy array.
    values = sample["dutiablevaluephp"].to_numpy()

    # Loop calculation.
    loop_times = []
    loop_result = None

    for _ in range(runs):
        start_time = time.perf_counter()

        loop_result = np.array([
            value / 1_000_000
            for value in values
        ])

        loop_times.append(
            time.perf_counter() - start_time
        )

    # Vectorized calculation.
    vectorized_times = []
    vectorized_result = None

    for _ in range(runs):
        start_time = time.perf_counter()

        vectorized_result = values / 1_000_000

        vectorized_times.append(
            time.perf_counter() - start_time
        )

    # Boolean mask for high-value records.
    high_value_mask = values >= 10_000_000

    return {
        "loop_result": loop_result,
        "vectorized_result": vectorized_result,
        "results_equal": np.array_equal(
            loop_result,
            vectorized_result
        ),
        "loop_median_time": np.median(loop_times),
        "vectorized_median_time": np.median(
            vectorized_times
        ),
        "high_value_count": np.sum(high_value_mask)
    }


def create_bar_plot(
    df: pd.DataFrame,
    output_folder: str = "output"
) -> None:
    """
    Create a bar plot of the top 10 dutiable values.

    Parameters:
        df: Filtered Customs 2015 DataFrame.
        output_folder: Folder where the plot will be saved.
    """

    # Create output folder if it does not exist.
    os.makedirs(output_folder, exist_ok=True)

    # Select the top 10 records by dutiable value.
    top10 = df.nlargest(
        10,
        "dutiablevaluephp"
    ).copy()

    # Sort so the largest value appears at the top.
    top10 = top10.sort_values(
        "dutiablevaluephp"
    )

    # Create labels using country and quarter.
    labels = (
        top10["countryorigin_iso3"]
        + " - "
        + top10["tq"]
    )

    # Convert PHP to millions of PHP.
    values = (
        top10["dutiablevaluephp"] / 1_000_000
    )

    plt.figure(figsize=(10, 6))

    plt.barh(
        labels,
        values
    )

    plt.title(
        "Top 10 Customs Records by Dutiable Value"
    )
    plt.xlabel(
        "Dutiable Value (Million PHP)"
    )
    plt.ylabel(
        "Country and Quarter"
    )

    plt.tight_layout()

    plt.savefig(
        f"{output_folder}/bar.png"
    )

    plt.close()


def create_heatmap(
    df: pd.DataFrame,
    output_folder: str = "output"
) -> None:
    """
    Create a heatmap of total dutiable value by country and quarter.

    Parameters:
        df: Filtered Customs 2015 DataFrame.
        output_folder: Folder where the plot will be saved.
    """

    # Create output folder if it does not exist.
    os.makedirs(output_folder, exist_ok=True)

    # Create a country-by-quarter summary.
    pivot = pd.pivot_table(
        df,
        index="countryorigin_iso3",
        columns="tq",
        values="dutiablevaluephp",
        aggfunc="sum",
        fill_value=0
    )

    plt.figure(figsize=(10, 12))

    plt.imshow(
        pivot.values,
        aspect="auto"
    )

    plt.colorbar(
        label="Dutiable Value (PHP)"
    )

    plt.title(
        "Dutiable Value by Country and Quarter"
    )
    plt.xlabel("Quarter")
    plt.ylabel("Country of Origin")

    plt.xticks(
        range(len(pivot.columns)),
        pivot.columns
    )

    plt.yticks(
        range(len(pivot.index)),
        pivot.index
    )

    plt.tight_layout()

    plt.savefig(
        f"{output_folder}/heatmap.png"
    )

    plt.close()
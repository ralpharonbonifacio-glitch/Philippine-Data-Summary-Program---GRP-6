import os
import pandas as pd

from config import GROUPING_COLUMNS


def create_summary_tables(
    df: pd.DataFrame,
    output_folder: str = "output"
) -> dict:
    """
    Create grouped, two-column grouped, pivot, and top-10 summary tables.

    Parameters:
        df: Filtered and transformed Customs 2015 DataFrame.
        output_folder: Folder where summary CSV files will be saved.

    Returns:
        A dictionary containing the four summary DataFrames.
    """

    # Create the output folder if it does not exist.
    os.makedirs(output_folder, exist_ok=True)

    # Group by country of origin.
    grouped = (
        df.groupby(
            GROUPING_COLUMNS[0],
            dropna=False
        )["dutiablevaluephp"]
        .agg(
            record_count="size",
            total_dutiablevaluephp="sum"
        )
        .reset_index()
    )

    # Group by country of origin and quarter.
    grouped_two = (
        df.groupby(
            GROUPING_COLUMNS,
            dropna=False
        )["dutiablevaluephp"]
        .agg(
            record_count="size",
            total_dutiablevaluephp="sum"
        )
        .reset_index()
    )

    # Create a pivot table using country and quarter.
    pivot = pd.pivot_table(
        df,
        index=GROUPING_COLUMNS[0],
        columns=GROUPING_COLUMNS[1],
        values="dutiablevaluephp",
        aggfunc="sum",
        fill_value=0
    ).reset_index()

    # Get the top 10 records by dutiable value.
    top10 = (
        df[
            [
                "countryorigin_iso3",
                "tq",
                "dutiablevaluephp",
                "dutiablevalue_million",
                "value_category"
            ]
        ]
        .sort_values(
            by="dutiablevaluephp",
            ascending=False
        )
        .head(10)
    )

    # Save the summary tables.
    grouped.to_csv(
        f"{output_folder}/grouped.csv",
        index=False
    )

    grouped_two.to_csv(
        f"{output_folder}/grouped_two.csv",
        index=False
    )

    pivot.to_csv(
        f"{output_folder}/pivot.csv",
        index=False
    )

    top10.to_csv(
        f"{output_folder}/top10.csv",
        index=False
    )

    return {
        "grouped": grouped,
        "grouped_two": grouped_two,
        "pivot": pivot,
        "top10": top10
    }
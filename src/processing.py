import pandas as pd

from config import FILTER_QUARTER, FILTER_MIN_VALUE


def filter_and_transform_data(
    df: pd.DataFrame,
    quarter: str = FILTER_QUARTER,
    minimum_value: float = FILTER_MIN_VALUE
) -> pd.DataFrame:
    """
    Filter the Customs 2015 dataset and create derived columns.

    Parameters:
        df: Original Customs 2015 DataFrame.
        quarter: Quarter to keep from the tq column.
        minimum_value: Minimum dutiable value in PHP.

    Returns:
        A filtered and transformed DataFrame.
    """
    
    filtered_df = df.loc[
        (df["tq"] == quarter) &
        (df["dutiablevaluephp"] >= minimum_value)
    ].copy()

    filtered_df = filtered_df.sort_values(
        by="dutiablevaluephp",
        ascending=False
    )

    filtered_df["dutiablevalue_million"] = (
        filtered_df["dutiablevaluephp"] / 1_000_000
    )

    filtered_df["value_category"] = filtered_df[
        "dutiablevaluephp"
    ].apply(
        lambda value: "High"
        if value >= 10_000_000
        else "Standard"
    )

    filtered_df["countryorigin_iso3"] = filtered_df[
        "countryorigin_iso3"
    ].fillna("Missing")

    return filtered_df
import os

import pandas as pd


class DataValidator:
    """
    Validate the results of the Customs 2015 data processing program.
    """

    def __init__(
        self,
        raw_df: pd.DataFrame,
        filtered_df: pd.DataFrame,
        summaries: dict
    ):
        """
        Initialize the validator with the original data,
        filtered data, and summary tables.
        """

        self.raw_df = raw_df
        self.filtered_df = filtered_df
        self.summaries = summaries

    def check_raw_row_count(self) -> dict:
        """Check the number of rows in the original dataset."""

        expected = 2_236_612
        actual = len(self.raw_df)

        return {
            "check": "Raw row count",
            "expected": expected,
            "actual": actual,
            "tolerance": 0,
            "pass": actual == expected
        }

    def check_raw_total(self) -> dict:
        """Check the total dutiable value of the original dataset."""

        expected = 3_587_267_375_257
        actual = self.raw_df["dutiablevaluephp"].sum()

        return {
            "check": "Raw dutiable value total",
            "expected": expected,
            "actual": actual,
            "tolerance": 1.00,
            "pass": abs(actual - expected) <= 1.00
        }

    def check_filtered_rows(self) -> dict:
        """Check that the filtered records match the selected count."""

        expected = 127_272
        actual = len(self.filtered_df)

        return {
            "check": "Filtered row count",
            "expected": expected,
            "actual": actual,
            "tolerance": 0,
            "pass": actual == expected
        }

    def check_grouped_rows(self) -> dict:
        """Check that grouped record counts equal filtered records."""

        expected = len(self.filtered_df)

        actual = self.summaries["grouped"]["record_count"].sum()

        return {
            "check": "Grouped record count",
            "expected": expected,
            "actual": actual,
            "tolerance": 0,
            "pass": actual == expected
        }

    def check_grouped_total(self) -> dict:
        """Check that grouped totals equal the filtered total."""

        expected = self.filtered_df[
            "dutiablevaluephp"
        ].sum()

        actual = self.summaries["grouped"][
            "total_dutiablevaluephp"
        ].sum()

        return {
            "check": "Grouped dutiable value total",
            "expected": expected,
            "actual": actual,
            "tolerance": 1.00,
            "pass": abs(actual - expected) <= 1.00
        }

    def check_pivot_total(self) -> dict:
        """Check that the pivot total equals the filtered total."""

        expected = self.filtered_df[
            "dutiablevaluephp"
        ].sum()

        pivot = self.summaries["pivot"]

        actual = pivot.select_dtypes(
            include="number"
        ).sum().sum()

        return {
            "check": "Pivot dutiable value total",
            "expected": expected,
            "actual": actual,
            "tolerance": 1.00,
            "pass": abs(actual - expected) <= 1.00
        }

    def run_all_checks(self) -> pd.DataFrame:
        """Run all validation checks and return a DataFrame."""

        checks = [
            self.check_raw_row_count(),
            self.check_raw_total(),
            self.check_filtered_rows(),
            self.check_grouped_rows(),
            self.check_grouped_total(),
            self.check_pivot_total()
        ]

        return pd.DataFrame(checks)


def save_validation(
    validation_df: pd.DataFrame,
    output_folder: str = "output"
) -> None:
    """
    Save validation results to validation.csv.
    """

    os.makedirs(output_folder, exist_ok=True)

    validation_df.to_csv(
        f"{output_folder}/validation.csv",
        index=False
    )
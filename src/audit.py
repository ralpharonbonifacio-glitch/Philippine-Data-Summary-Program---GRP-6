import os

import pandas as pd


def create_audit_log(
    raw_df: pd.DataFrame,
    filtered_df: pd.DataFrame,
    output_folder: str = "output"
) -> pd.DataFrame:
    """
    Create an audit log showing the major processing steps.
    """

    audit_records = [
        {
            "step": 1,
            "operation": "Load dataset",
            "rule": "Read Customs 2015 CSV file",
            "rows_before": 0,
            "rows_after": len(raw_df)
        },
        {
            "step": 2,
            "operation": "Filter records",
            "rule": "tq == 2015q4 AND dutiablevaluephp >= 1,000,000",
            "rows_before": len(raw_df),
            "rows_after": len(filtered_df)
        },
        {
            "step": 3,
            "operation": "Create derived columns",
            "rule": "Create dutiablevalue_million and value_category",
            "rows_before": len(filtered_df),
            "rows_after": len(filtered_df)
        },
        {
            "step": 4,
            "operation": "Create summary tables",
            "rule": "Group and aggregate filtered records",
            "rows_before": len(filtered_df),
            "rows_after": len(filtered_df)
        },
        {
            "step": 5,
            "operation": "Create plots",
            "rule": "Generate bar plot and heatmap from filtered records",
            "rows_before": len(filtered_df),
            "rows_after": len(filtered_df)
        }
    ]

    audit_df = pd.DataFrame(audit_records)

    os.makedirs(output_folder, exist_ok=True)

    audit_df.to_csv(
        f"{output_folder}/audit_log.csv",
        index=False
    )

    return audit_df
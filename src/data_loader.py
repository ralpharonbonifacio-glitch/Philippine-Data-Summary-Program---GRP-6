import os
import pandas as pd

from config import INPUT_FILE, REQUIRED_COLUMNS


def load_data(file_path: str = INPUT_FILE) -> pd.DataFrame:
    """
    Load the Customs 2015 CSV dataset and check required columns.

    Parameters:
        file_path: Path to the CSV dataset.

    Returns:
        A pandas DataFrame containing the dataset.

    Raises:
        FileNotFoundError: If the dataset file does not exist.
        ValueError: If required columns are missing.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Input file not found: {file_path}"
        )

    print(f"Loading dataset: {file_path}")

    df = pd.read_csv(
        file_path,
        encoding="latin1"
    )

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print(f"Dataset loaded successfully: {len(df):,} rows")

    return df
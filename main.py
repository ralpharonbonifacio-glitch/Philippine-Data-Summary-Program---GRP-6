from src.data_loader import load_data
from src.processing import filter_and_transform_data
from src.summary import create_summary_tables


def main():
    """Load, filter, and transform the Customs 2015 dataset."""

    try:
    
        df = load_data()

        print("\nFirst 5 rows of original dataset:")
        print(df.head())

        print("\nOriginal dataset shape:")
        print(df.shape)

        
        filtered_df = filter_and_transform_data(df)

        print("\nFiltered dataset shape:")
        print(filtered_df.shape)

        print("\nFirst 5 filtered records:")
        print(
            filtered_df[
                [
                    "countryorigin_iso3",
                    "tq",
                    "dutiablevaluephp",
                    "dutiablevalue_million",
                    "value_category"
                ]
            ].head()
        )

        summaries = create_summary_tables(filtered_df)

        print("\nSummary tables created successfully.")

        print("\nGrouped table:")
        print(summaries["grouped"].head())

        print("\nGrouped two-column table:")
        print(summaries["grouped_two"].head())

        print("\nPivot table:")
        print(summaries["pivot"].head())

        print("\nTop 10:")
        print(summaries["top10"])

    except FileNotFoundError as error:
        print(f"ERROR: {error}")

    except ValueError as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()

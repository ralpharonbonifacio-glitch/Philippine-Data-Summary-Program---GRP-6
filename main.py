from src.data_loader import load_data
from src.processing import filter_and_transform_data
from src.summary import create_summary_tables
from src.plotting import (
    compare_loop_vectorized,
    create_bar_plot,
    create_heatmap
)
from src.validation import DataValidator, save_validation
from src.audit import create_audit_log

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

        comparison = compare_loop_vectorized(filtered_df)

        print("\nLoop vs Vectorized:")
        print(
            "Results equal:",
            comparison["results_equal"]
        )
        print(
            "Loop median time:",
            comparison["loop_median_time"]
        )
        print(
            "Vectorized median time:",
            comparison["vectorized_median_time"]
        )
        print(
            "High-value records in sample:",
            comparison["high_value_count"]
        )

        create_bar_plot(filtered_df)
        create_heatmap(filtered_df)

        print("\nPlots created successfully.")

        validator = DataValidator(df, filtered_df, summaries)

        validation_results = validator.run_all_checks()

        save_validation(validation_results)

        print("\nValidation results:")
        print(validation_results)

        # Create audit log.
        audit_results = create_audit_log(df, filtered_df)

        print("\nAudit log created successfully.")
        print(audit_results)

    except FileNotFoundError as error:
        print(f"ERROR: {error}")

    except ValueError as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()

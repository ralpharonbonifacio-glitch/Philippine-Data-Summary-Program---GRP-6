from src.data_loader import load_data

def main():
    """Run the initial Customs 2015 dataset loading test."""

    try:
        df = load_data()

        print("\nFirst 5 rows:")
        print(df.head())

        print("\nDataset shape:")
        print(df.shape)

        print("\nRequired columns:")
        print([
            "countryorigin_iso3",
            "tq",
            "dutiablevaluephp"
        ])

    except FileNotFoundError as error:
        print(f"ERROR: {error}")

    except ValueError as error:
        print(f"ERROR: {error}")

if __name__ == "__main__":
    main()


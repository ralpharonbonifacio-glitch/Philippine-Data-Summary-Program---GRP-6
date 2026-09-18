# Configuration settings for the Customs 2015 dataset

INPUT_FILE = "2015.csv"

FILTER_QUARTER = "2015q4"
FILTER_MIN_VALUE = 1_000_000

GROUPING_COLUMNS = [
    "countryorigin_iso3",
    "tq"
]

OUTPUT_FOLDER = "output"

REQUIRED_COLUMNS = [
    "countryorigin_iso3",
    "tq",
    "dutiablevaluephp"
]
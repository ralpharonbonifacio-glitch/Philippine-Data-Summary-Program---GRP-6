# Philippine Data Summary Program

## Project Description

This project analyzes the Philippine Customs 2015 dataset using Python and pandas.

The program loads the dataset, filters the records, transforms selected values,
creates summary tables, generates visualizations, and performs validation checks.

## Data Source

Dataset: Philippine Customs 2015 Dataset

The raw `2015.csv` dataset is not included in the repository because of its large
file size. It must be placed in the project root directory before running the program.

## Filtering Rules

The program selects records where:

- Quarter (`tq`) is `2015q4`
- Dutiable value (`dutiablevaluephp`) is greater than or equal to PHP 1,000,000

The resulting filtered dataset contains 127,272 records.

## Data Transformations

The program creates derived fields including:

- `dutiablevalue_million`
- `value_category`

## Requirements

Python 3.14 or compatible Python version

Install the required packages:

    pip install -r requirements.txt

## How to Run

Place `2015.csv` in the project root directory.

Then run:

    python main.py

## Outputs

The program produces:

- grouped.csv
- grouped_two.csv
- pivot.csv
- top10.csv
- bar.png
- heatmap.png
- validation.csv
- audit_log.csv

## Analysis Notebook

The project includes:

- `analysis.ipynb`
- `analysis.html`

The notebook demonstrates the use of the imported project modules and presents
the analysis results.
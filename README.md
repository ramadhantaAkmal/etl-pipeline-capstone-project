# Capstone 1 - ETL Pipeline Capstone Project

## Overview

This project, completed by Mohamad Akmal Ramadhanta as part of the Purwadhika School Data Engineering curriculum, focuses on programming fundamental. The datasets, sourced from Kaggle, consist of multiple CSV files that are cleaned, transformed, and merged into a single CSV file using Python and the pandas library. The resulting dataset is structured and ready for further analysis.

## Technology Used
- **Python**
- **Pandas**

## Contents
- **Abstract**: Overview of the project and its objectives.
- **Task Description**: Details of the ETL process and goals.
- **Data Extraction Process**: Available in the [Jupyter Notebook](https://github.com/ramadhantaAkmal/etl-pipeline-capstone-project/blob/main/Extraction.ipynb).
- **Data Transformation Process**: Available in the [Jupyter Notebook](https://github.com/ramadhantaAkmal/etl-pipeline-capstone-project/blob/main/Transformation.ipynb).
- **Summary**: Key findings and outcomes.

## Abstract

This project demonstrates the creation of an ETL pipeline to process multiple CSV datasets from Kaggle. Using Python and pandas, the data is cleaned, transformed, and consolidated into a single, analysis-ready CSV file. The exercise was conducted as part of the Purwadhika School Data Engineering curriculum.

## Setup Instructions

### Prerequisites
- Download your Kaggle API key (`kaggle.json`) from [Kaggle](https://www.kaggle.com).
- Place the `kaggle.json` file in the appropriate directory:
  - **Linux/macOS**: `~/.kaggle/kaggle.json`
  - **Windows**: `C:\Users\<YourUsername>\.kaggle\kaggle.json`
- Ensure the `EXTRACT_PATH` and `LOAD_PATH` variables are configured in `settings.py` located in the `config` directory.

### Recommended Environment
- **Linux** or **macOS** is recommended for running the program.

### Running the Program
- **Linux/macOS**:
  1. Navigate to the project directory.
  2. Run the shell script:
     ```bash
     ./run-etl-script.sh
     ```
- **Windows**:
  1. Navigate to the project directory.
  2. Run the main Python script:
     ```bash
     python main.py
     ```

## Notes
- Ensure all dependencies (Python, pandas, and others listed in the project) are installed.
- The data transformation process is documented in the linked Jupyter Notebook.

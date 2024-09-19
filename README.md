# Drift Monitoring with Evidently

This project utilizes [Evidently AI](https://evidentlyai.com/) for comprehensive machine learning model monitoring, focusing on data drift detection and data quality monitoring. With Evidently's tools, you can ensure timely issue detection, allowing for the maintenance of high-performing and reliable ML models.

## Project Overview

This repository showcases how Evidently can be used for monitoring ML models, particularly focusing on:

1. **Data Drift Detection**: Compare different versions of your dataset (reference and current) to detect if the distribution of data changes over time.
2. **Data Quality Monitoring**: Use Evidently's Test Suites for systematic checks across multiple dimensions of data quality.
3. **Reporting & Visualization**: Generate interactive reports and visualize them within the Evidently UI.

## Features

- **Data Drift Detection**: Compares historical (reference) and current data to check for drift using Evidently's metrics.
- **Data Quality Test Suites**: Perform automated quality checks on your data, such as mean value checks and handling missing data.
- **Seamless Integration**: Pushes results and reports to the Evidently workspace for ongoing model monitoring.

## Setup & Installation

### Requirements

- Python 3.x
- pip or conda for package management
- Docker (optional for Docker-based setup)

### Install Dependencies

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/arifhaidari/drift_monitoring_evidently.git
cd drift_monitoring_evidently

# Using pip
pip install -r requirements.txt

# Or, if using conda
conda env create -f environment.yml
conda activate drift-monitoring-env
```

### Running the Project

1. **Generate Drift and Data Quality Reports**:

   To run the monitoring scripts and generate drift and quality reports:

   ```bash
   python data_monitoring_with_report.py
   ```

2. **Run Evidently UI**:

   To visualize the reports and track monitoring data, start the Evidently UI:

   ```bash
   evidently ui --workspace ./datascientest-workspace/
   ```

3. **View Reports**:

   Navigate to [http://localhost:8000](http://localhost:8000) in your browser to interact with the reports in the Evidently dashboard.

## Project Structure

- `data_monitoring_with_report.py`: Main script to run data drift and data quality monitoring.
- `simple_regression_model_monitoring.py`: Monitors a simple regression model using Evidently.
- `classification_model_monitoring.py`: Monitors a classification model.
- `requirements.txt`: Contains Python dependencies.
- `code_snippets.py`: extra functionalities.
- `column_mapping.py`: code snippets.
- `Dockerfile`: for container based projects.
- `notebooks`: for step by step executions.
- `artifacts`: for execution files.
- `docker-compose.yml`: for container based projects.
- `README.md`: This file.

## License

This project was developed under the supervision and instruction of the DataScientest Bootcamp.

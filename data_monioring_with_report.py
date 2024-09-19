import pandas as pd
import numpy as np
import zipfile
from sklearn import ensemble
from sklearn import datasets
from evidently.report import Report
from evidently.metric_preset import DataQualityPreset
from evidently.ui.workspace import Workspace
from evidently.test_suite import TestSuite
from evidently.test_preset import DataQualityTestPreset
from evidently.tests import TestColumnValueMean
from evidently.metrics import (DatasetSummaryMetric, 
                               DatasetCorrelationsMetric,
                               DatasetMissingValuesMetric)
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data_from_zip(zip_path, sample_size):
    """
    Load a sample of data from a ZIP file and return as a DataFrame.
    """
    np.random.seed(42)

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        # Get the first file in the ZIP archive
        file_name = zip_file.namelist()[0]
        # Read a sample of the file as a DataFrame
        df = pd.read_csv(zip_file.open(file_name), index_col=0).sample(n=sample_size, random_state=42)
    return df

def split_data_by_month(df, month=6):
    """
    Split data into reference and current datasets based on month.
    """
    # Filter data based on the month
    month_range = df['Month'] >= month
    ref_data = df[~month_range]
    curr_data = df[month_range]
    return ref_data, curr_data

def create_and_run_test_suite(ref_data, curr_data, SAVE_FILE = False):
    """
    Create and run a test suite for dataset summary.
    """
    # Define tests for dataset summary
    test_suite = TestSuite(tests=[DataQualityTestPreset(),
                                  TestColumnValueMean(column_name='ArrDelay')])
    # Run the test suite
    test_suite.run(reference_data=ref_data, current_data=curr_data)

    # save the report as HTML
    if SAVE_FILE:
        test_suite.save_html("data_drift_suite.html")
    return test_suite

def create_and_run_report(reference_data, current_data):
    """
    Generates a classification report using Evidently.
    """
    # Create a Report instance for classification with a set of predefined metrics
    report = Report(metrics=[
        DatasetSummaryMetric(),
        DatasetCorrelationsMetric(),
        DatasetMissingValuesMetric(),
    ])

    # Generate the report using reference_data and current_data
    report.run(reference_data=reference_data, current_data=current_data)

    return report

def add_report_and_test_suite_to_workspace(workspace, project_name, 
                                           project_description, 
                                           report, test_suite):
    """
    Adds a report and test suite to an existing or new project in a workspace.
    """
    # Check if project already exists
    project = None
    for p in workspace.list_projects():
        if p.name == project_name:
            project = p
            break

    # Create a new project if it doesn't exist
    if project is None:
        project = workspace.create_project(project_name)
        project.description = project_description

    # Add report to the project
    workspace.add_report(project.id, report)
    workspace.add_report(project.id, test_suite)
    print(f"New items added to project {project_name}")

if __name__ == "__main__":

    # Define constants for workspace and project details
    WORKSPACE_NAME = "datascientest-workspace"
    PROJECT_NAME = "data_monitoring_test_suite_and_report"
    PROJECT_DESCRIPTION = "Evidently Dashboards"

    # Path to the ZIP file
    zip_path = './data/Delay_data.zip'

    # Define sample size
    sample_size = 10000

    logging.info('Loading data from ZIP file...')
    df = load_data_from_zip(zip_path, sample_size)
    logging.info('Data loaded successfully.')

    logging.info('Splitting data by month...')
    ref_data, curr_data = split_data_by_month(df)
    logging.info('Data split completed.')

    logging.info('Creating and running test suite...')
    test_suite = create_and_run_test_suite(ref_data, curr_data)
    logging.info('Test suite completed.')

    logging.info('Creating and running report...')
    report = create_and_run_report(ref_data, curr_data)
    logging.info('Report generated successfully.')

    logging.info('Adding report to workspace...')
    workspace = Workspace(WORKSPACE_NAME)
    add_report_and_test_suite_to_workspace(workspace, PROJECT_NAME, 
                                           PROJECT_DESCRIPTION, report, test_suite)
    logging.info('Report added to workspace.')

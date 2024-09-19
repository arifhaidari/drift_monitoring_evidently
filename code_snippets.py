from evidently.test_preset import NoTargetPerformanceTestPreset

# Building the test suite
no_target_performance_suite = TestSuite(tests=[NoTargetPerformanceTestPreset()])

# Running the test suite
# We can split the datasets into different batches, of same batch size, and try test suite with different batch data, to find whether the model performance is declining or not with different batches
no_target_performance_suite.run(reference_data=processed_data_reference, current_data=processed_data_prod_simulation[2*batch_size:3*batch_size])


# =========

from evidently.test_suite import TestSuite
from evidently.test_preset import DataDriftTestPreset

# Create a test suite
data_drift_suite = TestSuite(tests=[
    DataDriftTestPreset(),
])

# Run the suite
data_drift_suite.run(reference_data=ref_data, current_data=current_data)

# Check results
if data_drift_suite.as_dict()['summary']['all_passed']:
    print("All data quality checks passed!")
else:
    print("Some data quality issues detected. Check the report for details.")

# =============
# Tests suites with specific metrics
# It is also possible to use specific metrics to carry out the test suite (see the code below as an example).

# build the test suites
custom_performance_suite = TestSuite(tests=[
    TestShareOfMissingValues(eq=0),
    TestPrecisionScore(gt=0.5),
    TestRecallScore(gt=0.3),
    TestAccuracyScore(gte=0.75),
])

# run the test suites
custom_performance_suite.run(reference_data=processed_reference, current_data=processed_prod_simulation[:batch_size])

# to display results in a jupyter notebook
custom_performance_suite.show(mode='inline')


# ===========
# Report with specific metrics
# It is also possible to get the data drift report for specific features, using the ColumnDriftMetric metric:

data_drift_column_report = Report(metrics=[
    ColumnDriftMetric(column_name='ArrDelay'),
    ColumnDriftMetric(column_name='ArrDelay', stattest='psi')
])
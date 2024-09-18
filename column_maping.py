# Import the necessary modules
from evidently.pipeline.column_mapping import ColumnMapping

# Create a new instance of the ColumnMapping class
column_mapping = ColumnMapping()

# Set the target column name
column_mapping.target = 'target'

# Set the prediction column name
column_mapping.prediction = 'prediction'

# Set the list of numerical feature column names
numerical_features = ['numerical_feature_1', 'numerical_feature_2']
column_mapping.numerical_features = numerical_features

# Set the list of categorical feature column names
categorical_features = ['categorical_feature_1', 'categorical_feature_2']
column_mapping.categorical_features = categorical_features

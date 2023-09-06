
# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from azureml.core import Workspace, Dataset

subscription_id = '9a4c4ce5-6506-4fae-9fdd-051e7d71f1d5'
resource_group = 'mlops-aug-batch'
workspace_name = 'intellipaat-mlops'

workspace = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(workspace, name='iris')
df = dataset.to_pandas_dataframe()





def test_columns():
    print(df.columns.to_list())
    assert df.columns.to_list() ==['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
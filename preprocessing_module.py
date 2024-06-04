import kfp
from kfp.dsl import Input, Output, Dataset, component
import os

@component
def preprocessing(
    raw_data: Input[Dataset],
    preprocessed_df: Output[Dataset]
):
    import subprocess
    subprocess.run(['pip', 'install', 'pandas'], check=True)
    import pandas as pd

    black_friday_df = pd.read_csv(raw_data.path)
    black_friday_df['Product_Category_2'].fillna(0, inplace=True)
    black_friday_df['Product_Category_3'].fillna(0, inplace=True)
    black_friday_df.drop(['User_ID', 'Product_ID'], axis=1, inplace=True)
    black_friday_df.to_csv(preprocessed_df.path, index=False)

@component
def feature_engineering(
    preprocessed_df: Input[Dataset],
    engineered_test_df: Output[Dataset]
):
    import subprocess
    subprocess.run(['pip', 'install', 'pandas', 'google-cloud-storage'], check=True)
    import pandas as pd

    black_friday_test_df = pd.read_csv(preprocessed_df.path)
    black_friday_test_df['Gender'] = black_friday_test_df['Gender'].replace({'F': 0, 'M': 1}).astype('int64')

    age_mapping = {'0-17': 0, '18-25': 1, '26-35': 2, '36-45': 3, '46-50': 4, '51-55': 5, '55+': 6}
    black_friday_test_df['Age'] = black_friday_test_df['Age'].map(age_mapping).astype('int64')

    city_category_mapping = {'A': 0, 'B': 1, 'C': 2}
    black_friday_test_df['City_Category'] = black_friday_test_df['City_Category'].replace(city_category_mapping).astype('int64')
    black_friday_test_df['Stay_In_Current_City_Years'] = black_friday_test_df['Stay_In_Current_City_Years'].str.replace('+', '').astype('int64')

    columns_to_int = ['Occupation', 'Marital_Status', 'Product_Category_1', 'Product_Category_2', 'Product_Category_3']
    for column in columns_to_int:
        black_friday_test_df[column] = black_friday_test_df[column].astype('int64')
    
    black_friday_test_df.to_csv(engineered_test_df.path, index=False)

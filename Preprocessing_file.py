import kfp
from kfp.dsl import (component, Input, Output, Dataset, Model)

@component
def preprocessing(
    raw_data: Input[Dataset],
    preprocessed_data: Output[Dataset]
):
    import subprocess
    subprocess.run(['pip', 'install', 'pandas'], check=True)
    
    """
    Component for data preprocessing, including dropping User_ID, Product_ID, 
    and Product_category_3.
    """
    
    import pandas as pd
    
    # Load data
    black_friday_df = pd.read_csv(raw_data.path)
    
    # Handle missing values before encoding
    black_friday_df['Product_Category_2'] = black_friday_df['Product_Category_2'].fillna(0)
       
    # Drop columns not needed for demographic analysis
    black_friday_df.drop(['User_ID', 'Product_ID', 'Product_Category_3'], axis=1, inplace=True)
    
    # Save preprocessed data to a CSV file
    black_friday_df.to_csv(preprocessed_data.path, index=False)

@component
def feature_engineering(
    preprocessed_data: Input[Dataset],
    engineered_data: Output[Dataset]
):
    import subprocess
    subprocess.run(['pip', 'install', 'pandas', 'scikit-learn'], check=True)
  
    """
    Component for feature engineering using encoding strategies.
    """
    
    import pandas as pd
    
    # Load data
    black_friday_df = pd.read_csv(preprocessed_data.path)
    
    # Encode categorical columns
    black_friday_df['Gender'] = black_friday_df['Gender'].replace({'F': 0, 'M': 1}).astype('int64')
    
    age_mapping = {'0-17': 0, '18-25': 1, '26-35': 2, '36-45': 3, '46-50': 4, '51-55': 5, '55+': 6}
    black_friday_df['Age'] = black_friday_df['Age'].map(age_mapping).astype('int64')
    
    city_category_mapping = {'A': 0, 'B': 1, 'C': 2}
    black_friday_df['City_Category'] = black_friday_df['City_Category'].replace(city_category_mapping).astype('int64')
    
    # Remove '+' sign from the 'Stay_In_Current_City_Years' and convert to int64
    black_friday_df['Stay_In_Current_City_Years'] = black_friday_df['Stay_In_Current_City_Years'].str.replace('+', '').astype('int64')

    # Convert relevant columns to int64
    columns_to_int = ['Occupation', 'Marital_Status', 'Product_Category_1', 'Product_Category_2']
    for column in columns_to_int:
        black_friday_df[column] = black_friday_df[column].astype('int64')
    
    # Save engineered data
    black_friday_df.to_csv(engineered_data.path, index=False)

"""
Load, preprocess, prepare, and save the Titanic dataset.
"""

import pandas as pd
import os
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder


def load_data(data_dir, file_name):
    """
    Load the Titanic dataset from a CSV file.
    
    Returns:
        DataFrame: The loaded Titanic dataset.
    """
    return pd.read_csv(os.path.join(data_dir,file_name),index_col=0)
       
def clean_data(df):
    """
    clean the Titanic dataset.
    
    Args:
        df (DataFrame): The Titanic dataset.
        
    Returns:
        DataFrame: The preprocessed Titanic dataset.
    """
    df.drop(columns=['Name', 'Ticket', 'Cabin'], inplace=True)

    imputer = SimpleImputer().set_output(transform="pandas")
    
    imputer.fit(df[['Age']])

    df[['Age']] = imputer.transform(df[['Age']])
    df["Embarked"].fillna("S", inplace=True)    
    df.dropna(subset=['Fare'], inplace=True)
    
        

def prepare_data(df:pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]: 
    """
    Prepare the Titanic dataset for training.
    
    Args:
        df (DataFrame): The preprocessed Titanic dataset.
        
    Returns:
        tuple: A tuple containing [X,y] the features DataFrame and the target Series.
    """
    

    numeric_features = ['Age', 'Fare']

    scaler = StandardScaler()
    df_scaled = df.copy()
    categorical_features =  ["Sex", "Embarked"]
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore', drop='first').set_output(transform="pandas")
        
    
    df_scaled[numeric_features] = scaler.fit_transform(df[numeric_features])    
    df_scaled[numeric_features] = scaler.transform(df[numeric_features])
    
    df_encoded = encoder.fit_transform(df[categorical_features])
    df_encoded = encoder.transform(df[categorical_features])

    df_final = pd.concat([df_scaled, df_encoded], axis=1).drop(columns=['Sex', 'Embarked'])
    
    X_df = df_final.drop(columns=['Survived'])
    y_df = df_final['Survived']

    return X_df,y_df
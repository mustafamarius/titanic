"""
Load, preprocess, prepare, and save the Titanic dataset.
"""

import pandas as pd
import os

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
    pass

def prepare_data(df:pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]: 
    """
    Prepare the Titanic dataset for training.
    
    Args:
        df (DataFrame): The preprocessed Titanic dataset.
        
    Returns:
        tuple: A tuple containing [X,y] the features DataFrame and the target Series.
    """
    pass
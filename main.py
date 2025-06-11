"""

"""
import pandas as pd
from titanic.data import load_data,clean_data,prepare_data
from titanic.registry import save_model
from titanic.train import train_model, evaluate_model, optimize_model

DATA_DIR = "data/"

train_df = load_data(DATA_DIR, "train.csv")

test_df_missing_target  = load_data(DATA_DIR, "test.csv")
target_test_df          = load_data(DATA_DIR, "gender_submission.csv")
test_df = pd.merge(  test_df_missing_target
                   , target_test_df
                   , left_index=True
                   , right_index=True
                   , how='left'
                   , suffixes=('', '_target')).copy()

print (test_df.head())

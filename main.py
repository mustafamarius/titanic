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



# clean data

clean_data(train_df)
clean_data(test_df)

# print (train_df.head())
# print (test_df.head())


x_train , y_train =  prepare_data(train_df)
x_test, y_test = prepare_data(test_df)

print(x_train.head())
print (y_train)

print(x_test.head())
print (y_test.head())

lin_model = train_model(x_train , y_train)
print(evaluate_model(lin_model, x_test, y_test))

best_model = optimize_model(lin_model, x_train, y_train)
print("best score:")
print(evaluate_model(best_model, x_test, y_test))






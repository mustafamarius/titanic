import os

DATA_FOLDER= "data"
MODEL_FOLDER = os.environ.get("MODEL_FOLDER"
                              , "models")
CAT_FEATURES = ["Embarked", "Sex"]
NUMERIC_FEATURES = ["Age", "Fare"]

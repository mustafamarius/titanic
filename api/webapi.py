from fastapi import FastAPI
from loguru import logger
from titanic.data import prepare_data, clean_data
from titanic.registry import load_model
import pandas as pd

my_api = FastAPI(
    title="Web API",
    description="API for the web application")


@my_api.get("/")
def read_root():
    """
    Root endpoint of the Web API.
    """
    return {"message": "Welcome to the Web API!"}

@my_api.get("/love")
def send_love(amount: int = 1):
    logger.info(f"{amount=} , type : {type(amount)}")
    return {"love": amount*"❤️"}


@my_api.get("/predict")
def survive_pred(PassengerId : str = "1",
                 Pclass: int = 1,
                 Name: str = "John Doe",
                 Sex: str = "male",
                 Age: float = 30,
                 SibSp: int = 0,
                 Parch: int = 0,
                 Ticket: str = "A/5 21171",
                 Fare: float = 7.25,
                 Cabin: str = "C85",
                 Embarked: str = "S"):
    logger.info(f"Predicting survival for {Name}")
    model = load_model("best_model.pkl")
    data = pd.DataFrame({
        "PassengerId": [PassengerId],
        "Pclass": [Pclass],
        "Name": [Name],
        "Sex": [Sex],
        "Age": [Age],
        "SibSp": [SibSp],
        "Parch": [Parch],
        "Ticket": [Ticket],
        "Fare": [Fare],
        "Cabin": [Cabin],
        "Embarked": [Embarked]
    })
    X , _ = prepare_data(data,fit=False, survive=False)
    logger.debug(f"Prepared data for prediction: {X}")
    prediction = model.predict(X)
    return {"survived": bool(prediction[0])}
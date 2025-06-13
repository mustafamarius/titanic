"""

"""

from titanic.data import load_data,clean_data,prepare_data
from titanic.registry import save_model
from titanic.train import train_model, evaluate_model


def train():
    data= load_data(train=True)
    data = clean_data(data)
    X, y = prepare_data(data, fit=True, survive=True)
    model = train_model(X, y)
    save_model(model, "best_model.pkl")
    
    

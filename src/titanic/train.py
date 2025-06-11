"""
Train the Titanic model.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

def train_model(x_train, y_train):
    """ 
    Initiate the model and train it on the Titanic dataset.""
    """
    lin = LogisticRegression(max_iter=1000, random_state=42)

    lin.fit(x_train, y_train)
    return lin
#

def evaluate_model(lin_model, x_test, y_test):
    return lin_model.score(x_test, y_test)

def optimize_model(lin_model, x_train, y_train):

    param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear', 'saga']
}
    grid_search = GridSearchCV(lin_model, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
    grid_search.fit(x_train, y_train)
    best_lin = grid_search.best_estimator_
    return best_lin
    
   


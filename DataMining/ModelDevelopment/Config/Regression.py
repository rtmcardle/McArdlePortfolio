from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import BaggingRegressor
import numpy as np


estimator_list = [LinearRegression(),
                       MLPRegressor(max_iter=50000),
                       BaggingRegressor(),
                      ]

params_list = [{'fit_intercept':[False,True],
                    'normalize':[False,True],
                    },#LinearRegression

                    {'activation':['logistic','tanh','relu'],
                    'solver': ['lbfgs','sgd','adam'],
                    'alpha': [0.5e-4,1.0e-4,1.5e-4],
                    'learning_rate': ['constant','adaptive'],
                    },#MLPRegressor

                    {'base_estimator':[LinearRegression()],
                    'n_estimators': np.arange(5,26,5),
                    'max_samples': np.arange(0.5,1.001,0.1),
                    'max_features':np.arange(0.5,1.001,0.1),
                    }, #BaggingRegressor
                    ]
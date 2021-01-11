from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.ensemble import RandomForestClassifier
import numpy as np

estimator_list = [LogisticRegression(),
                 Perceptron(),
                 RandomForestClassifier(),
                 ]

params_list = [{'penalty':['l1','l2','elasticnet','none'],
                'C':[0.5,1.0,1.5],
                'class_weight':[None,'balanced'],
                'solver':['liblinear','newton-cg','lbfgs','sag','saga'],
                }, #LogisticRegression

                {'penalty':['l1','l2','elasticnet'],
                'alpha':[0.5e-4,1.0e-4,1.5e-4],
                'class_weight':[None,'balanced'],
                'shuffle':[False,True],
                }, #Perceptron

                {'n_estimators':np.arange(25,201,25),
                'criterion':['gini','entropy'],
                'min_samples_split':np.arange(2,23,5),
                'max_features':['sqrt','log2',None],
                'class_weight':[None,'balanced','balanced_subsample'],
                }, #RandomForest
            ]
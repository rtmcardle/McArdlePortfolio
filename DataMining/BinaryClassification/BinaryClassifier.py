
###############################################################
##  Ryan McArdle
##  29 October, 2020
###############################################################



from sklearn.linear_model import LogisticRegression, RidgeClassifier, Perceptron, LinearRegression
from sklearn.model_selection import GridSearchCV, train_test_split, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.feature_selection import RFECV
from sklearn.preprocessing import scale
from joblib import dump,load
import pandas as pd
import numpy as np
import psutil
import time
import os


class ModelDevelopment():
    """
    A class capable of exploring the breast_cancer and solar 
    data sets to find the best classifier and regressor 
    respectively.
    """

    def __init__(self):
        self.best_score = 0.0
        self.best_model = None
        self.problem_path = None


    def explore_dataset(self,problem):
        """
        The main method that should be called with the desired
        problem to solve. Defines the lists of estimators and 
        their associated parameters for the gridsearch.

        :param problem: the problem to be solved; 'cancer' or 
            'solar'
        """

        self.problem = problem
        if problem == 'cancer':
            self.file = './HW4/model_dev_data/breast_cancer.csv'
            self.estimator_list = [LogisticRegression(),
                                   Perceptron(),
                                   RandomForestClassifier(),
                                   ]
            self.params_list = [{'penalty':['l1','l2','elasticnet','none'],
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

        #elif problem == 'solar':
        #    self.file = './HW4/model_dev_data/solar.csv'
        #    self.estimator_list = [LinearRegression(),
        #                           MLPRegressor(max_iter=50000),
        #                           BaggingRegressor(),
        #                           ]

        #    self.params_list = [{'fit_intercept':[False,True],
        #                         'normalize':[False,True],
        #                         },#LinearRegression
        #                        {'activation':['logistic','tanh','relu'],
        #                         'solver': ['lbfgs','sgd','adam'],
        #                         'alpha': [0.5e-4,1.0e-4,1.5e-4],
        #                         'learning_rate': ['constant','adaptive'],
        #                         },#MLPRegressor
        #                        {'base_estimator':[LinearRegression()],
        #                         'n_estimators': np.arange(5,26,5),
        #                         'max_samples': np.arange(0.5,1.001,0.1),
        #                         'max_features':np.arange(0.5,1.001,0.1),
        #                         }, #BaggingRegressor
        #                        ]


        self.test_size_list = np.arange(0.15,0.6001,0.05)

        self.load_data(self.file)
        self.process_data(problem)
        self.find_best_model(self.estimator_list,self.params_list,self.test_size_list)

    
    def load_data(self,problem):
        """
        Loads the necessary data.

        :param file: defined by the problem in 
            self.explore_dataset()
        """

        if problem == 'cancer':
            self.file = './HW4/model_dev_data/breast_cancer.csv'
        #elif problem == 'solar':
        #    self.file = './HW4/model_dev_data/solar.csv'
        print('Loading Data...')
        self.input_data = pd.read_csv(self.file)
        print('Done')
        return self.input_data


    def process_data(self,problem):
        """
        Preprocesses the data as needed.

        :param problem: the problem being explored
        """

        if problem == 'cancer':
            self.attributes = self.input_data.drop(['ID','diagnosis'],axis=1)
            self.columns = self.attributes.columns
            self.attributes = scale(self.attributes)
            self.targets = self.input_data['diagnosis']
        #elif problem == 'solar':
        #    self.attributes = self.input_data.drop(['TIMESTAMP','SOLARRADIATION_0003'],axis=1)
        #    self.columns = self.attributes.columns
        #    self.attributes = scale(self.attributes)
        #    self.targets = scale(self.input_data['SOLARRADIATION_0003'])
        return


    def split_valid(self,attr,targ,test_size=0.2,random=None):
        """
        Splits the training set into training data and 
        validation data.

        :param attr: training attributes
        :param targ: training targets
        :param test_size: the portion of data for validation
        :param random: allows for a random seed
        """

        print('Splitting Validation Data..')
        self.att_train, self.att_valid, self.tar_train, self.tar_valid = train_test_split(attr, targ, test_size=test_size, random_state=random)
        print('Done')
        #return att_train, self.att_valid, tar_train, self.tar_valid


    def split_test(self,test_size=0.2,random=None):
        """
        Splits the data set into training data and 
        testing data.

        :param test_size: the portion of data for validation
        :param random: allows for a random seed
        """

        print('Splitting Test Data..')
        self.att_full_train, self.att_test, self.tar_full_train, self.tar_test = train_test_split(self.attributes, self.targets, test_size=test_size, random_state=random)
        print('Done')


    def gridsearch(self,estimator,params):
        """
        Performs the GridSearchCV to find the best parameters
        for the current training set.

        :param estimator: the kind of estimator to search over
        :param params: the parameters to seach over
        :return: the best parameters and their validation score
        """

        self.gSearch = GridSearchCV(estimator=estimator,
                                       param_grid = params,
                                       cv = 5,
                                       verbose = 1,
                                       #error_score = 0.0,
                                       n_jobs = len(psutil.Process().cpu_affinity())//2
                                       #n_jobs = 12,
                                       )
        self.gSearch.fit(self.att_train,self.tar_train)

        best_params = self.gSearch.best_params_
        #best_score = self.gSearch.best_score_
        best_score = self.gSearch.score(self.att_valid,self.tar_valid)
        print(f'Grid Best Parameters: {[(k,v) for k,v in best_params.items()]}')
        print(f'Grid Best Score: {best_score}')

        return best_params,best_score


    def find_best_model(self,estimator_list,params_list,test_size_list,random=None):
        """
        Find the best kind of estimator and the best parameters
        for the current problem. Outputs log files and saves 
        the best model for each kind of estimator.

        :param estimator_list: the list of estimators to 
            explore
        :param params_list: the parameters associated with each
            kind of estimator in estimator_list; indices should 
            match
        :param test_size_list: the test size proportions that should 
            be explored
        :param random: allows for a random see
        """

        self.problem_path = os.path.dirname('./HW4/'+self.problem+'_models/')
        #creates model storage folder
        time_string = time.strftime('%Y%m%d-%H%M%S')
        model_storage = os.path.join(self.problem_path,'results'+time_string+'/')
        if not os.path.exists(os.path.dirname(model_storage)):
            os.makedirs(os.path.dirname(model_storage))
        
        # Initializes search
        self.all_models = []
        self.best_models = []
        self.best_model = None
        self.best_score = 0.0

        # Sets aside testing data
        self.split_test()

        # Loops over estimators
        for i in range(len(estimator_list)):

            print(f'\n\n\n\n\n\n\n\n\n\nTesting: {estimator_list[i]}')

            # Initializes estimator search
            self.best_estimator_model = None
            self.best_estimator_score = 0.0

            # Loops over testing sizes
            for size in test_size_list:
                print(f'\n\n\nSize: {size}')
                self.split_valid(self.att_full_train, self.tar_full_train, size,random)
                params = {}
                score = None
                # Gridsearches and returns best params and score on validation set
                params,score = self.gridsearch(estimator_list[i],params_list[i])
                current_model = {'validation score':score,'estimator':estimator_list[i],'test_size':size}
                current_model.update(params)
                self.all_models.append(current_model)
                # If this is the best model yet of this estimator type, save
                if score >= self.best_estimator_score:
                    self.best_estimator_model = current_model
                    self.best_estimator_score = score
                    self.estimator_saved_model = self.gSearch.best_estimator_
                    #self.estimator_saved_dict = current_model


            # Scores best estimator model on the testing set
            this_score = self.estimator_saved_model.score(self.att_test,self.tar_test)
            self.best_estimator_model['test score'] = this_score

            # Saves this model to list with testing score
            self.best_models.append(self.best_estimator_model)

            # Gets name and path for best estimator model
            estimator_name = f'{estimator_list[i]}'.replace('(','').replace(')','')
            model_name = estimator_name+'.joblib'
            model_file = os.path.join(model_storage,model_name)

            # Saves this model as best for estimator
            dump(self.estimator_saved_model,model_file)

            # If estimator has best overall model on testing set, save as such
            if this_score >= self.best_score:
                    self.best_model = self.best_estimator_model
                    self.best_score = this_score
                    self.saved_model = self.estimator_saved_model


        print('\n\n\nSaving Best Model...\n\n\n')
        #Save overall best model
        best_name = 'overall_best_no_selection'
        best_file_name = best_name+'.joblib'
        best_file = os.path.join(model_storage,best_file_name)
        dump(self.saved_model,best_file)

        #Print logfile of bests
        best_log_file = os.path.join(model_storage,'log_best.txt')
        with open(best_log_file,'w') as f:
            print(f'Overall Best Model: {self.best_model}\n', file=f)
            print(f'Overall Best Test Score: {self.best_score}\n\n', file=f)
            print(f'Best Models per Estimator: \n', file=f)
            for model in self.best_models:
                print(f'{model}\n', file=f)

        #Print logfile of all
        all_log_file = os.path.join(model_storage,'log_all.txt')
        with open(all_log_file,'w') as f:
            print(f'Overall Best Model: {self.best_model}\n', file=f)
            print(f'Overall Best Score: {self.best_score}\n\n', file=f)
            print(f'All Models: \n', file=f)
            for model in self.all_models:
                print(f'{model}\n', file=f)


    def eliminate_features(self,problem=None):
        """
        Performs a Recursive Feature Elimination on the 
        provided models, testing sizes, and scores 
        (determined from explore_dataset()) and saves models
        that out-perform their predecesors.

        :param problem: sets the problem to be evaluated
        """

        # Set directory for recording
        if self.problem_path==None:
            self.problem = problem
            self.problem_path = os.path.dirname('./HW4/'+problem+'_models/rfe_models/')

        # Import data
        self.load_data(problem)
        self.process_data(problem)

        # Manually set model params
        if self.problem == 'cancer':
            # List of regressors, test sizes, and original scores to reduce features on
            regs_list = [(LogisticRegression(C=0.5,solver='liblinear'),0.25,0.9912280701754386),
                         (Perceptron(alpha=5e-05,penalty='l1'),0.25,0.9473684210526315),
                         (RandomForestClassifier(criterion='entropy',max_features='log2',n_estimators=75),0.15,0.9912280701754386),
                         ]
        elif self.problem == 'solar':
            # List of regressors, test sizes, and original scores to reduce features on
            regs_list = [(LinearRegression(fit_intercept = False),0.15,0.8797824499658808)]
            
        # Run RFE on each type of model
        num_atts = self.attributes.shape[1]
        for reg in regs_list:
            score_to_beat = reg[2]
            self.split_test(reg[1])
            selector = RFECV(estimator = reg[0], step = 1, cv = 10)
            selector = selector.fit(self.att_full_train,self.tar_full_train)
            this_score = selector.score(self.att_test,self.tar_test)
            if this_score >= score_to_beat:
                # We've improved the model
                score_to_beat = this_score
                print(f'Improved model: {reg[0]}\nScore:{this_score}\n')

                ## Code below borrowed from professor's class notes ##
                ## Name removed for security of assignments ##
                # print out a formatted dataframe representation
                improved_features = pd.DataFrame({'Column':self.columns, 'Included':selector.support_, 'Rank':selector.ranking_})
                coefs = list(improved_features[improved_features['Included'] == True].Column)
                # get the fitted model from the selector. 
                new_model = selector.estimator_

                # print out the coefficients of the model. 
                try:
                    print(f'{new_model.intercept_:.3f}\t')
                    print(f'Num. Features: {len(coefs)}')
                    for c in range(len(coefs)):
                        print(f'\t+ {new_model.coef_[c]:.3f}[{coefs[c]}]')
                except:
                    print(f'Num. Features: {len(coefs)}')
                    for c in range(len(coefs)):
                        print(f'\t+ [{coefs[c]}]')
                
                ## Code above borrowed from class notes ##

                # Save improved model 
                improved_name = f'improved{reg[0]}'
                improved_model_name = improved_name+'.joblib'
                dump(new_model,os.path.join(self.problem_path,improved_model_name))

                # Save features
                improved_log_name = improved_name+'.txt'
                improved_log = os.path.join(self.problem_path,improved_log_name)
                with open(improved_log, 'w') as f:
                    print(f'Improved Model:', file=f)
                    print(f'Score: {this_score}', file=f)
                    try:
                        print(f'Num. Features: {len(coefs)}', file=f)
                        print(f'{new_model.intercept_:.3f}\t', file=f)
                        for c in range(len(coefs)):
                            print(f'\t+ {new_model.coef_[c]:.3f}[{coefs[c]}]', file=f)
                    except:
                        print(f'Num. Features: {len(coefs)}', file=f)
                        for c in range(len(coefs)):
                            print(f'\t+ [{coefs[c]}]', file=f)
            else:
                print(f'No improvement for features. Score: {this_score}')



def main():
    explorer = ModelDevelopment()
    explorer.explore_dataset('cancer')
    explorer.eliminate_features('cancer')
    explorer.explore_dataset('solar')
    explorer.eliminate_features('solar')


if __name__=='__main__':
    main()
#!/usr/bin/env python -*- coding: utf-8 -*-

import numpy as np

from sklearn.linear_model import LinearRegression, BayesianRidge, ARDRegression
from sklearn.linear_model import ElasticNet, LogisticRegression, RandomizedLogisticRegression
from sklearn.linear_model import PassiveAggressiveRegressor, RANSACRegressor
from sklearn.isotonic import IsotonicRegression
from sklearn import ensemble
from sklearn.svm import SVR
from sklearn.gaussian_process import GaussianProcess
from sklearn.tree import DecisionTreeRegressor

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from sts_data import get_meteor_scores, get_sts_scores

meteor_scores = np.array(get_meteor_scores())
sts_scores = np.array(get_sts_scores())


x = meteor_scores
y = sts_scores
n = len(sts_scores)

# Linear Regression
lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)

# Baysian Ridge Regression
br = BayesianRidge(compute_score=True)
br.fit(x[:, np.newaxis], y)

# Elastic Net
enr = ElasticNet()
enr.fit(x[:, np.newaxis], y)

# Passive Aggressive Regression
par = PassiveAggressiveRegressor()
par.fit(x[:, np.newaxis], y)

# RANSAC Regression
ransac = RANSACRegressor()
ransac.fit(x[:, np.newaxis], y)

# Logistic Regression
lgr = LogisticRegression()
lgr.fit(x[:, np.newaxis], y)


'''
# SLOW Regressors !!!!

# Randomized Log Regression
rlgr = RandomizedLogisticRegression()
rlgr.fit(x[:, np.newaxis], y)
# ARD Regression 
ard = ARDRegression(compute_score=True)
ard.fit(x[:, np.newaxis], y)
'''

# Isotonic Regression
ir = IsotonicRegression()
y_ = ir.fit_transform(x, y)

# Gradient Boosting Regression
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls'}
gbr = ensemble.GradientBoostingRegressor(**params)
gbr.fit(x[:, np.newaxis], y)

# Decision Tree Regression
dtr2 = DecisionTreeRegressor(max_depth=2)
dtr5 = DecisionTreeRegressor(max_depth=2)
dtr2.fit(x[:,np.newaxis], y) 
dtr5.fit(x[:,np.newaxis], y) 


'''
# Support Vector Regressions
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbf = svr_rbf.fit(x[:,np.newaxis], y)  
y_lin = svr_lin.fit(x[:,np.newaxis], y)  
y_poly = svr_poly.fit(x[:,np.newaxis], y)  
'''

'''
# Gaussian Process
gp = GaussianProcess(corr='squared_exponential', theta0=1e-1,
                     thetaL=1e-3, thetaU=1,
                     random_start=100)
gp.fit(x[:,np.newaxis], y) 
'''
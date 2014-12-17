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

meteor_scores = np.array(get_meteor_scores('meteor.output.train'))
sts_scores = np.array(get_sts_scores('score.train'))

test_meteor_scores = np.array(get_meteor_scores('meteor.output.test'))

x = meteor_scores
y = sts_scores
n = len(sts_scores)
xt = test_meteor_scores
xt = meteor_scores

# Linear Regression
print 'linear'
lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)
lr_sts_scores = lr.predict(xt[:, np.newaxis])

# Baysian Ridge Regression
print 'baysian ridge'
br = BayesianRidge(compute_score=True)
br.fit(x[:, np.newaxis], y)
br_sts_scores = br.predict(xt[:, np.newaxis])

# Elastic Net
print 'elastic net'
enr = ElasticNet()
enr.fit(x[:, np.newaxis], y)
enr_sts_scores = enr.predict(xt[:, np.newaxis])


# Passive Aggressive Regression
print 'passive aggressive'
par = PassiveAggressiveRegressor()
par.fit(x[:, np.newaxis], y)
par_sts_scores = par.predict(xt[:, np.newaxis])

# RANSAC Regression
print 'ransac'
ransac = RANSACRegressor()
ransac.fit(x[:, np.newaxis], y)
ransac_sts_scores = ransac.predict(xt[:, np.newaxis])

# Logistic Regression
print 'logistic'
lgr = LogisticRegression()
lgr.fit(x[:, np.newaxis], y)
lgr_sts_scores = lgr.predict(xt[:, np.newaxis])

'''
# SLOW Regressors !!!!
# Randomized Log Regression
rlgr = RandomizedLogisticRegression()
rlgr.fit(x[:, np.newaxis], y)
# ARD Regression 
ard = ARDRegression(compute_score=True)
ard.fit(x[:, np.newaxis], y)
## SLOW Regressors !!!!
'''

# Isotonic Regression
print 'isotonic'
ir = IsotonicRegression()
ir.fit_transform(x, y)
ir_sts_scores = ir.predict(xt)

# Gradient Boosting Regression
# Gives  "RuntimeWarning: divide by zero encountered in true_divide"
print 'gradient boosting'
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls'}
gbr = ensemble.GradientBoostingRegressor(**params)
gbr.fit(x[:, np.newaxis], y)
gbr_sts_scores = gbr.predict(xt[:, np.newaxis])


'''
# Decision Tree Regression
# Gives  "RuntimeWarning: divide by zero encountered in true_divide"
print 'decision tree'
dtr2 = DecisionTreeRegressor(max_depth=2)
dtr5 = DecisionTreeRegressor(max_depth=2)
dtr2.fit(x[:,np.newaxis], y)
dtr5.fit(x[:,np.newaxis], y) 
dtr2_sts_scores = dtr2.predict(xt[:, np.newaxis])
dtr5_sts_scores = dtr5.predict(xt[:, np.newaxis])
'''


# Support Vector Regressions
print 'support vector'
svr_lin = SVR(kernel='linear', C=1e3)
y_lin = svr_lin.fit(x[:,np.newaxis], y)  
y_lin_sts_scores = y_lin.predict(xt[:, np.newaxis])

svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_poly = svr_poly.fit(x[:,np.newaxis], y)
y_poly_sts_scores = y_poly.predict(xt[:, np.newaxis])

# Gives runtime warning.
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
y_rbf = svr_rbf.fit(x[:,np.newaxis], y)  
y_rbf_sts_scores = y_rbf.predict(xt[:, np.newaxis])




scores = np.array(zip(lr_sts_scores,
br_sts_scores,
par_sts_scores,
[i[0] for i in ransac_sts_scores],
lgr_sts_scores,
ir_sts_scores, gbr_sts_scores,
y_lin_sts_scores, y_poly_sts_scores, y_rbf_sts_scores))



for i, j in zip(scores, y):
    print i, j


'''
# Gaussian Process
gp = GaussianProcess(corr='squared_exponential', theta0=1e-1,
                     thetaL=1e-3, thetaU=1,
                     random_start=100)
xu = np.unique(x) 
idx = [np.where(x==x1)[0][0] for x1 in xu]
gp.fit(xu[:,np.newaxis], y[idx])
#gp.fit(x[:,np.newaxis], y)
''' 
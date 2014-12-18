#!/usr/bin/env python -*- coding: utf-8 -*-

import math

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
from asiya import get_asiya_scores

meteor_scores = np.array(get_meteor_scores('meteor.output.train'))
sts_scores = np.array(get_sts_scores('score.train'))

test_meteor_scores = np.array(get_meteor_scores('meteor.output.test'))

x = meteor_scores
_x, to_remove = get_asiya_scores()

x = np.array(_x)
y = sts_scores
y =np.delete(y, to_remove, axis=0)
n = len(y)
xt = x

#print len(_x), len(x), len(y)

# Linear Regression
print 'linear'
lr = LinearRegression()
#lr.fit(x[:, np.newaxis], y)
#lr_sts_scores = lr.predict(xt[:, np.newaxis])
lr.fit(x, y)
lr_sts_scores = lr.predict(xt)


# Baysian Ridge Regression
print 'baysian ridge'
br = BayesianRidge(compute_score=True)
#br.fit(x[:, np.newaxis], y)
#br_sts_scores = br.predict(xt[:, np.newaxis])
br.fit(x, y)
br_sts_scores = br.predict(xt)


# Elastic Net
print 'elastic net'
enr = ElasticNet()
#enr.fit(x[:, np.newaxis], y)
#enr_sts_scores = enr.predict(xt[:, np.newaxis])
enr.fit(x, y)
enr_sts_scores = enr.predict(xt)


# Passive Aggressive Regression
print 'passive aggressive'
par = PassiveAggressiveRegressor()
par.fit(x, y)
par_sts_scores = par.predict(xt)
#par.fit(x[:, np.newaxis], y)
#par_sts_scores = par.predict(xt[:, np.newaxis])

# RANSAC Regression
print 'ransac'
ransac = RANSACRegressor()
#ransac.fit(x[:, np.newaxis], y)
#ransac_sts_scores = ransac.predict(xt[:, np.newaxis])
ransac.fit(x, y)
ransac_sts_scores = ransac.predict(xt)


# Logistic Regression
print 'logistic'
lgr = LogisticRegression()
#lgr.fit(x[:, np.newaxis], y)
#lgr_sts_scores = lgr.predict(xt[:, np.newaxis])
lgr.fit(x, y)
lgr_sts_scores = lgr.predict(xt)


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

'''
# Isotonic Regression
#print 'isotonic'
ir = IsotonicRegression()
ir.fit_transform(x, y)
ir_sts_scores = ir.predict(xt)

# Gradient Boosting Regression
# Gives  "RuntimeWarning: divide by zero encountered in true_divide"
#print 'gradient boosting'
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls'}
gbr = ensemble.GradientBoostingRegressor(**params)
gbr.fit(x[:, np.newaxis], y)
gbr_sts_scores = gbr.predict(xt[:, np.newaxis])
'''

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
y_lin = svr_lin.fit(x, y)  
y_lin_sts_scores = y_lin.predict(xt)
#y_lin = svr_lin.fit(x[:,np.newaxis], y)  
#y_lin_sts_scores = y_lin.predict(xt[:, np.newaxis])


svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_poly = svr_poly.fit(x, y)
y_poly_sts_scores = y_poly.predict(xt)
#y_poly = svr_poly.fit(x[:,np.newaxis], y)
#y_poly_sts_scores = y_poly.predict(xt[:, np.newaxis])


# Gives runtime warning.
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
#y_rbf = svr_rbf.fit(x[:,np.newaxis], y)  
#y_rbf_sts_scores = y_rbf.predict(xt[:, np.newaxis])
y_rbf = svr_rbf.fit(x, y)  
y_rbf_sts_scores = y_rbf.predict(xt)


scores = np.array(zip(lr_sts_scores,
br_sts_scores,
par_sts_scores,
[i[0] for i in ransac_sts_scores],
lgr_sts_scores,
##ir_sts_scores, gbr_sts_scores))
y_lin_sts_scores, y_poly_sts_scores, y_rbf_sts_scores))


mask = ~np.any(np.isnan(scores), axis=1)

newx = scores[mask]
newy = y[mask]


#print newx
#print len(newx), len(newy)
def get_mean_error(regressor):
    lgr2 = regressor
    lgr2.fit(newx, newy)
    out = lgr2.predict(newx)
    
    #for i,j,k in zip(newx, out, y):
    #    print i,j, k
    
    mean_error = []
    for i,j,k in zip(newx, out, y): 
        mean_error.append(math.fabs(k-j))   
    print 'ALL:', sum(mean_error) / float(len(mean_error))


    mean_error = []
    for i,j,k in zip(newx, out, y): 
        if 0 < k < 1:
            mean_error.append(math.fabs(k-j))
    print '0-1:', sum(mean_error) / float(len(mean_error))
    
    mean_error = []
    for i,j,k in zip(newx, out, y): 
        if 1 < k < 2:
            mean_error.append(math.fabs(k-j))
    print '1-2:', sum(mean_error) / float(len(mean_error))
    
    mean_error = []
    for i,j,k in zip(newx, out, y): 
        if 3 < k < 4:
            mean_error.append(math.fabs(k-j))
    print '3-4:', sum(mean_error) / float(len(mean_error))
    
    mean_error = []
    for i,j,k in zip(newx, out, y): 
        if 4 < k < 5.1:
            mean_error.append(math.fabs(k-j))
    print '4-5:', sum(mean_error) / float(len(mean_error))
    
r = [LinearRegression(),
#LogisticRegression,
BayesianRidge(),
SVR(kernel='linear', C=1e3),
SVR(kernel='poly', C=1e3, degree=2),
SVR(kernel='rbf', C=1e3, gamma=0.1)
]


for i in r:
    print i
    try:
        get_mean_error(i)
    except:
        pass
    print '#######'


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
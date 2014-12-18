#!/usr/bin/env python -*- coding: utf-8 -*-

import math

import numpy as np

import cPickle as pickle

from sklearn.linear_model import LinearRegression, BayesianRidge, ARDRegression
from sklearn.linear_model import ElasticNet, LogisticRegression, RandomizedLogisticRegression
from sklearn.linear_model import PassiveAggressiveRegressor, RANSACRegressor
from sklearn.isotonic import IsotonicRegression
from sklearn import ensemble
from sklearn.svm import SVR
from sklearn.gaussian_process import GaussianProcess
from sklearn.tree import DecisionTreeRegressor


m = 'meteor'

if m == 'asiya':
    x = np.loadtxt('x.asiya.train')
    y = np.loadtxt('y.asiya.train')
elif m == 'meteor':
    x = np.loadtxt('x.meteor.train')[:,np.newaxis]
    y = np.loadtxt('y.meteor.train')
    x_test = np.loadtxt('x.meteor.test')[:,np.newaxis]

regressors = {'lr':LinearRegression(),
'br':BayesianRidge(compute_score=True),
'enr':ElasticNet(),
'par':PassiveAggressiveRegressor(),
'ransac':RANSACRegressor(),
'lgr':LogisticRegression(),
'svr_lin':SVR(kernel='linear', C=1e3),
'svr_poly':SVR(kernel='poly', C=1e3, degree=2),
'svr_rbf':SVR(kernel='rbf', C=1e3, gamma=0.1)}

def build_regressors(num):
    rgs = regressors[num]
    rgs.fit(x, y)
    with open(num+'.'+m+'.pk', 'wb') as fid:
        pickle.dump(rgs, fid)

'''
x = x_test
lr = pickle.load(open("lr."+m+'.pk', 'rb'))
br = pickle.load(open("br."+m+'.pk', 'rb'))
par = pickle.load(open("par."+m+'.pk', 'rb'))
ransac = pickle.load(open("ransac."+m+'.pk', 'rb'))
lgr = pickle.load(open("lgr."+m+'.pk', 'rb'))
svr_lin = pickle.load(open("svr_lin."+m+'.pk', 'rb'))
svr_poly = pickle.load(open("svr_poly."+m+'.pk', 'rb')) 
svr_rbf = pickle.load(open("svr_rbf."+m+'.pk', 'rb'))

lr_sts_scores = lr.predict(x)
br_sts_scores = br.predict(x)
par_sts_scores = par.predict(x)
ransac_sts_scores = ransac.predict(x)
lgr_sts_scores = lgr.predict(x)
y_lin_sts_scores = svr_lin.predict(x)
y_poly_sts_scores = svr_poly.predict(x)
y_rbf_sts_scores = svr_rbf.predict(x)

scores = np.array(zip(lr_sts_scores,
br_sts_scores,
par_sts_scores,
[i[0] for i in ransac_sts_scores],
lgr_sts_scores,
y_lin_sts_scores, y_poly_sts_scores, y_rbf_sts_scores))

for i in scores:
    print i
'''
#mask = ~np.any(np.isnan(scores), axis=1)
#newx = scores[mask]
#newy = y[mask]


r = [LinearRegression(),
BayesianRidge(),
SVR(kernel='linear', C=1e3),
SVR(kernel='poly', C=1e3, degree=2),
SVR(kernel='rbf', C=1e3, gamma=0.1)
]

    
def main(num):
    build_regressors(num)

if __name__ == '__main__':
  import sys
  main(*sys.argv[1:])

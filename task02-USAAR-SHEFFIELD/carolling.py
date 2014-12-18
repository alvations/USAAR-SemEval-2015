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



def build_regressors(num):
    x = np.loadtxt('x.train')
    y = np.loadtxt('y.train')
    regressors = {'lr':LinearRegression(),
    'br':BayesianRidge(compute_score=True),
    'enr':ElasticNet(),
    'par':PassiveAggressiveRegressor(),
    'ransac':RANSACRegressor(),
    'lgr':LogisticRegression(),
    'svr_lin':SVR(kernel='linear', C=1e3),
    'svr_poly':SVR(kernel='poly', C=1e3, degree=2),
    'svr_rbf':SVR(kernel='rbf', C=1e3, gamma=0.1)}
    rgs = regressors[num]
    rgs.fit(x, y)
    pickle.dump(num+'.pk', rgs)
    
def main(num):
    build_regressors(num)

if __name__ == '__main__':
  import sys
  main(*sys.argv[1:])


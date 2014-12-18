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

x = np.loadtxt('x.meteor.train')[:,np.newaxis]
y = np.loadtxt('y.meteor.train')
x_test = np.loadtxt('x.meteor.test')[:,np.newaxis]


latent_matrix = np.array(zip(LinearRegression().fit(x,y).predict(x_test),
BayesianRidge(compute_score=True).fit(x,y).predict(x_test),
ElasticNet().fit(x,y).predict(x_test),
PassiveAggressiveRegressor().fit(x,y).predict(x_test),
RANSACRegressor().fit(x,y).predict(x_test),
LogisticRegression().fit(x,y).predict(x_test),
SVR(kernel='linear', C=1e3).fit(x,y).predict(x_test),
SVR(kernel='poly', C=1e3, degree=2).fit(x,y).predict(x_test),
SVR(kernel='rbf', C=1e3, gamma=0.1).fit(x,y).predict(x_test)))


mask = ~np.any(np.isnan(latent_matrix), axis=1)
newx = latent_matrix[mask]
newy = y[mask]


last_layer = SVR(kernel='rbf', C=1e3, gamma=0.1)
last_layer.fit(newx, newy)
sts_task_output = last_layer.predict(x_test)

print len(sts_task_output)

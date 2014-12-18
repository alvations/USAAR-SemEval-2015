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

import random
random.seed(0)

def get_latent_matrix(_x,_y,_z):
    latent_matrix = np.array(zip(LinearRegression().fit(_x,_y).predict(_z),
    BayesianRidge(compute_score=True).fit(_x,_y).predict(_z),
    ElasticNet().fit(_x,_y).predict(_z),
    PassiveAggressiveRegressor().fit(_x,_y).predict(_z),
    RANSACRegressor().fit(_x,_y).predict(_z),
    LogisticRegression().fit(_x,_y).predict(_z)))
    #SVR(kernel='linear', C=1e3).fit(_x,_y).predict(_z),
    #SVR(kernel='poly', C=1e3, degree=2).fit(_x,_y).predict(_z),
    #SVR(kernel='rbf', C=1e3, gamma=0.1).fit(_x,_y).predict(_z)))
    return latent_matrix

x = np.loadtxt('x.meteor.train')[:,np.newaxis]
y = np.loadtxt('y.meteor.train')
x_test = np.loadtxt('x.meteor.test')[:,np.newaxis]

runs = []

for _ in range(100):
    train_latent_matrix = get_latent_matrix(x,y,x)
    test_latent_matrix = get_latent_matrix(x,y,x_test)
    # Clean out rows with NaN.
    mask = ~np.any(np.isnan(train_latent_matrix), axis=1)
    newx = train_latent_matrix[mask]
    newy = y[mask]

    last_layer = SVR(kernel='rbf', C=1e3, gamma=0.1)
    #last_layer = BayesianRidge()
    last_layer.fit(newx, newy)

    output = last_layer.predict(test_latent_matrix)
    assert len(output) == 8500
    runs.append(output)

fout = io.open('modelz.output', 'w')
for line in zip(*runs):
    avg =sum(line)/len(line)
    if avg > 5:
        fout.write(str(5.0000)+'\n')
    if avg < 0:
        fout.write(str(0.0000)+'\n')
    else:
        fout.write(str(round(avg,4))+'\n')
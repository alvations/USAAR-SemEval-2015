#!/usr/bin/env python -*- coding: utf-8 -*-

import numpy as np

from sklearn.linear_model import LinearRegression, BayesianRidge
from sklearn.isotonic import IsotonicRegression
from sklearn import ensemble
from sklearn.gaussian_process import GaussianProcess


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

# Isotonic Regression
ir = IsotonicRegression()
y_ = ir.fit_transform(x, y)

# Gradient Boosting Regression
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls'}
gbr = ensemble.GradientBoostingRegressor(**params)
gbr.fit(x[:, np.newaxis], y)

# Gaussian Process
gp = GaussianProcess(corr='squared_exponential', theta0=1e-1,
                     thetaL=1e-3, thetaU=1,
                     random_start=100)
gp.fit(x[:, np.newaxis], y)

#!/usr/bin/env python -*- coding: utf-8 -*-

import math
import cPickle as pickle

import numpy as np

from sklearn.svm import SVR
from sklearn.linear_model import BayesianRidge


x = np.loadtxt('x.asiya.train')[:,np.newaxis]
y = np.loadtxt('y.asiya.train')
x_test = np.loadtxt('x.asiya.test')[:,np.newaxis]

br = pickle.load(open("br."+'asiya'+'.pk', 'rb'))

runs = []
for _ in range(10): 
    output = br.predict(x_test)
    runs.append(output)


fout = open('modely.10.output', 'w')
for line in zip(*runs):
    avg =sum(line)/len(line)
    if avg > 5:
        avg = 5.0
    elif avg < 0:
        avg = 0.0
    print str(float(avg))[:6]
    fout.write(str(float(avg))[:6]+'\n')



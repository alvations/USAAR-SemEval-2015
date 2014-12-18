#!/usr/bin/env python -*- coding: utf-8 -*-

import math

import numpy as np

import cPickle as pickle

def get_latent_matrix(_x,_y,_z):
    m = 'asiya'
    lr = pickle.load(open("lr."+m+'.pk', 'rb'))
    br = pickle.load(open("br."+m+'.pk', 'rb'))
    enr = pickle.load(open("enr."+m+'.pk', 'rb'))
    par = pickle.load(open("par."+m+'.pk', 'rb'))
    ransac = pickle.load(open("ransac."+m+'.pk', 'rb'))
    lgr = pickle.load(open("lgr."+m+'.pk', 'rb')) 
    svr_rbf = pickle.load(open("svr_rbf."+m+'.pk', 'rb'))
    
    
    latent_matrix = np.array(zip(lr.fit(_x,_y).predict(_z),
    br.fit(_x,_y).predict(_z),
    enr.predict(_z),
    par.fit(_x,_y).predict(_z),
    ransac.fit(_x,_y).predict(_z),
    lgr.fit(_x,_y).predict(_z),
    svr_rbf.fit(_x,_y).predict(_z)))
    
    return latent_matrix


x = np.loadtxt('x.asiya.train')
y = np.loadtxt('y.asiya.train')
x_test = x

runs = []

for _ in range(5):
    
    train_latent_matrix = get_latent_matrix(x,y,x)
    #test_latent_matrix = get_latent_matrix(x,y,x_test)
    
    # Clean out rows with NaN.
    mask = ~np.any(np.isnan(train_latent_matrix), axis=1)
    newx = train_latent_matrix[mask]
    newy = y[mask]
    
    test_latent_matrix = newx
    
    last_layer = BayesianRidge()
    last_layer.fit(newx, newy)
    output = last_layer.predict(test_latent_matrix)
    
    for i,j in zip(output, newy):
        print i
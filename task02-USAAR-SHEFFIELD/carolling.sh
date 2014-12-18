#!/bin/bash

nohup python carolling.py lr &
nohup python carolling.py br &
nohup python carolling.py enr &
nohup python carolling.py par &
nohup python carolling.py ransac &
nohup python carolling.py lgr &
nohup python carolling.py svr_lin &
nohup python carolling.py svr_poly &
nohup python carolling.py svr_rbf &
#!/bin/bash
set -m
python -m csvtoDB.py
python application.py
fg %1
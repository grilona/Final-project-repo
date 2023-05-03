import csv
import torch
import numpy as np

data_path = 'datasetcsv.csv'
data_numpy = np.loadtxt(data_path, dtype='str', delimiter=",")
print(type(data_numpy))

import csv
import torch
import numpy as np


def pytorchnn_data_load():
    data_path = 'pytorchnn\dataset.csv'
    data_numpy = np.loadtxt(data_path, dtype=np.float32, delimiter=",", skiprows=1)

    col_names = next(csv.reader(open(data_path), delimiter=","))
    print(col_names)
    data_pytorch = torch.from_numpy(data_numpy)
    print(data_pytorch)


class Pytorchnn:
    def __init__(self):
        pytorchnnDataLoad()
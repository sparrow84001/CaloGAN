import time
import os
from sys import platform

import numpy as np
import matplotlib.pyplot as plt
from geant3_parser import Geant3DataFile
from geant3_parser import build_train_set

file_name = os.path.join('data', 'shower_geant3_new.dat')
data_file = Geant3DataFile(file_name, skip_lines=3)
inputs, true_e, sum_e = build_train_set(data_file, 50000, add_real_xy=False, normalize=True)
#print(inputs.shape)
input_dims = inputs.shape[1]

from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Input, Dense


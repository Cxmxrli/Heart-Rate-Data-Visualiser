#Main folder to start ecg reading project 

import scipy                    #to get ecg data as well as analyzing it and smoothing it
import numpy as np              #for data/numbers
import pandas as pd             #for data/numbers
import matplotlib.pyplot as plt #for creating graphs/plots

#grabbing ecg data from scipy datasets
ekg = scipy.datasets.electrocardiogram() 

ekg = pd.Series(ekg) #converting to pandas series for easier manipulation
ekg.plot 
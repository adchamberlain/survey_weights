## Sample Survey Weights in Python

import pandas as pd
import numpy as np

path = '/Users/andrew/Desktop/'

df = pd.read_csv(path + 'sample_weights.csv')

# Sample weights helper function for weighted mean.
def w_mean(frame, mean_var, weight):
    d = frame[mean_var]
    w = frame[weight]
    try: 
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return np.nan

# Sample weights helper function for weighted sum.
def w_sum(frame, sum_var, weight):
    d = frame[sum_var]
    w = frame[weight]
    try: 
        return (d * w).sum()
    except ZeroDivisionError:
        return np.nan

# Weighted mean income by sex.  
df.groupby('Sex').apply(w_mean, 'Income', 'Weight')

# Weighted sum of income by sex. 
df.groupby('Sex').apply(w_sum, 'Income', 'Weight')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

maxnum = 100
t = np.linspace(0, 10, num=maxnum)
noise = 2*np.random.rand(maxnum) -1

linear1 = 3*t + 1
linear1 = linear1 + noise

linear2 = 2*t + 1
noise = 2*np.random.rand(maxnum) -1
linear2 = linear2 + noise

exponential1 = 30*np.exp(-t)
noise = 2*np.random.rand(maxnum) -1
exponential1 = exponential1 + noise


lin1 = lambda t: 3*t + 1 + 2*np.random.rand(1) -1
lin2 = lambda t: 2*t + 1 + 2*np.random.rand(1) -1
expon1 = lambda t: 30*np.exp(-t) + 2*np.random.rand(1) -1


numTrials = 10
header = ["t", "trial", "category", "A", "B", "C"]
category = ['foo','bar','baz']
rows = np.empty((1, 6))

with open("fakedata.csv", 'w') as fp:
    fp.write(','.join(header))
    fp.write('\n')
    for trial in [1,2,3,4,5,6,7,8,9,10]:
        for n in t[1:]:
            for cat in category:
                tmp = [str(n), str(trial), cat, str(lin1(n)[0]), str(lin2(n)[0]), str(expon1(n)[0]) ]
                fp.write(','.join(tmp))
                fp.write('\n')




#!/usr/bin/env python3.6

import numpy as np
import matplotlib.pyplot as plt
import os

#inputdir = "out_chap06c"
inputdir = "out_chap06a-1"

def parse_datafile(path):
    with open(path) as f:
        wanted_sum, data_len = f.readline().split()
        for line in f:
            if "real" in line:
                _, time = line.split()
        return int(wanted_sum), int(data_len), float(time)


allsums = set()
alllens = set()

raw_data = {}
for f in os.listdir(inputdir):
    wanted_sum, data_len, time = parse_datafile(os.path.join(inputdir, f))
    l = raw_data.setdefault((wanted_sum, data_len), [])
    l.append(time)
    allsums.add(wanted_sum)
    alllens.add(data_len)


x = sorted(list(allsums))
numpyx = np.array(x)

fig, axs = plt.subplots(nrows=len(alllens), sharex=True, figsize=(12,6))

for i, data_len in enumerate(sorted(alllens)):
    ax = axs[i]
    ax.set_title('data_len={}'.format(data_len))
    y = []
    minerr = []
    maxerr = []
    x2 = []
    for point in x:
        if (point, data_len) in raw_data:
            datumlist = raw_data[(point, data_len)]
            y.append(sum(datumlist) / len(datumlist))
            minerr.append(min(datumlist))
            maxerr.append(max(datumlist))
            x2.append(point)
    ax.errorbar(x2, y, yerr=[minerr,maxerr])

#plt.show()
plt.savefig("{}.svg".format(inputdir))

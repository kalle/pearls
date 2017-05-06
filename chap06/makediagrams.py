#!/usr/bin/env python3.5

import numpy as np
import matplotlib.pyplot as plt
import os


def parse_datafile(path):
    with open(path) as f:
        time = -100
        wanted_sum, data_len = f.readline().split()
        for line in f:
            if "real" in line:
                _, time = line.split()
        return int(wanted_sum), int(data_len), float(time)


def read_data_from(inputdir):
    all_sums = set()
    all_lens = set()

    raw_data = {}
    for f in os.listdir(inputdir):
        wanted_sum, data_len, time = parse_datafile(os.path.join(inputdir, f))
        l = raw_data.setdefault((wanted_sum, data_len), [])
        l.append(time)
        all_sums.add(wanted_sum)
        all_lens.add(data_len)

    return raw_data, sorted(list(all_sums)), sorted(list(all_lens))


def plot_sum_vs_time(input_dir, output_file, title):
    raw_data, all_sums, all_lens = read_data_from(input_dir)
    fig, axs = plt.subplots(nrows=len(all_lens), sharex=True, figsize=(12, 6))
    fig.suptitle(title)

    for i, data_len in enumerate(all_lens):
        ax = axs[i]
        ax.set_title('data_len={}'.format(data_len))
        y = []
        minerr = []
        maxerr = []
        for point in all_sums:
            if (point, data_len) in raw_data:
                datumlist = raw_data[(point, data_len)]
                y.append(sum(datumlist) / len(datumlist))
                minerr.append(min(datumlist))
                maxerr.append(max(datumlist))
        ax.errorbar(all_sums, y, yerr=[minerr, maxerr])
        ax.set_ylabel('time (s)')

    plt.xticks(all_sums)
    fig.autofmt_xdate()
    ax.set_xlabel('data size')
    plt.savefig(output_file)

def plot_datalen_vs_time(expected_sum, input_dir, output_file, title):
    raw_data, all_sums, all_lens = read_data_from(input_dir)
    fig, ax = plt.subplots(nrows=1, sharex=True, figsize=(12, 6))
    fig.suptitle(title)

    y = []
    minerr = []
    maxerr = []
    for point in all_lens:
        if (expected_sum, point) in raw_data:
            datumlist = raw_data[(expected_sum, point)]
            y.append(sum(datumlist) / len(datumlist))
            minerr.append(min(datumlist))
            maxerr.append(max(datumlist))
    ax.errorbar(all_lens, y, yerr=[minerr, maxerr])

    plt.xticks(all_lens)
    plt.yscale('log')
    fig.autofmt_xdate()
    ax.set_ylabel('time (s)')
    ax.set_xlabel('data size')
    plt.savefig(output_file)


if __name__ == "__main__":
    plot_sum_vs_time("out_chap06a-1", "chap06a-1.svg", "All permutations")
    plot_sum_vs_time("out_chap06c", "chap06c.svg", "With pruning")
    plot_datalen_vs_time(150, "out_chap06c_sum150", "chap06c_sum150.svg", "chap06c")

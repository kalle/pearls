#!/usr/bin/env python

from random import randint

def generate_file(number_len, num_numbers):
    with open("random_{}.dat".format(number_len), "w") as f:
        for _ in range(0, num_numbers):
            f.write(''.join(['%s' % randint(0,9) for num in range(0,number_len)]))
            f.write('\n')


for number_len in range(10, 30):
    generate_file(number_len, 10)

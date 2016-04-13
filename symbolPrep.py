#!/usr/bin/env python
import sys
import wave
import math
import struct
import numpy as np
import random
import argparse
from itertools import izip_longest




def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

N = 11

data_in = np.random.random_integers(0,1,N)
print 'data in', data_in

#put into 5 bit chunks and convert to decimal for symbols..
for chunk in grouper(data_in,5,''):
	for index in range(4)
	symbol += (int(chunk[index])*2^4-index)
	print symbol



#!/usr/bin/env python
import numpy as np
import random

N=11
data_in = np.random.random_integers(0,1,N)

symbolData =[]
#put into 5 bit chunks and return decimal for symbols..
symbol = 0
for i in xrange(0, len(data_in), 5):
	chunk = data_in[i:i+5]
	print chunk
	for b in range(len(chunk)):
		symbol += chunk[b]*(2**(len(chunk)-b-1))
	print 'symbol..............', symbol
	symbolData.append(symbol)
	symbol = 0

print symbolData

for symbolD in symbolData:
	print 'test', symbolD


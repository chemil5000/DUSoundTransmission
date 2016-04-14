#!/usr/bin/env python
import numpy as np
import random

def symbolConverter(input)

	symbolData =[]
	#put into 5 bit chunks and return decimal for symbols..
	symbol = 0
	for i in xrange(0, len(input), 5):
		chunk = data_in[i:i+5]
		print chunk
		for b in range(len(chunk)):
			symbol += chunk[b]*(2**(len(chunk)-b-1))
		print 'symbol..............', symbol
		symbol = 0
		symbolData.append(symbol)



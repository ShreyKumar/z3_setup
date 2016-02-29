#!/usr/bin/python

import sys
from z3 import *
import math

filename = sys.argv[1]
file = open(filename, 'r')
num = file.read(1)
x = float(num)

s = Solver()
s.add(x.is_integer())

print s.check()

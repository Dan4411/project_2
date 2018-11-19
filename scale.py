import math
S = 0.248
N = 10 / S
L = 724 / N
SCALE = round(((2 * 695 * 10**8) / L), 1)
print('1 :', SCALE)
print('Это значит, что в 1 сантиметре', round(SCALE/100000), 'километров')


import numpy as np

print("band.kpointsNumber = [", end = '')
for x in np.linspace(0e0, 1e0, 30):
  for y in np.linspace(0e0, 1e0, 30):
    print("30,", end = '')
    #print("K2,", end = '')
print("]")

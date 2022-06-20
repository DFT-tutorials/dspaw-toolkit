import numpy as np
import subprocess
import shutil



with open('band.in','r') as f:
  lines = f.read().split('\n')


ind = 0

for x in np.linspace(0e0, 1e0, 30):
  for y in np.linspace(0e0, 1e0, 30):
    #print("{0:18.10f}, {1:18.10f}, 0.0000,".format(x, y), end = '')
    #print("{0:18.10f}, {1:18.10f}, 0.5000,".format(x, y), end = '')
    lines[-1]  = "  band.kpointsCoord   = [ {0:18.10f}, {1:18.10f}, {2:18.10f} ,{3:18.10f}, {4:18.10f}, {5:18.10f} ] \n".format(x, y, -0.5, x, y, 0.5)
    with open('band1.in','w') as f:
      for item in lines:
        f.write(item + '\n')
    subprocess.call('DS-PAW -mpi mpirun -mpiargs "--map-by node:PE=1" band1.in', shell = True)
    shutil.copy('band.json', 'band.json' + str(ind))
    ind += 1

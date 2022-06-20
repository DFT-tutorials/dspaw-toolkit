import matplotlib.pyplot as plt
import json
import numpy as np


f=open('band.json','r')
band = json.load(f)['BandInfo']
ene  = band['Spin1']['Band']
fer  = band['EFermi']
nbnd = band['NumberOfBand']
nkpts  = band['NumberOfKpoints']
print(fer, nbnd, nkpts)
print(len(ene))
eig = [[] for i in range(nbnd)]

ind = 0
for i in range(nkpts):
  for j in range(nbnd):
    eig[j].append(ene[ind])
    ind += 1

fig = plt.figure()
ax  = fig.add_subplot(111)
for i in range(nbnd):
  ax.plot(np.array(eig[i]) - fer, color='b')
ax.set_ylim(-5,2)
plt.savefig('band.png',format='png',dpi=400)

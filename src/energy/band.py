import numpy as np
import scipy
import json
import os
import matplotlib.pyplot as plt
import sys


def read_bandjson(fname):
    '''Parse band.json file'''
    with open(fname, 'r') as f:
        data = json.load(f)['BandInfo']
        kpt  = np.array(data['CoordinatesOfKPoints'])
        bnd1 = np.array(data['Spin1']['Band'])
        nkpt = data['NumberOfKpoints']
        nbnd = data['NumberOfBand']

    kpt  = kpt.reshape(nkpt,3)
    bnd1 = bnd1.reshape(nkpt, nbnd)
    return kpt, nkpt, nbnd, bnd1


def read_bandjson_sp(fname):
    '''Parse band.json file'''
    with open(fname, 'r') as f:
        data = json.load(f)['BandInfo']
        kpt  = np.array(data['CoordinatesOfKPoints'])
        bnd1 = np.array(data['Spin1']['Band'])
        bnd2 = np.array(data['Spin2']['Band'])
        nkpt = data['NumberOfKpoints']
        nbnd = data['NumberOfBand']

    kpt  = kpt.reshape(nkpt,3)
    bnd1 = bnd1.reshape(nkpt, nbnd)
    bnd2 = bnd2.reshape(nkpt, nbnd)
    return kpt, nkpt, nbnd, bnd1, bnd2


def dump_bnd_csv_sp(kpt, bnd1, bnd2):
    '''Convert energy file into x,y,z,ene1,...'''
    if not os.path.isfile('band.csv'):
        with open('band.csv','w') as f:
            f.write("kx, ky, kz")
            for i in range(nbnd):
                f.write(",{0:3s}{1:<3d}".format('ene', i))
            f.write("\n")

    with open('band.csv','a') as f:
        for i in range(len(kpt)):
            f.write("{0:18.10f}, {1:18.10f}, {2:18.10f}, ".format(kpt[i][0], kpt[i][1], kpt[i][2]))
            for j in range(nbnd):
                f.write("{0:18.10f}, ".format(bnd1[i][j]))
            for j in range(nbnd):
                f.write("{0:18.10f},  ".format(bnd2[i][j]))
            f.write("\n")


def plot_bnd_sp(kpt, bnd1, bnd2):
    '''Plot spin polarized band structure'''
    fig  = plt.figure()
    bnd1 = np.transpose(bnd1)
    bnd2 = np.transpose(bnd2)
    ax  = fig.add_subplot(111)
    for i in range(len(bnd1)):
        ax.plot(bnd1[i], color='r')
        ax.plot(bnd2[i], color='b')
    plt.savefig('band.png',format='png',dpi=400)
    plt.close()


def fs():
    if os.path.isfile('band.csv'):
        shutil.rm('band.csv')
    ind   = []
    files = [ item for item in os.listdir() if 'band.json' in item and item != 'band.json']
    for item in files:
        ind.append(int(item.replace('band.json','')))

    for i in range(max(ind)):
        item = 'band.json' + str(i)
        kpt, nkpt, nbnd, bnd1, bnd2 = read_bandjson_sp(item)
        dump_bnd_csv_sp(kpt, bnd1, bnd2)


def band():
    '''loading band.json file'''
    kpt, nkpt, nbnd, bnd1 = read_bandjson_sp('band.json')


if __name__ == "__main__":
    if sys.argv[1] == 'fs':
        fs()
    elif sys.argv[1] == 'band':
        band()

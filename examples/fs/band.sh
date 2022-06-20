#!/bin/bash
#SBATCH -p normal
#SBATCH -o _out.%j.log
#SBATCH -e _err.%j.log
#SBATCH -J ds-paw
#SBATCH --exclusive

#SBATCH -N 1
#SBATCH --ntasks-per-node=24
#SBATCH -t 1000:00:00

#unlimit memory
 
ulimit -s unlimited
ulimit -l unlimited

# load path

source /data/profile/ds-paw.env

#DS-PAW -mpi mpirun -mpiargs "--map-by node:PE=1" band2.in
python3 gen_k.py

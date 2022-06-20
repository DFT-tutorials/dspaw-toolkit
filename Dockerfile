FROM continuumio/anaconda

RUN conda install -c conda-forge -y requirements.txt

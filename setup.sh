#!/usr/bin/env bash

./install_environment.sh
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate vmp-proj
cd data
python download_vmp_data.py
cd ../matlab_toolboxes
python download_toolboxes.py
cd ../analysis
jupytext --to=ipynb *.py
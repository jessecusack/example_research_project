#!/usr/bin/env bash
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate vmp-proj && jupyter kernelspec uninstall vmp-proj && conda deactivate
conda remove --name vmp-proj --all
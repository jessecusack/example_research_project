# Example Research Project

Analysis of vmp data. To run this yourself, follow the instructions below.

## Requirements

* [Conda package manager](https://conda.io/en/latest/) (I recommend the lightweight version [miniconda](https://docs.conda.io/en/latest/miniconda.html))
* [MATLAB](https://www.mathworks.com/products/matlab.html)

## Installing the environment

Automatic setup is captured in the bash script `setup.sh`, which can be run in a terminal assuming the above requirements are fulfilled (macOS/Linux systems only!):

```bash
./setup.sh
```

You can also execute the steps manually in a terminal using the following instructions.

A conda environment is specified in `environment.yml` and may be install using the appropriate bash scripts (windows users, see the manual instructions at the bottom). 

To install:

```bash
./install_environment.sh
```

To remove:

```bash
./remove_environment.sh
```

These also install/remove the jupyter kernel for the environment.

> If these don't execute, you might need to change the file permissions with `chmod u+x *.sh`.

If you run in to problems, see the instructions for manual installation at the bottom.

After successfully installing the environment, activate it using: 

```bash
conda activate vmp-proj
```

Download the data by navigating to the `data/` and running:

```bash
python download_vmp_data.py
```

Download the MATLAB toolboxes by navigating to `matlab_toolboxes/` and execute

```bash
python download_toolboxes.py
```

## Project Structure
```
example_research_project/
    ├── README.md          <- The top-level README for people using this project.
    ├── data/
    │   ├── external       <- Data pulled in from outside of this project.
    │   ├── internal       <- Data generated within this project.
    │   └── README.md      <- Information on data sources and retrieval. 
    │
    ├── analysis/          <- Jupyter notebooks, MATLAB code and anything else that constitutes analysis.
    │   ├── README.md      <- Any information about the analysis, such as execution order. 
    │   ├── *.py           <- Python files that can be converted to notebooks using jupytext.
    │   └── *.m            <- Analysis in MATLAB.
    │
    ├── figures/           <- Saved figures generated during analysis.
    │
    ├── environment.yml    <- Conda environment specification. Install using the bash scripts.
    │
    ├── matlab_toolboxes/  <- A place for 3rd party MATLAB toolboxes.
    │   ├── toolbox/
    │   │
    │   └── get_toolbox.py <- Script to download toolboxes.
 ```

## Running the analysis

Within the `analysis/` directory you can:

* run `python analyse_vmp_profile.py` to execute the script (don't forget to `conda activate vmp-proj`!)
* convert the python script to a notebook with `jupytext --to=ipynb *.py` then open with Jupyter Lab/Notebook
* open up MATLAB and run `analyse_vmp_profile.m`.

Figures are saved to `figures/`.

## Manually installing the environment

If the bash scripts fail, open a terminal, navigate to this directory, and attempt the following:

```bash
conda env create -f environment.yml
conda activate vmp-proj
python -m ipykernel install --user --name vmp-proj
conda deactivate
```

To remove the kernel and environment:

```bash
conda activate vmp-proj
jupyter kernelspec uninstall vmp-proj
conda deactivate
conda remove --name vmp-proj --all
```

---

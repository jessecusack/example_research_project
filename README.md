# Example Research Project

Analysis of vmp data. To run this yourself, follow the instructions below.

## Requirements

* Python users: [Conda package manager](https://conda.io/en/latest/)
* MATLAB users: [MATLAB](https://www.mathworks.com/products/matlab.html)

## Python setup

Open a terminal, navigate to this directory and install the environment and kernel using:

```bash
conda env create -f environment.yml
conda activate vmp-proj
python -m ipykernel install --user --name vmp-proj
conda deactivate
```

Check that you can activate it again using: 

```bash
conda activate vmp-proj
```

With the environment active, download the data by navigating to the `data/` and running:

```bash
python download_vmp_data.py
```

Download the MATLAB toolboxes by navigating to `matlab_toolboxes/` and execute

```bash
python download_toolboxes.py
```

If you want to remove the environment and kernel later, see the instructions at the bottom.

Now you can proceed to the analysis.

## MATLAB setup

Open MATLAB and navigate to `data/`. Run the script to download the data.

Then navigate to `matlab_toolboxes/`. Run the script to download the toolboxes.

Now you can proceed to the analysis.

## Running the analysis

Within the `analysis/` directory you can:

* run `python analyse_vmp_profile.py` to execute the script (don't forget to `conda activate vmp-proj`!)
* convert the python script to a notebook with `jupytext --to=ipynb *.py` then open with Jupyter Lab/Notebook
* open up MATLAB and run `analyse_vmp_profile.m`.

Figures are saved to `figures/`.

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
    ├── environment.yml    <- Conda environment specification.
    │
    ├── matlab_toolboxes/  <- A place for 3rd party MATLAB toolboxes.
    │   ├── toolbox/
    │   ├── get_toolbox.m  <- Scripts to download toolboxes.
    │   └── get_toolbox.py
    │
    ├── setup_scripts/     <- Bash scripts for automatic setup.
    │   └── install.sh     <- Script to install something.
 ```

## Automatic setup

Automatic setup is captured in the bash script `setup_scripts/setup.sh`, which can be run in a terminal assuming the above requirements are fulfilled (macOS/Linux systems only!):

```bash
cd setup_scripts
./setup.sh
```

Note that this will download the data and toolboxes, as well as install the kernel and environment.

To install/remove the environment separately from the downloads, use the following scripts:

```bash
./install_environment.sh
```

or:

```bash
./remove_environment.sh
```

> If these don't execute, you might need to change the file permissions with `chmod u+x *.sh`.

If you run in to problems, see the instructions for manual setup above.

### Removing the environment

To remove the kernel and environment manually use:

```bash
conda activate vmp-proj
jupyter kernelspec uninstall vmp-proj
conda deactivate
conda remove --name vmp-proj --all
```

---

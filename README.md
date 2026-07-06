# PsrPopPySuper

This is the Python3 port for the PsrPopPy Package with added support for newwer electron density models and better output

# Prerequisites

- Python 3.8+
- gfortran compiler
- C compiler 

On macOS::

```shell
  brew install gcc
```

On Linux::
```shell
  sudo apt-get install gcc gfortran  # Ubuntu/Debian
  sudo yum install gcc gcc-gfortran   # CentOS/RHEL
```

## Installation



```bash
# for installing the latest dev version
git clone -b dev  https://github.com/HIGGS317/PsrPopPySuper 
cd PsrPopPySuper
```

### With Conda

Use the [environment.yml](environment.yml) to make the conda environment and activate it

```bash
conda create --file environment.yml --name PsrPopPySuper
conda activate PsrpoppySuper
```
Replace PsrPopPySuper with your own preferred name of the environment
```bash
pip install -e .
```

### Without Conda

Before moving on without conda ensure you have python version 3.11+ and have install c and fortran compiler.

```bash
cd PsrPopPySuper
pip install -r requirements.txt
pip install -e .
```


## Usage

```python
import psrpoppysuper
```

or, following the below example you could do:

```python
  from psrpoppysuper import evolve,dosurvey

  evolution = evolve.generate(ngen=1269,
            age_max=1.0E+9,
            birthVModel='exp',
            birthVPars=[0,380],
            electronModel='ne2001',
            bFieldPars=[12.35,0.55],
            lumDistType='fk06',
            lumDistPars=[-1.5,0.5],
            pDistPars=[0.3,0.15],
            braking_index=3
  )

  survey = dosurvey.run(evolution,surveyList=['LOFAR'])

  dosurvey.write(survey,asc=True,extension=f'{i}.results')
```

Usage
=====

If not installing the package via `pip install ` I'd recommend adding the `psrpoppy` directory to your PYTHONPATH and adding the `bin` directory to your PATH. This should then leave you set up to run the code from wherever you like.


A brief description of the "executables" follows.

populate
--------

Create a population mode using user-defined parameters using the snapshot method

evolve
------

Create a populate model using the Ridley & Lorimer evolution method

dosurvey 
--------

Run a population model through a survey. Pre-defined surveys are given, but a user may also create their own.


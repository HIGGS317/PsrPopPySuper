# **This is the Python3 port for the PsrPopPy Package**

## **This comes with a file to set up conda virtual environments for ease of use**

## **Please report back any issue to the github issue page if and only if you have used this port**

Use [environment.yml](environment.yml) file to set up a conda virtual environment with all the required dependencies. Then you can follow the rest of the README as normal.

>[!CAUTION]
>This port is still in development, and there may be issues that are not addressed. Use at your own risk.

PsrPopPy
========

(For full documentation, see http://samb8s.github.com/PsrPopPy/ or manual.pdf)

Python implementation of PSRPOP (which was written by D Lorimer).
Several of the old models from that (e.g. NE2001) are still included in their native fortran, since re-writing those is beyond the scope of this work. Currently, only a rudimentary makefile is included. This is something that needs work from a willing volunteer!

The main external requirements are [matplotlib](matplotlib.sourceforge.net) and [wxPython](http://wxpython.org/), which are used for the visualization stuff. It has a very useful API for making simple GUIs, as well as making beautiful plots. I've had difficulty compiliing wxPython from scratch on more recent versions of Mac OS X, but it should be straightforward to install via macports or similar.

Thanks
------

Many thanks to recent suggestions from Manjari Bagchi and Anirban Chakraborty. Their work https://arxiv.org/abs/2012.13243 used PsrPopPy, and they found some issues which I've been happy to correct.

If you spot any issues, please either let me know, or make a pull request - I'm not actively developing the code anymore, but I'm happy to keep it reasonably maintained.

Dev Notes
---------

I've just added scintillation effects to `dosurvey`! They can be switched on by adding the
flag --scint, but are off by default. The code uses equations from Lorimer & Kramer and 
the NE2001 code to calculate modulation indices for pulsars in the population. The S/N of each
pulsar is then scaled up or down using the modulation index.

Compiling
---------

The package now supports automatic Fortran compilation during installation.
Simply run::

  pip install .

This will automatically compile the Fortran libraries using gfortran and install
the package. Make sure gfortran is installed on your system first.

For manual compilation (legacy method), see the documentation.

## Installation

```bash
git clone https://github.com/HIGGS317/PsrPopPySuper
cd PsrPopPySuper
pip install .
```

### Prerequisites

- Python 3.8+
- gfortran compiler

On macOS::

  brew install gcc

On Linux::

  sudo apt-get install gfortran  # Ubuntu/Debian
  sudo yum install gcc-gfortran   # CentOS/RHEL
```
```bash
cd PsrPoPySuper
```

Use the [environment.yml](environment.yml) to make the conda environment and activate it

```bash
pip install -e .
```


## Usage

```python
import psrpoppy
```

or, following [this example](examples/populate_and_survey.py), you could do:

```python
from psrpoppy import populate

pop = populate.generate(1038, 
                        surveyList=['PMSURV'],
                        radialDistType='lfl06',
                        siDistPars=[-1.41, 0.96], # non-standard SI distribution
                        duty_percent=6.,
                        electronModel='lmt85',
                        nostdout=True # switches off output to stdout
                       )
```

Usage
=====

If not installing the package via `pip install .` I'd recommend adding the `psrpoppy` directory to your PYTHONPATH and adding the `bin` directory to your PATH. This should then leave you set up to run the code from wherever you like.


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

wxView
------

More detailed population model viewer. Make histograms, scatter plots, etc. All based off the wx backend for matplotlib.

wxHist
------

Make more intricate histograms, including histograms of multiple population models.

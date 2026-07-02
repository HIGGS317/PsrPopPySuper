.. _installation:

************
Installation
************

To get started with PsrPopPySuper there are a few steps you'll need to 
go through.

PsrPopPySuper is currently supported on Linux and Mac OS X, and for
full feature support, it is recommended to install the 
`Matplotlib <http://matplotlib.org/>`_ package and either use
Python versions >3.11, or install the argparse module.

.. _download_package:

Download the package
====================
The source for PsrPopPy can be downloaded from `GitHub <http://github.com>`_ 
from the `PsrPopPy page <https://github.com/samb8s/PsrPopPy>`_.
The source will contain the Python modules and scripts needed both for
basic and advanced use.

.. _installing_package:

Installing the package
======================
PsrPopPy now supports standard Python package installation using pip.
This automatically handles the Fortran compilation and installation.

Prerequisites
-------------
- Python 3.11 or later
- gfortran compiler (for Fortran library compilation)

On macOS, install gfortran using Homebrew::

  brew install gcc

On Linux, install gfortran using your package manager::

  # Ubuntu/Debian
  sudo apt-get install gfortran

  # CentOS/RHEL/Fedora
  sudo yum install gcc-gfortran  # or dnf install gcc-gfortran

Installation
------------
If you want to install PsrPopPySuper in isolation, it is recommended 
to use a virtual conda environment. You can create one using conda.

Use the providede environment.yml to make the conda environment and activate it::


  conda create --file environment.yml
  conda activate PsrpoppySuper



After creating and activating the conda environment, navigate to the source directory and run::

  pip install -e .

This will:

-  Compile the Fortran and C libraries using gfortran and gcc
-  Install the Python package
-  Install command-line scripts (dosurvey, populate, evolve)

.. For development or user installation::

..   pip install -e .  # editable install
..   pip install --user .  # user install

.. _legacy_compiling_fortran:

Legacy Fortran Compilation (if needed)
======================================
Although PsrPopPySuper is a Python-based package, some of the algorithms
have been kept in their native FORTRAN for speed and ease of
programming (e.g. the NE2001 electron model, coordinate conversion...).
The pip installation now handles this automatically, but if you need
to compile manually:

From the base directory::

  cd psrpoppy/fortran

To use ``make``, edit ``makefile.<OSTYPE>`` and ensure that the gf variable
points to the location of your gfortran compiler. Then simply type ``make``.
All being well, four .so files will be generated.

Failing this, edit either ``make_mac.sh`` or ``make_linux.sh``, depending upon
your system, so that the ``gf`` variable points to your local gfortran/f77
compiler. Running the script::

  bash make_<os>.sh
  
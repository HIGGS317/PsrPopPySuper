import glob
import os

__dir__ = os.path.dirname(os.path.abspath(__file__))


def find_library(name):
    """Return a library path for a shared library in psrpoppy/fortran."""
    if name.endswith(('.so', '.dylib', '.dll')):
        name = os.path.splitext(name)[0]

    exact = os.path.join(__dir__, f'{name}.so')
    if os.path.exists(exact):
        return exact

    # Accept platform-specific compiled extension suffixes like
    # libgamma.cpython-311-darwin.so or libgamma.dylib.
    candidates = []
    for ext in ('so', 'dylib', 'dll'):
        candidates.extend(glob.glob(os.path.join(__dir__, f'{name}*.{ext}')))

    if candidates:
        return sorted(candidates)[0]

    raise FileNotFoundError(
        f'Fortran library {name} not found in {__dir__}. '
        'Build the package with gfortran and rerun pip install.'
    )

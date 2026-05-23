#!/usr/bin/env python
import os
import sys
import shutil
import subprocess
from pathlib import Path

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py as _build_py

HERE = Path(__file__).resolve().parent
PKG_NAME = "PsrPopPySuper"
FORTRAN_DIR = HERE / PKG_NAME / "fortran"

LIBRARIES = {
    "libne2001": ["ne2001.f", "dm.f", "psr_ne.f", "dist.f", "calc_xyz.f", "density.f", "glun.f"],
    "libne2025": ["ne2025.f", "dm.f", "psr_ne.f", "dist.f", "calc_xyz.f", "density.f", "glun.f"],
    "libykarea": ["ykarea.f", "psrran.f"],
    "libsla": ["galtfeq.f", "sla.f"],
    "libvxyz": ["vxyz.f", "rkqc.f", "rk4.f"],
    "libgamma": ["gamma.f"],
    "libgetseed": ["getseed.f", "clock.f"],
}


def find_gfortran():
    f90 = os.environ.get("F90") or shutil.which("gfortran")
    if f90:
        return f90

    candidates = [
        "/opt/homebrew/bin/gfortran",
        "/usr/local/bin/gfortran",
        "/usr/bin/gfortran",
        os.path.expanduser("~/miniforge3/bin/gfortran"),
        os.path.expanduser("~/miniforge3/envs/Psrpoppy/bin/gfortran"),
    ]
    for candidate in candidates:
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate

    return None


def build_fortran_library(libname, sources, compiler):
    if sys.platform == "darwin":
        suffix = ".dylib"
        flags = ["-dynamiclib", "-undefined", "dynamic_lookup"]
    else:
        suffix = ".so"
        flags = ["-shared", "-fPIC"]

    target = FORTRAN_DIR / f"{libname}{suffix}"
    if target.exists():
        return

    command = [compiler] + flags + ["-o", str(target)] + [str(FORTRAN_DIR / s) for s in sources]
    subprocess.check_call(command, cwd=str(FORTRAN_DIR))


def build_fortran_libraries(compiler):
    for libname, sources in LIBRARIES.items():
        build_fortran_library(libname, sources, compiler)


class BuildPyCommand(_build_py):
    def run(self):
        gfortran = find_gfortran()
        if not gfortran:
            sys.exit(
                "ERROR: gfortran not found. Install it with brew install gcc, conda install -c conda-forge gfortran,"
                " or add gfortran to PATH before running pip install."
            )

        build_fortran_libraries(gfortran)
        super().run()


def read_long_description():
    readme_path = HERE / "README.md"
    if readme_path.exists():
        return readme_path.read_text(encoding="utf-8")
    return ""


setup(
    name="PsrPopPySuper",
    version="1.0.0",
    description="Python3 port of PsrPopPy",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="Divyansh Tripathi",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "psrpoppysuper": [
            "fortran/**",
            "models/**",
            "surveys/**",
        ]
    },
    install_requires=["numpy"],
    entry_points={
        "console_scripts": [
            "dosurvey=psrpoppysuper.dosurvey:main",
            "populate=psrpoppysuper.populate:main",
            "evolve=psrpoppysuper.evolve:main",
        ]
    },
    python_requires=">=3.8",
    zip_safe=False,
    cmdclass={"build_py": BuildPyCommand},
)

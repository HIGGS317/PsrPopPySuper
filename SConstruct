# Starter SConstruct for enscons

import sys
import os
import toml as toml
import enscons
from SCons.Script import AddOption, Environment, GetOption, Exit
import glob
# from enscons import find_source_files
# from SCons.Node.FS import Glob

# check if prefix is set
AddOption('--prefix', dest='prefix', type='string', nargs=1,
          action='store', metavar='DIR', default='/usr/local',
          help='Installation Prefix')

AddOption('--user', dest='user', action='store_true', default=False,
          help='Install as pip-like "--user" (this overrides "--prefix")')

metadata = dict(toml.load(open('pyproject.toml')))['tool']['enscons']

full_tag = enscons.get_binary_tag()

# full_tag = py2.py3-none-any # pure Python packages compatible with 2+3

# env = Environment(tools=['default', 'packaging', enscons.generate],
#                    PACKAGE_METADATA=metadata,
#                    WHEEL_TAG=full_tag)

env = Environment(ENV=os.environ,tools=['default', 'packaging', enscons.generate],
                  PACKAGE_METADATA=metadata,
                    WHEEL_TAG=full_tag)


# # set the compiler to gfortran
# env['F90'] = 'gfortran'

if env.Detect('gfortran'):
    env['F90'] = env.WhereIs('gfortran') or 'gfortran'
else:
    # Try common locations (Homebrew/conda/etc)
    candidates = [
        '/opt/homebrew/bin/gfortran',
        '/usr/local/bin/gfortran',
        '/usr/bin/gfortran',
        os.path.expanduser('~/miniforge3/bin/gfortran'),
        os.path.expanduser('~/miniforge3/envs/Pulsar/bin/gfortran'),
    ]
    for c in candidates:
        if os.path.exists(c) and os.access(c, os.X_OK):
            env['F90'] = c
            break
    else:
        print('ERROR: gfortran not found. Install it (brew install gcc or conda install -c conda-forge gfortran) or add it to PATH.')
        Exit(1)
py_source = glob.glob('psrpoppy/*.py')

libpath = os.path.join('psrpoppy', 'fortran')

# check whether installing on a Mac
if 'Darwin' in os.uname()[0]:
    env.Append(CFLAGS=['-m 32'])
    env.Append(CPPFLAGS=['-dynamiclib', '-O2', '-fPIC', '-fno-second-underscore', '-c', '-std=legacy'])

env.Append(CPPPATH=[libpath])

# dictionary of libraries and files needed for library
LIBDIC = {}
#LIBDIC['libne2001']  = ['ne2001.f', 'dm.f', 'psr_ne.f', 'dist.f', 'calc_xyz.f', 'density.f', 'glun.f']
LIBDIC['libne2025']  = ['ne2025.f', 'dm.f', 'psr_ne.f', 'dist.f', 'calc_xyz.f', 'density.f', 'glun.f']
LIBDIC['libykarea']  = ['ykarea.f', 'psrran.f']
LIBDIC['libsla']     = ['galtfeq.f', 'sla.f']
LIBDIC['libvxyz']    = ['vxyz.f', 'rkqc.f', 'rk4.f']
LIBDIC['libgamma']   = ['gamma.f']
LIBDIC['libgetseed'] = ['getseed.f', 'clock.f']

libs = []

# compile libraries
for libname in LIBDIC:
    lib = os.path.join(libpath, libname)
    libsources = [os.path.join(libpath, srcfile) for srcfile in LIBDIC[libname]]
    
    sharedlib = env.SharedLibrary(target=lib, source=libsources)
    #staticlib = env.StaticLibrary(target=lib, source=libsources)

    libs += sharedlib

# install prefix
# If the user requested a per-user install, honour that. Otherwise prefer
# installing into the active Python interpreter's prefix (this makes
# installs go into the active conda/venv environment instead of system
# locations like /usr/local which require root).
if GetOption('user'):
    installprefix = os.path.join(os.environ['HOME'], '.local')
else:
    installprefix = sys.prefix
pyprefix='psrpoppy'
executables = ['dosurvey', 'evolve', 'populate']

# install executables
insbins = env.InstallAs(target=[os.path.join(installprefix, 'bin', ex) for ex in executables],
               source=[os.path.join(pyprefix, ex+'.py') for ex in executables])

otherfiles = glob.glob('psrpoppy/fortran/*.so') + glob.glob('psrpoppy/fortran/lookuptables/*') + glob.glob('psrpoppy/models/*') + glob.glob('psrpoppy/surveys/*')+glob.glob('psrpoppy/fortran/NE_2001/*')

platlib = env.Whl('platlib', py_source + libs + otherfiles, root='')
whl = env.WhlFile(source=platlib)

# Add automatic source files, plus any other needed files.
sdist_source=list(set(
                  glob.glob('psrpoppy/fortran/*.f') + glob.glob('psrpoppy/fortran/*.inc') + glob.glob('psrpoppy/fortran/lookuptables/*') + glob.glob('psrpoppy/models/*') + glob.glob('psrpoppy/surveys/*')+glob.glob('psrpoppy/fortran/NE_2001/*')))

sdist_source += py_source

sdist = env.SDist(source=sdist_source)
env.Alias('sdist', sdist)

if GetOption('user'):
    # Install in user site (same as pip --user)
    install_cmd = ' '.join([sys.executable, '-m', 'pip', 'install', '--no-deps', '--user', '$SOURCE'])
else:
    # Install into the active interpreter's environment (conda/venv). Do
    # not pass --user so pip installs into sys.prefix site-packages.
    install_cmd = ' '.join([sys.executable, '-m', 'pip', 'install', '--no-deps', '$SOURCE'])

install = env.Command("#DUMMY", whl, install_cmd)
env.Alias('install', install + insbins)
env.AlwaysBuild(install + insbins)

env.Default(sdist)


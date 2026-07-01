evolve.py
=========
.. program:: evolve.py

.. cmdoption:: -n <number of pulsars>

   Required: Number of pulsars to generate or detect

.. cmdoption:: -o <output>

   Output file name for population model (def=evolve.model)

.. cmdoption:: -asc <ascii output file name>

   Output file name for ascii output file (def=None)

.. cmdoption:: -surveys <SURVEY NAME(S)>

   List of surveys to use when trying to detect pulsars (default=None)

.. cmdoption:: -dm <Electron model>

   Model to describe the Galactic electron distribution

   Supported: 'ne2025', , 'ne2001', 'ymw16'

.. cmdoption:: -tmax <max age>

   Maximum initial age of pulsars, in years (def=1.0E9)

.. cmdoption:: -p <mean stddev>

   Period distribution mean and standard deviation, seconds (def=0.3, 0.15)

.. cmdoption:: -ldist <distribution>

   Distribution to use for luminosities

   Supported: 'fk06', 'lnorm', 'pow'

.. cmdoption:: -l <parameters>

   Luminosity distribution parameters (def=-1.5, 0.5)

.. cmdoption:: -b <mean stddev>

   Mean and standard deviation of log-normal B field distribution (Gauss, def=12.65, 0.55)

.. cmdoption:: -vmodel <model>

   Velocity model to use

   Supported: 'gaussian', 'exp'

.. cmdoption:: -v <mean stddev>

   Velocity distribution values (def=0, 180 km/s)

.. cmdoption:: -si <mean stddev>

   Spectral index mean and standard deviation (def=-1.4, 0.96)

.. cmdoption:: -spinmodel <model>

   Spin-down model to employ

   Supported: 'fk06', 'cs06'

.. cmdoption:: -alignmodel <model>

   Pulsar alignment model to use

   Supported: 'orthogonal', 'random', 'rand45', 'wj08'

.. cmdoption:: -aligntime <time>

   Alignment timescale (def=None)

.. cmdoption:: -beammodel <model>

   Beaming model to use (def=tm98)

   Supported: 'tm98', 'none', 'const', 'wj08'

.. cmdoption:: -w <width>

   Pulse width to use when generating pulsars, percent (def=5.0)

.. cmdoption:: -wmod <width model>

   Pulse width model to use

   Supported: None, 'kj07'

.. cmdoption:: -sc <scatter index>

   Spectral index of scattering law to use (def=-3.86)

.. cmdoption:: -eff <efficiency cutoff>

   Efficiency cutoff value (def=None)

.. cmdoption:: -z <scale height>

   Exponential z-scale height for the population, in kpc (def=0.05)

.. cmdoption:: -bi <braking index>

   Braking index value to use (def=0 = model default)

.. cmdoption:: --nostdout

   Turn off writing to stdout.

.. cmdoption:: --nodeathline

   Turn off the deathline.

.. cmdoption:: --nospiralarms

   Turn off spiral arms galactic distribution.

.. cmdoption:: --keepdead

   Keep dead pulsars in the population model.

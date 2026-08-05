
dosurvey.py
===========
.. program:: dosurvey.py

.. cmdoption:: -f <filename>

   Input population model to use (default=populate.model)

.. cmdoption:: -surveys <SURVEY NAME(S)>

   Required: Name(s) of surveys to simulate on the population model

.. cmdoption:: --noresults

   By default, a .results file is written, containing a model of the population
   detected in the survey. This option switches off the writing of this file.

.. cmdoption:: --asc

   Write the survey model in plain ascii (psrpop old style). Not recommended, 
   since the cPickle '.results' file is easier to work with.

.. cmdoption:: -wS <surveyed ascii output file name>

   Write the surveyed ASCII population to a file. This option requires the
   ``-surveys`` (or ``-survey``) argument and is the preferred way to output
   survey-detected pulsars in ascii format.

.. cmdoption:: --summary

   Write a short .summary file (per survey) describing number of detections,
   number of pulsars outside survey area, number smeared, and number not beaming

.. cmdoption:: --nostdout

   Turn off writing to stdout. Useful for many iterations eg. in large simulations

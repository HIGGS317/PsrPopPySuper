:mod:`evolve` -- Evolve a pulsar population object
=================================================
.. module:: evolve
   :synopsis: Evolve a pulsar population model
.. moduleauthor:: Sam Bates <sam.d.bates@gmail.com>

.. class:: EvolveException

.. function:: generate(ngen, surveyList=None, age_max=1.0E9, pDistPars=[.3, .15], bFieldPars=[12.65, 0.55], birthVPars=[0.0, 180.], siDistPars=[-1.6, 0.35], alignModel='orthogonal', lumDistType='fk06', lumDistPars=[-1.5, 0.5], alignTime=None, spinModel='fk06', beamModel='tm98', birthVModel='gaussian', electronModel='ne2025', braking_index=0, zscale=0.05, duty=5., scindex=-3.86, widthModel=None, nodeathline=False, efficiencycut=None, nostdout=False, nospiralarms=False, keepdead=False, ascfile=None, write_global=None, write_surveyed=None)

   Generate an evolved pulsar population model.

   The optional ``write_global`` argument writes the full generated population
   to an ASCII file. The optional ``write_surveyed`` argument writes the
   survey-detected subset to ASCII and requires ``surveyList`` to be set.

.. function:: main()

   Entry point for the evolve console script.

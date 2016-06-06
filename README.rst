===============================
JSBSim Manager
===============================

.. image:: https://img.shields.io/pypi/v/jsbsim_manager.svg
        :target: https://pypi.python.org/pypi/jsbsim_manager

.. image:: https://img.shields.io/travis/open-aerospace/jsbsim-manager.svg
        :target: https://travis-ci.org/open-aerospace/jsbsim-manager

.. image:: https://requires.io/github/open-aerospace/jsbsim-manager/requirements.svg?branch=master
        :target: https://requires.io/github/open-aerospace/jsbsim-manager/requirements?branch=master
        :alt: Dependencies


Manager for JSBSim case files and support for running simulations in parallel

* Free software: GNU General Public License v3

JSBSim Manager Features
-----------------------

 - Automate the writing of JSBSim XML configuration files
 - Automate running JSBSim instances in parallel


JSBSim (What Is It?)
--------------------

JSBSim is a free, open source aerospace simulation framework written in c++. It's a fully featured "Flight Dynamics Model" (FDM). An FDM is essentially the physics/math model that defines the movement of an aircraft, rocket, etc., under the forces and moments applied to it using the various control mechanisms and from the forces of nature. In other words, given the mass, size, shape, thrust, and aerodynamic coefficients of some object like a rocket it will faithfully simulate that object's movement.

JSBSim can be installed as a stand-alone simulation engine, but it expects a lot of XML files as input. They describe everything from the vehicle being simulated, to initial conditions and environmental variables like wind.

**JSBSim Manager** is a python module for automating the writing of these XML configuration files and running JSBSim efficiently in parallel. This is especially useful when you want to run thousands of simulations in a Monte-Carlo scheme.

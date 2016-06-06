# -*- coding: utf-8 -*-


class RunManager(object):
    """Run a JSBSim instance for a case

    :param Case case: A JSBSim Case object to build into a file structure and run.

    """

    def __init__(self, case):
        self.case = case


class Case(object):
    """Information that makes up a JSBSim case. The usual JSBSim runtime
    directory should look like this::

        .
        ├── aircraft
        │   └── rocket
        │       ├── init.xml
        │       └── rocket.xml
        ├── engine
        │   ├── motor_nozzle.xml
        │   └── motor.xml
        ├── output.xml
        └── run.xml


    Aircraft and Engine data can either be existing XML files, or an
    `openrocketdoc` document. Initial conditions, output file definitions, and
    the run files are described by this class.
    """

    def __init__(self):
        pass

# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


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

    def _append_unit_element(self, parent, element, units, value):
        e = ET.SubElement(parent, element)
        e.attrib['unit'] = units
        e.text = "%f" % value

    def initial_conditions(self,
                           ubody=0,
                           vbody=0,
                           wbody=0,
                           phi=0,
                           theta=0,
                           psi=0,
                           altitude=0,
                           latitude=0,
                           longitude=0,
                           elevation=0):
        """Set the initial conditions for the simulation.
        """

        # initial conditions document:
        init_doc = ET.Element('initialize')
        init_doc.attrib['name'] = "Initial Conditions"

        # NED velocity vector:
        self._append_unit_element(init_doc, 'ubody', 'M/SEC', ubody)
        self._append_unit_element(init_doc, 'vbody', 'M/SEC', vbody)
        self._append_unit_element(init_doc, 'wbody', 'M/SEC', wbody)

        # Rotation:
        self._append_unit_element(init_doc, 'phi', 'DEG', phi)
        self._append_unit_element(init_doc, 'theta', 'DEG', theta)
        self._append_unit_element(init_doc, 'psi', 'DEG', psi)

        # Altitude AGL:
        self._append_unit_element(init_doc, 'altitude', 'M', altitude)

        # Earth position:
        self._append_unit_element(init_doc, 'latitude', 'DEG', latitude)
        self._append_unit_element(init_doc, 'longitude', 'DEG', longitude)
        self._append_unit_element(init_doc, 'elevation', 'M', elevation)

        # Pretty print XML Document
        xmldoc = minidom.parseString(ET.tostring(init_doc, encoding="UTF-8"))
        return xmldoc.toprettyxml(indent="  ")

# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


class RunManager(object):
    """Run a JSBSim instance for a case

    :param Case case: A JSBSim Case object to build into a file structure and run.

    """

    def __init__(self, case):
        self.case = case


class JSBSimWriter(object):
    """A Writing class for JSBSim XML
    """

    def _append_unit_element(self, parent, element, units, value):
        e = ET.SubElement(parent, element)
        e.attrib['unit'] = units
        e.text = "%f" % value

    @property
    def document(self):
        """Return an XML document (`str`)"""
        root_element = self._document()
        xmldoc = minidom.parseString(ET.tostring(root_element, encoding="UTF-8"))
        return xmldoc.toprettyxml(indent="  ")


class InitialConditions(JSBSimWriter):
    """Store initial conditions document
    """

    def __init__(self,
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
        self.ubody = ubody
        self.vbody = vbody
        self.wbody = wbody
        self.phi = phi
        self.theta = theta
        self.psi = psi
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def _document(self):

        init_doc = ET.Element('initialize')
        init_doc.attrib['name'] = "Initial Conditions"

        # NED velocity vector:
        self._append_unit_element(init_doc, 'ubody', 'M/SEC', self.ubody)
        self._append_unit_element(init_doc, 'vbody', 'M/SEC', self.vbody)
        self._append_unit_element(init_doc, 'wbody', 'M/SEC', self.wbody)

        # Rotation:
        self._append_unit_element(init_doc, 'phi', 'DEG', self.phi)
        self._append_unit_element(init_doc, 'theta', 'DEG', self.theta)
        self._append_unit_element(init_doc, 'psi', 'DEG', self.psi)

        # Altitude AGL:
        self._append_unit_element(init_doc, 'altitude', 'M', self.altitude)

        # Earth position:
        self._append_unit_element(init_doc, 'latitude', 'DEG', self.latitude)
        self._append_unit_element(init_doc, 'longitude', 'DEG', self.longitude)
        self._append_unit_element(init_doc, 'elevation', 'M', self.elevation)

        return init_doc


DEFAULT_INIT = InitialConditions()


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

    def __init__(self, run_conditions, init=DEFAULT_INIT, output_list=[]):
        self.init_doc = init.document
        self.outputs = output_list
        self.run_conditions = run_conditions

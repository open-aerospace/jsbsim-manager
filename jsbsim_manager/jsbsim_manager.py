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


class Output(JSBSimWriter):
    """Store output file
    """

    def __init__(self, outtype, destination, datarate, prop_list, port=5123):
        self.outtype = outtype
        self.destination = destination
        self.datarate = datarate
        self.prop_list = prop_list
        self.port = port

    def _document(self):

        out_doc = ET.Element('output')
        out_doc.attrib['name'] = self.destination
        out_doc.attrib['rate'] = "%f" % self.datarate

        if self.outtype.lower() == 'csv' or self.outtype.lower() == 'file':
            out_doc.attrib['type'] = "CSV"

        if self.outtype.lower() == 'udp':
            out_doc.attrib['type'] = "SOCKET"
            out_doc.attrib['protocol'] = "UDP"
            out_doc.attrib['port'] = "%d" % self.port

        for prop in self.prop_list:
            p = ET.SubElement(out_doc, 'property')
            p.attrib['caption'] = prop[0]
            p.text = prop[1]

        return out_doc


DEFAULT_INIT = InitialConditions()
"""A pre-built default initial conditions:

* Latitude, Longitude = Null Island (00.0, 000.0)
* ECEF velocity: 0
* Altitude: 0
* Attitude: roll/pitch/yaw = 0 (X pointed North)
"""


# Easy handler for JSBSim properites
PROPERTIES = {
    'altitudeMSL': ("Altitude MSL [m]", "position/h-sl-meters"),
    'rollaccel': ("Roll Acceleration [rad/s2]", "accelerations/pdot-rad_sec2"),
    'pitchaccel': ("Pitch Acceleration [rad/s2]", "accelerations/qdot-rad_sec2"),
    'yawaccel': ("Yaw Acceleration [rad/s2]", "accelerations/rdot-rad_sec2"),
    'accelX': ("Acceleration X [ft/s2]", "accelerations/udot-ft_sec2"),
    'accelY': ("Acceleration Y [ft/s2]", "accelerations/vdot-ft_sec2"),
    'accelZ': ("Acceleration Z [ft/s2]", "accelerations/wdot-ft_sec2"),
    'gravity': ("Acceleration X [ft/s2]", "accelerations/gravity-ft_sec2"),
    'forcesX': ("Forces X [lbf]", "forces/fbx-total-lbs"),
    'forcesY': ("Forces Y [lbf]", "forces/fby-total-lbs"),
    'forcesZ': ("Forces Z [lbf]", "forces/fbz-total-lbs"),
    'momentsl': ("Moments L [lbf*ft]", "moments/l-total-lbsft"),
    'momentsM': ("Moments M [lbf*ft]", "moments/m-total-lbsft"),
    'momentsN': ("Moments N [lbf*ft]", "moments/n-total-lbsft"),
    'qbar': ("Aero QBar [psf]", "aero/qbar-psf"),
    'downrange': ("Downrange [mt]", "position/distance-from-start-mag-mt"),
    'mass': ("Mass [lbs]", "inertia/weight-lbs"),
    'velNorth': ("Velocity North [fps]", "velocities/v-north-fps"),
    'velEast': ("Velocity East [fps]", "velocities/v-east-fps"),
    'velDown': ("Velocity Down [fps]", "velocities/v-down-fps"),
    'velX': ("Velocity X [fps]", "velocities/u-fps"),
    'velY': ("Velocity Y [fps]", "velocities/v-fps"),
    'velZ': ("Velocity Z [fps]", "velocities/w-fps"),
    'velECI_X': ("Velocity ECI X [fps]", "velocities/eci-x-fps"),
    'velECI_Y': ("Velocity ECI Y [fps]", "velocities/eci-y-fps"),
    'velECI_Z': ("Velocity ECI Z [fps]", "velocities/eci-z-fps"),
    'velECI': ("Velocity Magnitude ECI [fps]", "velocities/eci-velocity-mag-fps"),
    'latitude': ("Latitude [deg]", "position/lat-gc-deg"),
    'longitude': ("Latitude [deg]", "position/long-gc-deg"),
    'altitudeAGL': ("Altitude AGL [km]", "position/h-agl-km"),
    'positionECI_X': ("Position ECI X", "position/eci-x-ft"),
    'positionECI_Y': ("Position ECI Y", "position/eci-y-ft"),
    'positionECI_Z': ("Position ECI Z", "position/eci-z-ft"),
    'positionECEF_X': ("Position ECEF X", "position/ecef-x-ft"),
    'positionECEF_Y': ("Position ECEF Y", "position/ecef-y-ft"),
    'positionECEF_Z': ("Position ECEF Z", "position/ecef-z-ft"),
    'roll': ("Roll [deg]", "attitude/phi-deg"),
    'pitch': ("Pitch [deg]", "attitude/theta-deg"),
    'yaw': ("Yaw [deg]", "attitude/psi-deg"),
}


DEFAULT_OUTPUT = Output('csv', "simulation_data.csv", 100, [
    PROPERTIES['altitudeMSL'],
])


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

    def __init__(self, run_conditions, init=DEFAULT_INIT, output_list=[DEFAULT_OUTPUT]):
        self.init_doc = init.document
        self.outputs = output_list
        self.run_conditions = run_conditions

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jsbsim_manager
----------------------------------

Tests for `jsbsim_manager` module.
"""


import sys
import unittest
import xml.etree.ElementTree as ET

from jsbsim_manager import jsbsim_manager


class TestJsbsim_manager(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_smoke(self):
        # Really simple smoke test
        case = jsbsim_manager.Case(None)
        runner = jsbsim_manager.RunManager(case)
        self.assertEqual(type(runner), jsbsim_manager.RunManager)

    def test_init_default(self):
        # Pure default values
        init = jsbsim_manager.InitialConditions()

        # unwrap XML
        initialize = ET.fromstring(init.document)
        self.assertEqual(initialize.tag, 'initialize')
        for element in initialize:
            if element.tag == 'ubody':
                self.assertEqual(element.get("unit"), "M/SEC")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'vbody':
                self.assertEqual(element.get("unit"), "M/SEC")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'wbody':
                self.assertEqual(element.get("unit"), "M/SEC")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'phi':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'theta':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'psi':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'altitude':
                self.assertEqual(element.get("unit"), "M")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'latitude':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'longitude':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'elevation':
                self.assertEqual(element.get("unit"), "M")
                self.assertAlmostEqual(float(element.text), 0.0)
            else:
                # Should not get here
                self.fail("Unrecognised element in initial conditions doc")

    def test_init_override(self):
        # Use non-default values for vbody and latitude
        init = jsbsim_manager.InitialConditions(vbody=2.5, latitude=45.0)

        # unwrap XML
        initialize = ET.fromstring(init.document)
        self.assertEqual(initialize.tag, 'initialize')
        for element in initialize:
            if element.tag == 'ubody':
                self.assertEqual(element.get("unit"), "M/SEC")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'vbody':
                self.assertEqual(element.get("unit"), "M/SEC")
                self.assertAlmostEqual(float(element.text), 2.5)
            elif element.tag == 'wbody':
                self.assertEqual(element.get("unit"), "M/SEC")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'phi':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'theta':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'psi':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'altitude':
                self.assertEqual(element.get("unit"), "M")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'latitude':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 45.0)
            elif element.tag == 'longitude':
                self.assertEqual(element.get("unit"), "DEG")
                self.assertAlmostEqual(float(element.text), 0.0)
            elif element.tag == 'elevation':
                self.assertEqual(element.get("unit"), "M")
                self.assertAlmostEqual(float(element.text), 0.0)
            else:
                # Should not get here
                self.fail("Unrecognised element in initial conditions doc")

    def test_out_csv(self):
        out = jsbsim_manager.Output('File', "filename", 20, [])

        # unwrap XML
        output = ET.fromstring(out.document)
        self.assertEqual(output.tag, 'output')
        self.assertEqual(output.get("type"), "CSV")
        self.assertEqual(output.get("name"), "filename")
        self.assertAlmostEqual(float(output.get("rate")), 20)

        # No output fields.
        self.assertEqual([e for e in output], [])

    def test_out_UDP(self):
        out = jsbsim_manager.Output('UDP', "localhost", 20, [])

        # unwrap XML
        output = ET.fromstring(out.document)
        self.assertEqual(output.tag, 'output')
        self.assertEqual(output.get("type"), "SOCKET")
        self.assertEqual(output.get("protocol"), "UDP")
        self.assertEqual(output.get("name"), "localhost")
        self.assertEqual(int(output.get("port")), 5123)
        self.assertAlmostEqual(float(output.get("rate")), 20)

        # No output fields.
        self.assertEqual([e for e in output], [])

    def test_out_csv_fields(self):
        out = jsbsim_manager.Output('File', "filename", 20, [
            jsbsim_manager.PROPERTIES['altitudeMSL'],
            ("Velocity Down [fps]", "velocities/v-down-fps"),
        ])

        # unwrap XML
        output = ET.fromstring(out.document)
        self.assertEqual(output.tag, 'output')
        self.assertEqual(output.get("type"), "CSV")
        self.assertEqual(output.get("name"), "filename")
        self.assertAlmostEqual(float(output.get("rate")), 20)

        # output fields.
        self.assertEqual(len(output), 2)
        self.assertEqual(output[0].get("caption"), "Altitude MSL [m]")
        self.assertEqual(output[0].text.strip(), "position/h-sl-meters")
        self.assertEqual(output[1].get("caption"), "Velocity Down [fps]")
        self.assertEqual(output[1].text.strip(), "velocities/v-down-fps")


if __name__ == '__main__':
    sys.exit(unittest.main())

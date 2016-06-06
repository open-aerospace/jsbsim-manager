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
        case = jsbsim_manager.Case()
        runner = jsbsim_manager.RunManager(case)
        self.assertEqual(type(runner), jsbsim_manager.RunManager)

    def test_init_default(self):
        case = jsbsim_manager.Case()

        # Pure default values
        init = case.initial_conditions()

        # unwrap XML
        initialize = ET.fromstring(init)
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
        case = jsbsim_manager.Case()

        # Pure default values
        init = case.initial_conditions(vbody=2.5, latitude=45.0)

        # unwrap XML
        initialize = ET.fromstring(init)
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


if __name__ == '__main__':
    sys.exit(unittest.main())

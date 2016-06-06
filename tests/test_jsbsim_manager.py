#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jsbsim_manager
----------------------------------

Tests for `jsbsim_manager` module.
"""


import sys
import unittest

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

        self.maxDiff = 1500
        self.assertEqual(init, """<?xml version="1.0" ?>
<initialize name="Initial Conditions">
  <ubody unit="M/SEC">0.000000</ubody>
  <vbody unit="M/SEC">0.000000</vbody>
  <wbody unit="M/SEC">0.000000</wbody>
  <phi unit="DEG">0.000000</phi>
  <theta unit="DEG">0.000000</theta>
  <psi unit="DEG">0.000000</psi>
  <altitude unit="M">0.000000</altitude>
  <latitude unit="DEG">0.000000</latitude>
  <longitude unit="DEG">0.000000</longitude>
  <elevation unit="M">0.000000</elevation>
</initialize>
""")

    def test_init_override(self):
        case = jsbsim_manager.Case()

        # Pure default values
        init = case.initial_conditions(vbody=2.5, latitude=45.0)

        self.maxDiff = 1500
        self.assertEqual(init, """<?xml version="1.0" ?>
<initialize name="Initial Conditions">
  <ubody unit="M/SEC">0.000000</ubody>
  <vbody unit="M/SEC">2.500000</vbody>
  <wbody unit="M/SEC">0.000000</wbody>
  <phi unit="DEG">0.000000</phi>
  <theta unit="DEG">0.000000</theta>
  <psi unit="DEG">0.000000</psi>
  <altitude unit="M">0.000000</altitude>
  <latitude unit="DEG">45.000000</latitude>
  <longitude unit="DEG">0.000000</longitude>
  <elevation unit="M">0.000000</elevation>
</initialize>
""")

if __name__ == '__main__':
    sys.exit(unittest.main())

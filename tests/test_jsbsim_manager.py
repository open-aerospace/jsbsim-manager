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
        runer = jsbsim_manager.RunManager(case)


if __name__ == '__main__':
    sys.exit(unittest.main())

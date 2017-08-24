#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_quadis
----------------------------------

Tests for `quadis` module.
"""

import unittest

import quadis


class TestQuadis(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(quadis.__version__)

    def tearDown(self):
        pass

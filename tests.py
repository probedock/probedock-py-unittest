#!/usr/bin/env python

"""
This is tests for Probedock nose2 plugin
"""


import unittest
import time


from unittest_probedock import ProbedockTestResult


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


class Test(unittest.TestCase):
    def test_success(self):
        time.sleep(1)
        self.assertTrue(True)

    def test_failure(self):
        time.sleep(0.2)
        self.assertTrue(False)

    def test_error(self):
        raise Exception()

    @unittest.skip("Not yet implemented")
    def test_skip(self):
        raise Exception()

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_unexpected_success(self):
        self.assertTrue(True)


if __name__ == '__main__':
    test_modules = unittest.defaultTestLoader.discover(start_dir='.', pattern='test*.py', top_level_dir=None)
    res = unittest.TextTestRunner(verbosity=2, resultclass=ProbedockTestResult).run(test_modules).wasSuccessful()
    exit(not res)

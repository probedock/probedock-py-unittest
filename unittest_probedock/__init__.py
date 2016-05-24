#!/usr/bin/env python

"""
This is the Probedock probe for py.test
"""

import time
import unittest.runner

import requests

from probedock import ProbeDockReporter


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


class ProbedockTestResult(unittest.runner.TextTestResult):
    """
    A test result class that reports data to a Probedock.io server

    :param stream: stream on which to print the results
    :param descriptions: passed to TextTestResult
    :param verbosity: passed to TextTestResult
    """
    separator1 = '=' * 70

    def __init__(self, stream, descriptions, verbosity):
        super(ProbedockTestResult, self).__init__(stream, descriptions, verbosity)

        self.reporter = ProbeDockReporter("unittest")
        self.start_time = time.time()
        self.time = 0

    def _traceback(self, test, err, flavour):
        """
        nicely formats the traceback to send to probedock

        :param test: test that was run
        :param err: error the test gave
        :param flavour: type of the error
        :return: string showing the error nicely formatted
        """
        return "{}: {}\n\n{}".format(flavour, self.getDescription(test), self._exc_info_to_string(err, test))

    def startTest(self, test):
        """
        starts a new test and registers the time

        :param test: test that need to be started
        """
        super(ProbedockTestResult, self).startTest(test)
        self.time = time.time()

    def addSuccess(self, test):
        """
        reports the test as a success

        :param test: test ro report
        """
        super(ProbedockTestResult, self).addSuccess(test)
        self.reporter.addSuccess(test, time.time() - self.time)

    def addError(self, test, err):
        """
        reports the test as an error

        :param test: test to report
        :param err: error the test gave
        """
        super(ProbedockTestResult, self).addError(test, err)
        self.reporter.addError(test, time.time() - self.time, self._traceback(test, err, "ERROR"))

    def addFailure(self, test, err):
        """
        report the test as a failure

        :param test: test to report
        :param err: error the test gave
        """
        super(ProbedockTestResult, self).addFailure(test, err)
        self.reporter.addFailure(test, time.time() - self.time, self._traceback(test, err, "FAIL"))

    def addSkip(self, test, reason):
        """
        reports a test that was skipped

        :param test: test to report
        :param reason: reason why the test was skipped
        """
        super(ProbedockTestResult, self).addSkip(test, reason)
        self.reporter.addSkip(test, time.time() - self.time, reason)

    def addExpectedFailure(self, test, err):
        """
        reports a test that failed, but was expected to fail

        :param test: test to report
        :param err: error the test gave
        """
        super(ProbedockTestResult, self).addExpectedFailure(test, err)
        self.reporter.addExpectedFailure(test, time.time() - self.time, self._traceback(test, err, "EXPECTED FAILURE"))

    def addUnexpectedSuccess(self, test):
        """
        reports a test that passed but was expected to fail

        :param test: test to report
        """
        super(ProbedockTestResult, self).addUnexpectedSuccess(test)
        self.reporter.addUnexpectedSuccess(test, time.time() - self.time)

    def printErrors(self):
        """
        Prints a summary of the results
        """
        super(ProbedockTestResult, self).printErrors()

        self.stream.writeln(self.separator1)
        self.stream.write("Sending information to Probedock ... ")
        try:
            info = self.reporter.send_report(time.time() - self.start_time)
        except requests.exceptions.ConnectionError as e:
            self.stream.writeln("Error connecting to {}. Couldn't send data".format(e.request.url))
        else:
            self.stream.writeln("Data sent to {}".format(info))

#!/usr/bin/python3

import sys
from framework import test, e2e_framework_run

def run_all_tests():
    executable = sys.argv[1]
    test([executable], "Hello World\n")

e2e_framework_run(run_all_tests)

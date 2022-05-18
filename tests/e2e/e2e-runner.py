#!/usr/bin/python3

import sys
from framework import test, e2e_framework_run

def run_all_tests():
    executable = sys.argv[1]
    test([executable], b"NOTE: Checking for updates as scheduled in 'adept.config'\n -> Already up to date!\n     /\xe2\xe2\\\n    /    \\    \n   /      \\    \n  /   /\\   \\        The Adept Compiler v2.7 - (c) 2016-2022 Isaac Shelton\n /   /\\__   \\\n/___/    \\___\\\n\nUsage: adept [options] [filename]\n\nOptions:\n    -h, --help        Display this message\n    -e                Execute resulting executable\n    -w                Disable compiler warnings\n    -o FILENAME       Output to FILENAME (relative to working directory)\n    -n FILENAME       Output to FILENAME (relative to file)\n    -c                Emit object file\n    -O0,-O1,-O2,-O3   Set optimization level\n    --windowed        Don't open console with executable (only applies to Windows)\n    -std=2.x          Set standard library version\n    --version         Display compiler version\n    --root            Display root folder\n    --help-advanced   Show lesser used compiler flags\n")

e2e_framework_run(run_all_tests)

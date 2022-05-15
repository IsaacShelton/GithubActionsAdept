
# ---------------------------------------------------------
# Minimal E2E Testing Framework for Command-Line Programs
#     by Isaac Shelton
# ---------------------------------------------------------

import re
import sys
import subprocess

RED = "\x1B[31m"
NORMAL = "\x1B[0m"
GREEN = "\x1B[32m"

all_good = True

if sys.version_info.major != 3:
    print(RED + "ERROR: e2e-runner.py expects to be run with Python 3" + NORMAL)
    sys.exit(1)

if len(sys.argv) != 2:
    print(RED + "ERROR: e2e-runner.py requires executable location!" + NORMAL)
    print(RED + "  e2e-runner.py <executable>" + NORMAL)
    sys.exit(1)

def e2e_framework_run(run_all_tests_function):
    global all_good

    try:
        run_all_tests_function()
    except subprocess.CalledProcessError as e:
        print(RED + "ERROR: A testing command exited with non-zero status" + NORMAL)
        print(RED + "Cmd: " + str(e.cmd) + NORMAL)
        print(RED + "Out ---------------------------" + NORMAL)
        print(e.output)
        all_good = False

    if not all_good:
        print(RED + "Exiting with status of 1..." + NORMAL)
        sys.exit(1)
    else:
        print(GREEN + "All tests passed..." + NORMAL)
        sys.exit(0)

def test(args, expected_output):
    global all_good
    res = subprocess.run(args, capture_output=True)

    # Remove ANSI excape sequences
    # https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python
    # 7-bit and 8-bit C1 ANSI sequences
    ansi_escape_8bit = re.compile(
        br'(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])'
    )
    actual_output = ansi_escape_8bit.sub(b'', res.stdout.replace(b'\r\n', b'\n')).decode('ascii')
    
    if actual_output != expected_output:
        print(RED + "TEST FAILED: Command " + str(args) + " does not match expected output." + NORMAL)
        print(RED + "Expected...\n" + NORMAL + expected_output)
        print(RED + "Actual...\n" + NORMAL + actual_output)
        all_good = False
        print(RED + "Raw bytes...\n" + NORMAL + res.stdout)

    res.check_returncode()

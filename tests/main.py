import os
import sys
import unittest


def main():
    curr_work_dir = os.getcwd()
    test_directories = [
        os.path.join(curr_work_dir, "app"),
        os.path.join(curr_work_dir, "commands"),
        os.path.join(curr_work_dir, "components")
    ]

    test_suite = unittest.TestSuite()

    for test_dir in test_directories:
        discover_tests = unittest.defaultTestLoader.discover(test_dir, pattern='*.py', top_level_dir='.')

        for test in discover_tests:
            test_suite.addTests(test)

    unittest.TextTestRunner().run(test_suite)


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)

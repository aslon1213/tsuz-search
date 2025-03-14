import unittest
import sys
import os

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import test modules
from tsuz_search.test_client import TestClient
from tsuz_search.test_models import TestModels

if __name__ == "__main__":
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestClient))
    test_suite.addTest(unittest.makeSuite(TestModels))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Exit with non-zero code if tests failed
    sys.exit(not result.wasSuccessful())

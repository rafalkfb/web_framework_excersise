import unittest
from tests_cases.home.login_tests import LoginTests
from tests_cases.courses.register_courses_csv import RegisterCoursesCSVTests

test_cases1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
test_cases2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVTests)

smoke_tests = unittest.TestSuite([test_cases1, test_cases2])

unittest.TextTestRunner(verbosity=2).run(smoke_tests)

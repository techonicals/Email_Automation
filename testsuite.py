import os
import unittest
import HTMLTestRunner
import login
# report_location = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
# print report_location
suitetest = unittest.TestLoader().loadTestsFromTestCase(login.testing)
all_tests = unittest.TestSuite([suitetest])

#
# directory = os.path.join(report_location + "/")
# # create output directory if it does not exists
# if not os.path.exists(directory):
#     os.makedirs(directory)
# # open the report file
# outfile = open(directory  + "1SuiteReport.html", "w")

# # configure HTMLTestRunner options
# runner = HTMLTestRunner.HTMLTestRunner(
#     stream=outfile,
#     title='Test Report',
#     description='Tests report'
# )

runner=unittest.TextTestRunner(descriptions=True, verbosity=2 )
runner.run(all_tests)

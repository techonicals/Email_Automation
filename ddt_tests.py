import unittest
from ddt import ddt,file_data,unpack
import os
# @file_data('data.json')
# def test_data(self, data_set):
#     print data_set['start']



@ddt
class testing(unittest.TestCase):
    orig = "data/data12.json"
    dup = "data/data2.json"
    if os.path.isfile(orig):
        varl = orig


    else:
        varl = dup

    @file_data(varl)
    def test_dict(self, data_set):
        try:
            self.assertLess(data_set['start'],data_set['end'])
            print "in try"
        except AssertionError as e:
            print("Exception= '{0}'".format(e.message))
            raise

# self.assertLess(data_set['value'], data_set['end'])
# self.assertGreater(data_set['value'], data_set['end'])



# @data(1, 2)
# def test_greater_than_zero(self, value):
#     self.assertGreater(value, 0)
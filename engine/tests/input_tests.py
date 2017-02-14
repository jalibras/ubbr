
from unittest import TestCase
import os
import sys

d = os.path.dirname
ubbr_location = d(d(d(d((os.path.abspath(__file__))))))
print(ubbr_location)
sys.path.append(ubbr_location)


from ubbr.engine.core import Ubbr
import json





class UbbrTest(TestCase):


    def setUp(self):
        fixtures_path = os.path.join(d(os.path.abspath(__file__)),'fixtures')
        with open(os.path.join(fixtures_path,'inputtestcases.json')) as tc_file:
            self.testcases = json.load(tc_file)

    def test_inputs(self):
        tcs = [c  for c in self.testcases if c['test']=='Input']
        for case in tcs:
            u = Ubbr(case['source'])
            output = u.get_context()
            values_output=output[0]
            data_output = output[1]
            self.assertRegex(values_output[0],case['output']['patterns'][0])
            self.assertEqual(data_output[0]['data_type'],case['output']['data'][0]['data_type'])



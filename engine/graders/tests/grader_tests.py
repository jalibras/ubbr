
from unittest import TestCase
import os
import sys

d = os.path.dirname
ubbr_location = d(d(d(d(d((os.path.abspath(__file__)))))))
print(ubbr_location)
sys.path.append(ubbr_location)

from ubbr.engine.core import Ubbr
from ubbr.engine.graders.graders import StringInputGrader, IntegerInputGrader

import json


class UbbrTest(TestCase):

    def setUp(self):
        fixtures_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'fixtures')
        with open(os.path.join(fixtures_path,'testcases.json')) as tc_file:
            self.testcases = json.load(tc_file)


    def test_string_grader(self):
        cases = [case for case in self.testcases if case['test']=='string_grader']
        for tc in cases:
            u = Ubbr(tc['source'])
            data = u.get_context()[1]
            for r in data:
                grader = StringInputGrader()
                for answer in tc['correct']:
                    self.assertEqual(grader.grade(answer,r)['score'],grader.grade(answer,r)['max_score'])
                for answer in tc['incorrect']:
                    self.assertEqual(grader.grade(answer,r)['score'],int(0))




    def test_integer_grader(self):
        cases = [case for case in self.testcases if case['test']=='integer_grader']
        for tc in cases:
            u = Ubbr(tc['source'])
            data = u.get_context()[1]
            for r in data:
                grader = IntegerInputGrader()
                for answer in tc['correct']:
                    self.assertEqual(grader.grade(answer,r)['score'],grader.grade(answer,r)['max_score'])
                for answer in tc['incorrect']:
                    self.assertEqual(grader.grade(answer,r)['score'],int(0))


    def test_decimal_input_precision(self):
        tcs = [c  for c in self.testcases if c['test']=='DecimalInput Precision']
        for case in tcs:
            u = Ubbr(case['source'])
            



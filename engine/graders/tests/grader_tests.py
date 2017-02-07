
from unittest import TestCase
from ubbr.engine.core import Ubbr
from ubbr.engine.graders.graders import StringInputGrader, IntegerInputGrader

import json
import os


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
                    self.assertEqual(grader.grade(answer,r)[0],True)
                for answer in tc['incorrect']:
                    self.assertEqual(grader.grade(answer,r)[0],False)




    def test_integer_grader(self):
        cases = [case for case in self.testcases if case['test']=='integer_grader']
        for tc in cases:
            u = Ubbr(tc['source'])
            data = u.get_context()[1]
            for r in data:
                grader = IntegerInputGrader()
                for answer in tc['correct']:
                    self.assertEqual(grader.grade(answer,r)[0],True)
                for answer in tc['incorrect']:
                    self.assertEqual(grader.grade(answer,r)[0],False)





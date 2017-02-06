
from unittest import TestCase
from core import Ubbr
from graders.graders import StringInputGrader, IntegerInputGrader

import json


class UbbrTest(TestCase):

    def setUp(self):
        with open('graders/tests/fixtures/testcases.json') as tc_file:
            self.testcases = json.load(tc_file)


    def test_string_grader(self):
        cases = [case for case in self.testcases if case['test']=='string_grader']
        for tc in cases:
            u = Ubbr(tc['source'])
            resources = u.get_context()[1]
            for r in resources:
                grader = StringInputGrader(r)
                for answer in tc['correct']:
                    self.assertEqual(grader.grade(answer)[0],True)
                for answer in tc['incorrect']:
                    self.assertEqual(grader.grade(answer)[0],False)




    def test_integer_grader(self):
        cases = [case for case in self.testcases if case['test']=='integer_grader']
        for tc in cases:
            u = Ubbr(tc['source'])
            resources = u.get_context()[1]
            for r in resources:
                grader = IntegerInputGrader(r)
                for answer in tc['correct']:
                    self.assertEqual(grader.grade(answer)[0],True)
                for answer in tc['incorrect']:
                    self.assertEqual(grader.grade(answer)[0],False)






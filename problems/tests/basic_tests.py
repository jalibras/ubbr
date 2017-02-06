
from unittest import TestCase
from core import Ubbr


import json


class UbbrTest(TestCase):


    def setUp(self):
        with open('tests/fixtures/testcases.json') as tc_file:
            self.testcases = json.load(tc_file)




    def test_make_method(self):
        cases = [a for a in self.testcases if a['test'].startswith('basic')]
        for tc in cases:
            u = Ubbr(tc['source'])
            op = u._make()
            self.assertEqual(op[0],tc['output']['template'])
            self.assertEqual(op[1],tc['output']['code_fragments'])

    def test_get_context(self):
        cases = [a for a in self.testcases if a['test'].startswith('basic')]
        for tc in cases:
            u = Ubbr(tc['source'])
            nodes = u.get_context()[0]
            self.assertEqual(nodes,tc['output']['ubbrnodes'])

   
    def test_random_seed(self):
        #  checking that the random seed passes to the Ubbr correctly
        cases = [a for a in self.testcases if a['test'].startswith('random')]
        for tc in cases:
            u = Ubbr(tc['source'])
            one = u.get_context(random_seed=4)
            two = u.get_context(random_seed=4)
            self.assertEqual(one,two)

    def test_string_input(self):
        cases = [case for case in self.testcases if case['test']=='input']
        for tc in cases:
            u = Ubbr(tc['source'])
            nodes = u.get_context()[0]
            for j in range(len(nodes)):
                self.assertRegex(nodes[j],tc['output']['ubbrnodes'][j])

    def test_string_grader(self):
        cases = [case for case in self.testcases if case['test']=='stringgrader']
        for tc in cases:
            u = Ubbr(tc['source'])
            resources = u.get_context()[1]
            for r in resources:
                pass




import json


class BaseGrader(object):
    def __init__(self,data_string):
        self.data = json.loads(data_string)

    def grader(self,answer):
# returns a pair (Boolean,Information) where 
# Information is a json encoded object that 
# might contain extra information about the 
# grade. The Boolean is used for cases where simple 
# correct/incorrect reporting is appropriate
        pass


class StringInputGrader(BaseGrader):
        

    def grade(self,answer):
        if answer==self.data['answer']:
            return (True, "")
        else:
            return (False, "")

       
class IntegerInputGrader(BaseGrader):

    def grade(self,answer):
        if int(answer)==int(self.data['answer']):
            return (True, "")
        else:
            return (False, "") 

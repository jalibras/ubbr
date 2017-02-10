
import decimal
import json


class BaseGrader(object):

    def grade(self,answer,data):
# returns a pair (Boolean,Information) where 
# data is an object (dict) that 
# might contain extra information about the 
# grade. The Boolean is used for cases where simple 
# correct/incorrect reporting is appropriate
        pass


class StringInputGrader(BaseGrader):

    def grade(self,answer,data):
        if answer==data['answer']:
            return {
                    "score":1,
                    "max_score":1,
                    "data":{}
                    }
        else:
            return {
                    "score":0,
                    "max_score":1,
                    "data":{}
                    }

       
class IntegerInputGrader(BaseGrader):

    def grade(self,answer,data):
        if int(answer)==int(data['answer']):
            return {
                    "score":1,
                    "max_score":1,
                    "data":{}
                    }
        else:
            return {
                    "score":0,
                    "max_score":1,
                    "data":{}
                    }



def grader_from_data_type(data_type):
    if data_type == 'StringInput':
        return StringInputGrader
    if data_type == 'IntegerInput':
        return IntegerInputGrader
    return False




import decimal
from decimal import Decimal
from decimal import localcontext
import json


class BaseGrader(object):

    def grade(self,answer,data):
        """returns a dict with keys grade, max_grade and data"""
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


class DecimalInputGrader(BaseGrader):
    def grade(self,guess,data):
        with localcontext() as ctx:
            ctx.prec = int(data.get('prec',4))
            ctx.rounding = data.get('rounding','ROUND_HALF_UP')
            guess_as_decimal = Decimal(guess)
            correct = Decimal(data['answer_string'])
            if +guess_as_decimal == +correct:
                return {
                        "score": 1,
                        "max_score":1,
                        "data": {
                            "rel_error":str(Decimal(0))
                            }
                        }
            else:
                return {
                        "score": 0,
                        "max_score":1,
                        "data": {
                            "rel_error":str(abs((guess_as_decimal-correct)/correct))
                            }
                        }

        



def grader_from_data_type(data_type):
    if data_type == 'StringInput':
        return StringInputGrader
    if data_type == 'IntegerInput':
        return IntegerInputGrader
    if data_type == 'DecimalInput':
        return DecimalInputGrader
    raise ValueError('Cannot find grader class for input type {}'.format(data_type))



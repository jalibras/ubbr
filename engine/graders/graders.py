
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

    def __init__(self,default_prec=4,default_rounding='ROUND_HALF_UP'):
        self.default_prec = default_prec
        self.default_rounding = default_rounding




    def grade(self,guess,data):
        with localcontext() as ctx:
            ctx.prec = int(data.get('prec',self.default_prec))
            ctx.rounding = data.get('rounding',self.default_rounding)
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

        

class ExpressionInputGrader(BaseGrader):

    def grade(self,guess,data):
        try:
            from sage.all import symbolic_expression,var
        except:
            raise ImportError('could not import from sage.all')
        
        output = {
                'score':0,
                'max_score':1,
                'data':{
                    'info':'incorrect expression'
                    }
                }

        for v in data['variable_names']:
            var(v)

        try:
            guess_expression = symbolic_expression(guess)
        except:
            output.update({
                'data':{
                    'info':'could not convert input into a valid expression'
                    }
                })
            return output


        answer = symbolic_expression(data['answer_string'])
        if data['method']=='identity':

            if (guess_expression - answer).is_zero():
                output.update({
                    'score':1,
                    'data':{}

                    })
            else:
                pass

            return output
        else:
            raise ValueError('Unknown method in ExpressionInput')






def grader_from_data_type(data_type):
    if data_type == 'StringInput':
        return StringInputGrader
    if data_type == 'IntegerInput':
        return IntegerInputGrader
    if data_type == 'DecimalInput':
        return DecimalInputGrader
    if data_type == 'ExpressionInput':
        return ExpressionInputGrader
    raise ValueError('Cannot find grader class for input type {}'.format(data_type))



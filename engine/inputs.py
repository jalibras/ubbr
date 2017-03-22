from decimal import Decimal
import json
import random

class BaseInput(object):


    def __init__(self,**kwargs):
        self.kwargs = kwargs


    def get_html(self,input_id):
        return "<div class='ubbr-input' id='ubbr-input-{input_id}'><input type='text' name='ubbr-input-{input_id}'></input></div>".format(input_id=input_id)




    # subclasses must override this methods
    def data(self,data_id=None):
    # should return a data object for the input 
    # NB. this should be serializable
        pass



class StringInput(BaseInput):

    def __init__(self,answer,**kwargs):
        self.answer = answer
        super(StringInput,self).__init__(**kwargs)


    def data(self,data_id=None):
        r = {
                'data_id':data_id,
                'data_type': 'StringInput',
                'answer': self.answer,
                }
        return r


    def get_html(self,input_id):
        return "<div class='ubbr-input' id='ubbr-input-{input_id}'><input type='text' name='ubbr-input-{input_id}'></input></div>".format(input_id=input_id)




class IntegerInput(BaseInput):

    def __init__(self,answer,**kwargs):
        self.answer = int(answer)
        super(IntegerInput,self).__init__(**kwargs)


    def data(self,data_id=None):
        r = {
                'data_id':data_id,
                'data_type': 'IntegerInput',
                'answer': self.answer,
                }
        return r

    def get_html(self,input_id):
        return "<div class='ubbr-input' id='ubbr-input-{input_id}'><input type='text' name='ubbr-input-{input_id}'></input></div>".format(input_id=input_id)


class DecimalInput(BaseInput):
    def __init__(self,answer,**kwargs):
        self.answer = Decimal(answer)
        self.answer_string = str(self.answer)
        self.prec = int(kwargs.get('prec',4))
        self.rounding = kwargs.get('rounding','ROUND_HALF_UP')
        super(DecimalInput,self).__init__(**kwargs)

    def data(self,data_id=None):
        r = {
                'data_id':data_id,
                'data_type':"DecimalInput",
                'answer_string' :self.answer_string,
                'prec': self.prec,
                'rounding':self.rounding
                }
        return r


class MultipleChoiceInput(BaseInput):
    def __init__(self,choices,correct_index,**kwargs):
        self.shuffle = kwargs.get('shuffle',True)
        perm = list(range(len(choices)))
        if self.shuffle:
            random.shuffle(perm) 
        self.choices = [choices[j] for j in perm]
        self.correct_index = perm.index(correct_index)

    def get_html(self,input_id=None):
        pass



class ExpressionInput(BaseInput):
    def __init__(self,expression,**kwargs):
        self.expression=expression
        self.method = kwargs.get('method','identity')

    def data(self,data_id=None):
        variable_names = [str(v) for v in self.expression.variables()]
        r = {
                'data_id':data_id,
                'data_type':"ExpressionInput",
                'answer_string' :str(self.expression),
                'variable_names':variable_names,
                'method':self.method,
                }
        return r


        





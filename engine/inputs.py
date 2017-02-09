import json

class BaseInput(object):


    def __init__(self,**kwargs):
        self.kwargs = kwargs



    def get_html(self,input_id):
        return "<div class='ubbr-input' id='ubbr-input-{}'></div>".format(input_id)

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
    pass

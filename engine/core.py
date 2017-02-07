"""
Instances of Ubbr take a source string 
and generate django/jinja style templates
together with a list of strings that can be 
passed to the template as a variable called 
ubbrnodes
"""


import re

# imports for the Ubbr source code
from ubbr.engine.inputs import StringInput, IntegerInput


class UbbrState(object):
    def __init__(self,random_seed=None):
        self.out_stream=""
        self.random_seed = random_seed
        self.data=[]
    

    def echo(self,obj):
        if hasattr(obj,'data'):
            data_id = len(self.data)
            self.data.append(obj.data(data_id))
            self.out_stream+=obj.get_html(data_id)
            return 
        self.out_stream+=str(obj)
        return
    
    def get_output(self):
        return self.out_stream

    def get_data(self):
        return self.data

class Ubbr(object):
    def __init__(self,source=None,tag_name='ubbr',**kwargs):
        self.source = source
        self.tag_name = tag_name
        self.template,self.code_fragments = self._make() 

    



    def _make(self):
        pattern = r'{%\s*?'+self.tag_name+r'\s*?%}\s*(.*?){%\s*?end'+self.tag_name+r'\s*?%}'
        #pattern = r'{%\s*?'+self.tag_name+r'\s*(.*?)%}'
        fragment_list = re.split(pattern,self.source,flags=re.DOTALL)
        template_fragments = [fragment_list.pop(0)]
        code_fragments = []
        while len(fragment_list) > 0:
            code_fragments.append(fragment_list.pop(0))
            template_fragments.append(fragment_list.pop(0))

        template = ""
        template +=template_fragments.pop(0)
        counter = 0
        while len(template_fragments)>0:
            template +="{{ ubbrnodes."+str(counter)+" }}"+template_fragments.pop(0)
            counter+=1
        return [template,code_fragments]

    def _execute_code(self,random_seed=None,code_fragments=None):
        # returns an instance of UbbrState that results from executing the 
        # assembled code_fragemants (together with separatos)
        code = "\nubbr_state.echo('_ubbr_separator_')\n".join(code_fragments)
        ubbr_state = UbbrState(random_seed=random_seed)
        # here we inject some function names into the global namespace
        echo = ubbr_state.echo
        exec(code)
        return ubbr_state

    def get_template(self):
        return self._make()[0]
    
    def get_context(self,random_seed=None,code_fragments=None):
        """
returns a pair (list of strings,list of data) 
The list of srings tcan be passed to the template
as a variable named ubbrnodes.
The data contain information required to 
grade answers
"""
        if code_fragments==None:
            code_fragments = self.code_fragments
        if code_fragments==[]:
            return ([],[])

        state = self._execute_code(code_fragments=code_fragments,random_seed=random_seed)
        return ((state.get_output()).split('_ubbr_separator_'),state.get_data())



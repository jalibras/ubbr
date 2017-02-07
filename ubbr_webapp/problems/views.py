from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

# adding the ubbr namespace to the path
# assuming that is two levels above the django project root
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(settings.BASE_DIR)))

from ubbr.engine.core import Ubbr
from ubbr.engine.graders.graders import StringInputGrader, IntegerInputGrader,grader_from_data_type


from problems.models import ModelUbbr

import json

# Create your views here.


def problem_view(request,id):
    model_ubbr = ModelUbbr.objects.get(id=id)
    ubbr = Ubbr(model_ubbr.source)
    # get the template string and context values from the Ubbr
    template_string = ubbr.template
    random_seed=request.GET.get('seed','1')
    ubbrvalues = ubbr.get_context(random_seed=random_seed)[0]

    # now some standard django code for rendering a template
    # from a string and a dict of context values
    context = RequestContext(request,autoescape=False) # we use a RequestContext to enable csrf protection
    context.update({
        'ubbrvalues':ubbrvalues,
        'problem_id':model_ubbr.id, 
        })
    template = Template(template_string)
    return HttpResponse(template.render(context))

def problem_grade(request,id):
    if request.method !='POST':
        return HttpResponse('Only POST requests are supported')
# load the Ubbr from the DB and get the answer data 
    model_ubbr = ModelUbbr.objects.get(id=id)
    ubbr = Ubbr(model_ubbr.source)
    # get the template and context values from the Ubbr
    template_string = ubbr.template
    random_seed=request.GET.get('seed','1')
    ubbrdata = ubbr.get_context(random_seed=random_seed)[1]

# now use the graders to compare the submitted values with the 
# correct answers
    results = {}
    for inp in ubbrdata:
        grader = grader_from_data_type(inp['data_type'])().grade
        
        submitted = request.POST.get('ubbr-input-{}'.format(inp['data_id']),None)
        results.update({
            inp['data_id']:grader(submitted,inp)
            })

    return HttpResponse(json.dumps(results))



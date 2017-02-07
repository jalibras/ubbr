from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

from django.conf import settings

# adding the ubbr namespace to the path
# assuming that is two levels above the django project root
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(settings.BASE_DIR)))

from ubbr.engine.core import Ubbr

from problems.models import ModelUbbr

# Create your views here.


def problem_view(request,id):
    model_ubbr = ModelUbbr.objects.get(id=id)
    ubbr = Ubbr(model_ubbr.source)
    # get the template and context values from the Ubbr
    template_string = ubbr.template
    random_seed=request.GET.get('seed','1')
    ubbrnodes_value = ubbr.get_context(random_seed=random_seed)[0]

    # now some standard django code for rendering a template
    # from a string and a dict of context values
    context = Context({'ubbrnodes':ubbrnodes_value},autoescape=False)
    template = Template(template_string)
    return HttpResponse(template.render(context))


from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.urls import reverse, reverse_lazy
from green.models import Rules
from django.template import Template, Context


def rules_set():
    try:
        rules_list = Rules.objects.filter(status=10)
        with open("/root/GreenSite/rules_set.txt") as f:
            rules_str = f.read()
            t = Template(rules_str)
            content = {
                'rules_list': rules_list,
            }
            c = Context(content)
            res = t.render(c)

        rules_f = open("/root/GreenSite/rules_set.py", "w")
        print(rules_f)
        rules_f.write(res)
    except Exception as e:
        print(e)

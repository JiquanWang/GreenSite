from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.urls import reverse, reverse_lazy
from green.models import Rules
import time
# Create your views here.


def get_rules_list(request):
    if request.user.is_authenticated:
        rules_list = Rules.objects.all()
        content = {
            'active_main_menu': '自动控制',
            'active_submenu': '规则列表',
            'rules_list': rules_list,
        }
        return render(request, "rules/rules_list.html", content)


def add_new_rule(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            content = {
                'active_main_menu': '自动控制',
                'active_submenu': '添加新规则',
            }
            return render(request, "rules/add_new_rule.html", content)
        if request.method == 'POST':
            name = request.POST.get('name')
            comment = request.POST.get('comment')
            status = request.POST.get('status')
            condition = request.POST.get('condition')
            performance = request.POST.get('performance')
            try:
                rule = Rules(name=name, comment=comment, status=status, condition=condition, performance=performance, created_time=int(time.time()))
                rule.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('rules:get_rules_list'))


def modify_the_rule(request, rule_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            rule = Rules.objects.get(id=rule_id)
            content = {
                'active_main_menu': '自动控制',
                'active_submenu': '修改规则',
                'rule': rule,
            }
            return render(request, 'rules/modify_the_rule.html', content)
        if request.method == 'POST':
            try:
                rule = Rules.objects.get(id=rule_id)
                rule.name = request.POST.get('name')
                rule.comment = request.POST.get('comment')
                rule.status = request.POST.get('status')
                rule.condition = request.POST.get('condition')
                rule.performance = request.POST.get('performance')
                rule.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('rules:get_rules_list'))


def delete_the_rule(request, rule_id):
    if request.user.is_authenticated:
        try:
            rule = Rules.objects.get(id=rule_id)
            rule.delete()
        except Exception as e:
            print(e)
        return HttpResponseRedirect(reverse('rules:get_rules_list'))


def adapt_the_rule(request, rule_id):
    if request.user.is_authenticated:
        try:
            rule = Rules.objects.get(id=rule_id)
            if rule.status == -10:
                rule.status = 10
            elif rule.status == 10:
                rule.status = -10
            rule.save()
        except Exception as e:
            print(e)
        return HttpResponseRedirect(reverse('rules:get_rules_list'))

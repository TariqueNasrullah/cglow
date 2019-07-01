from django.shortcuts import render, HttpResponse
from contest.models import *
from . models import clearifications
from django.contrib.auth.models import User
import datetime

def clearification(request, contest_name):
    if request.method == 'POST':
        problem_id = request.POST['problem_name']
        clearification_text = request.POST['clearification-text']

        problem_instance = contest_problemset.objects.get(pk=problem_id)
        contest_instance = problem_instance.contest_id
        author = request.user
        clearification_instance = clearifications(
            associated_contest = contest_instance,
            associated_problem = problem_instance,
            author = author,
            clearification_text = clearification_text
        )
        clearification_instance.save()
    
    context = {}

    this_contest = contest.objects.get(pk=contest_name)
    problem_list = contest_problemset.objects.filter(contest_id=this_contest)
    
    start_time = this_contest.start_time
    end_time = this_contest.end_time
    current_time = datetime.datetime.now(datetime.timezone.utc)
    sub1 = start_time.timestamp() - current_time.timestamp()
    sub2 = end_time.timestamp() - current_time.timestamp()

    if sub1 < 0.0 and sub2 > 0.0:
        context['running'] = True
    else:
        context['running'] = False

    context['contest'] = this_contest
    context['contest_id'] = contest_name
    context['problem_list'] = problem_list
    context['contest_info'] = this_contest

    clearification_list = clearifications.objects.filter(associated_contest=this_contest).order_by('-declare_time')
    context['clearification_list'] = clearification_list

    return render(request, 'clearification/clearification.html', context)

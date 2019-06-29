from django.shortcuts import render, HttpResponse
from contest.models import *
import datetime

def clearification(request, contest_name):
    if request.method == 'GET':
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
        return render(request, 'clearification/clearification.html', context)
    else:
        print(request.POST)
        return HttpResponse("Post successfull")

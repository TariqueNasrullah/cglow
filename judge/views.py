from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.core.exceptions import ObjectDoesNotExist
import json
from contest.models import contest, contest_problemset, contestant_point, contest_submission
from django.core import serializers

def judge_index(request):
    contests = contest.objects.all().values('id' ,'name')
    context = {}
    context['contest_list'] = contests

    return render(request, 'judge/judge_index.html', context)

def judger_page(request, contest_name):
    try:
        context = {}

        l = contest.objects.get(pk=contest_name)
        number_of_problems = contest_problemset.objects.filter(contest_id__pk=contest_name).count()
        number_of_contestant = contestant_point.objects.filter(contest_id__pk=contest_name).count()
        number_of_submission = contest_submission.objects.filter(problem_id__contest_id__pk=contest_name).count()
        number_of_ac = contest_submission.objects.filter(problem_id__contest_id__pk=contest_name, judge_result="Accepted").count()
        submission_list = contest_submission.objects.filter(problem_id__contest_id=contest_name).order_by("-submission_time")
        submission_list_json = serializers.serialize('json', submission_list)

        context['submission_list'] = submission_list_json
        context['accepted_count'] = number_of_ac
        context['submission_count'] = number_of_submission
        context['contestant_count'] = number_of_contestant
        context['problem_count'] = number_of_problems
        context['contest_info'] = l
        context['contest_name_json'] = mark_safe(json.dumps(contest_name))

        return render(request, 'judge/judger_page.html',context)

    except ObjectDoesNotExist:
        return render(request, 'home/404.html')
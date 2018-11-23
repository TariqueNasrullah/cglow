from django.shortcuts import render, HttpResponse, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from contest.models import contest as contest_table
from contest.models import contest_problemset
from contest.models import contest_submission
from contest.models import contestant_point
from django.core import serializers
from contest.forms import UploadFileForm

from .tasks import contest_submission_ack
import datetime
import pickle
import json
from django.core import serializers

# Create your views here.

def contest_list(request):
	context = {}
	if request.user.is_authenticated:
		context['username'] = request.user.username
	l = contest_table.objects.all()
	context['contest_list'] = l

	return render(request, 'contest/contest_list.html', context)

def contest_info(request, pk=None):
	try:
		context = {}
		if request.user.is_authenticated:
			context['username'] = request.user.username

		l = contest_table.objects.get(pk=pk)
		context['contest_info'] = l

		#calculating contest duration
		tm = l.end_time - l.start_time

		context['contest_duration'] = tm
		context["contest_id"] = pk

		return render(request, 'contest/contest_info.html', context)

	except ObjectDoesNotExist:
		return render(request, 'home/404.html')

def contest_dashboard(request, pk=None):
	context = {}
	if request.user.is_authenticated:
		context['username'] = request.user.username

	#gather contest info
	contest_info = contest_table.objects.get(pk=pk)
	context['contest_info'] = contest_info

	#gather problem set for this contest
	problemset = contest_problemset.objects.filter(contest_id__id=pk).order_by('problem_title')

	context['problemset'] = problemset

	context['contest_id'] = pk

	return render(request, 'contest/contest_dashboard.html', context)

def contest_show_problem(request, pk=None, problem_id=None):
	try:
		# Gather this problem related data
		problem = contest_problemset.objects.get(pk=problem_id)

		if request.method=='POST':
			form = UploadFileForm(request.FILES['datafile'])
			if form:
				language = request.POST['filetype']
				uploaded_file = request.FILES['datafile']
				problem_id = problem
				instance = contest_submission(problem_id=problem_id, user_id=request.user, uploaded_file=uploaded_file, language=language)
				instance.save()
				contest_submission_ack.delay(instance.pk)

		context = {}
		if request.user.is_authenticated:
			context['username'] = request.user.username
			
		#Gather contest info
		contest_info = contest_table.objects.get(pk=pk)
		context['contest_info'] = contest_info

		
		context['problem'] = problem
		context['contest_id'] = pk

		return render(request, 'contest/contest_problem_view.html', context)
	
	except ObjectDoesNotExist:
		return render(request, 'home/404.html')

def contest_individual_submission(request, pk=None):
	context = {}
	if request.user.is_authenticated:
		context['username'] = request.user.username

	#Gather submisssion data
	l = contest_submission.objects.filter(user_id=request.user, problem_id__contest_id__id=pk)
	context['contest_submission'] = l

	#Gather contest related data
	contest_info = contest_table.objects.get(pk=pk)
	context['contest_info'] = contest_info
	context['contest_id'] = pk

	return render(request, 'contest/contest_submission.html', context)


def contest_standing(request, pk=None):
	context = {}
	context['contest_id'] = pk

	if request.user.is_authenticated:
		context['username'] = request.user.username
	#Gather contest info
	contest_info = contest_table.objects.get(pk=pk)
	context['contest_info'] = contest_info

	#Calculate ranklist
	user_list = contestant_point.objects.filter(contest_id=pk).order_by('-solve', 'penalty')
	problems = contest_problemset.objects.filter(contest_id=pk).order_by('problem_title')
	total_problem = problems.count()

	total_standing = []

	for i in user_list:
		user_info = []
		user_info.append(i.user_id.username)
		user_info.append(i.solve)
		user_info.append(i.penalty)

		data = []
		for j in problems:
			ac_count = contest_submission.objects.filter(user_id=i.user_id, problem_id=j.id, problem_id__contest_id__id=pk, judge_result="Accepted").count()
			submisssion_count = contest_submission.objects.filter(user_id=i.user_id, problem_id=j.id, problem_id__contest_id__id=pk).count()
			res = ""
			if ac_count != 0:
				res = "ac"
			elif submisssion_count != 0:
				res = "sub"
			else:
				res = "nosub"
			data.append(res)
		user_info.append(data)
		total_standing.append(user_info)

	context['standing'] = total_standing
	context['number_of_problems'] = total_problem
	context['pk'] = pk
	return render(request,'contest/contest_standing.html', context)
	

def contest_standing_server(request, pk=None):
	context = {}
	context['contest_id'] = pk

	if request.user.is_authenticated:
		context['username'] = request.user.username
	#Gather contest info
	contest_info = contest_table.objects.get(pk=pk)

	#Calculate ranklist
	user_list = contestant_point.objects.filter(contest_id=pk).order_by('-solve', 'penalty')
	problems = contest_problemset.objects.filter(contest_id=pk).order_by('problem_title')
	total_problem = problems.count()

	total_standing = []

	for i in user_list:
		user_info = []
		user_info.append(i.user_id.username)
		user_info.append(i.solve)
		user_info.append(i.penalty)

		data = []
		for j in problems:
			ac_count = contest_submission.objects.filter(user_id=i.user_id, problem_id=j.id, problem_id__contest_id__id=pk, judge_result="Accepted").count()
			submisssion_count = contest_submission.objects.filter(user_id=i.user_id, problem_id=j.id, problem_id__contest_id__id=pk).count()
			res = ""
			if ac_count != 0:
				res = "ac"
			elif submisssion_count != 0:
				res = "sub"
			else:
				res = "nosub"
			data.append(res)
		user_info.append(data)
		total_standing.append(user_info)

	context['standing'] = total_standing
	context['number_of_problems'] = total_problem
	context['pk'] = pk

	return HttpResponse(json.dumps(context))
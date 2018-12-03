from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from offlineProblemSolve.models import problemset, submission
from django.core.exceptions import ObjectDoesNotExist
from offlineProblemSolve.forms import UploadFileForm
from .tasks import offline_submission_ack
from django.urls import reverse
# Create your views here.

def problem_list(request):
	context = {}

	if request.user.is_authenticated:
		context['username'] = request.user.username

	l = problemset.objects.all()

	context['problemset'] = l

	return render(request, 'offlineProblemSolve/problem_list.html', context)

def show_problem(request, pk=None):
	try:

		problem = problemset.objects.get(pk=pk)

		if request.method == 'POST':
			form = UploadFileForm(request.FILES['datafile'])
			if form:
				language = request.POST['filetype']
				uploaded_file = request.FILES['datafile']
				problem_id = problem
				instance = submission(problem_id=problem_id, user_id=request.user, uploaded_file=uploaded_file, language=language)
				instance.save()
				offline_submission_ack.delay(instance.pk)
				# redirect to submission page

				return HttpResponseRedirect(reverse('show_submission'))
		context = {}

		if request.user.is_authenticated:
			context['username'] = request.user.username
		
		context['problem'] = problem

		return render(request, 'offlineProblemSolve/show_problem.html', context)

	except ObjectDoesNotExist:
		return render(request, 'home/404.html')

def show_submission(request):
	context = {}

	if request.user.is_authenticated:
		context['username'] = request.user.username
	l = submission.objects.all().order_by('-submission_time')
	context['submission'] = l

	return render(request, 'offlineProblemSolve/show_submission.html', context)

def individual_submission(request, pk=None):
	try:
		context = {}
		if request.user.is_authenticated:
			context['username'] = request.user.username

		q = submission.objects.get(pk=pk)
		f = open(str(q.uploaded_file), 'r')

		file_content = f.read()
		f.close()

		context['file_content'] = file_content
		context['submission'] = q
		return render(request, 'offlineProblemSolve/individual_submission.html', context)
	
	except:
		return render(request, 'home/404.html')
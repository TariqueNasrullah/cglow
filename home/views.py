from django.shortcuts import render

# Create your views here.

def home(request):
	context = {}
	if request.user.is_authenticated:
		context['username'] = request.user.username
	return render(request, 'home/home.html', context)

def user_profile(request):
	context = {}
	if request.user.is_authenticated:
		context['username'] = request.user.username
		context['first_name'] = request.user.first_name
		context['last_name'] = request.user.last_name
		context['email'] = request.user.email
		context['solved'] = 0
		context['contest'] = 0
		context['ratting'] = 0
	return render(request, 'home/profile.html', context)
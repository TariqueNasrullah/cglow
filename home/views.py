from django.shortcuts import render

# Create your views here.

def home(request):
	context = {}
	if request.user.is_authenticated:
		context['username'] = request.user.username
	return render(request, 'home/home.html', context)
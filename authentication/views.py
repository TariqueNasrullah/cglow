from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

def user_logout(request):
	logout(request)

	return HttpResponseRedirect(reverse('home'))

def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('home'))


	if request.method == 'POST':
		user_name = request.POST['user_name']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		hashed_password = request.POST['password']
		confirmed_hashed_password = request.POST['confirm_password']

		error = {}

		if User.objects.filter(username=user_name).count() != 0:
			error['user_error'] = "Username Already Exists"
		if hashed_password != confirmed_hashed_password:
			error['password_missmatch'] = "Passwords Didn't Match"

		if len(error):
			return render(request, 'authentication/registrations.html', error)

		u = User.objects.create_user(username=user_name,email=email, password=hashed_password, first_name=first_name, last_name=last_name)
		u.save()
		currentuser = authenticate(username=user_name, password=hashed_password)

		if currentuser:
			if currentuser.is_authenticated:
				auth_login(request, currentuser)
				return HttpResponseRedirect(reverse('home'))
			else:
				return HttpResponse("Your Account is not active")
		else:
			HttpResponse("Something Wrong Happened")

	else:
		return render(request, 'authentication/registrations.html')



def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('home'))

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		error = {}
		if user:
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect(reverse('home'))
			else:
				error['message'] = "Disabled Account"
				return render(request, 'authentication/login.html', error)
		else:
			error['message'] = "Invalid Username or Password"
			return render(request, 'authentication/login.html', error)
	else:
		return render(request, 'authentication/login.html')

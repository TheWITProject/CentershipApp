from django.shortcuts import  render, redirect
from .forms import NewMenteeForm, NewMentorForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# for register page...so only needs to get?
def register_request(request):
	if request.method == "GET":
		return render(request=request, template_name="register.html")
	# if request.method == "POST":
	# 	form = NewUserForm(request.POST)
	# 	if form.is_valid():
	# 		user = form.save()
	# 		login(request, user)
	# 		messages.success(request, "Registration successful." )
	# 		return redirect("profiles:homepage")
	# 	messages.error(request, "Unsuccessful registration. Invalid information.")
	# form = NewUserForm()
	# return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in as {username}.")
				return redirect("profiles:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

# for the mentor signup page
def mentor_request(request):
	if request.method == "POST":
		form = NewMentorForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("profiles:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewMentorForm()
	return render (request=request, template_name="mentor_signup.html", context={"register_form":form})

# for the mentee signup page
def mentee_request(request):
	if request.method == "POST":
		form = NewMenteeForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("profiles:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewMenteeForm()
	return render (request=request, template_name="mentee_signup.html", context={"register_form":form})
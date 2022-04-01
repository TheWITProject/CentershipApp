from django.shortcuts import render

from profiles.forms import SignupForm

def signup(request):
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'signup.html', context={})
    else:
      form = SignupForm()
      return render(request, 'signup.html', context={})
  else:
    form = SignupForm()
    return render(request, 'signup.html', context={})
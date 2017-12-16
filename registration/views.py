from django.shortcuts import render, redirect
from registration.forms import RegistrationForm

# Create your views here.

def index(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration/registered')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'registration/index.html', args)

def registered(request):
    return render(request, 'registration/registered.html')
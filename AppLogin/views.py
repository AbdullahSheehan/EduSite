from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def signupUser(req):
    form = SignUpForm()
    return render(req, 'AppLogin/signupUser.html', context={'form':form})
def loginUser(req):
    return render (req,'AppLogin/loginUser.html', context={})
@login_required
def logoutUser(req):
    logout(req)
    return HttpResponseRedirect(reverse('homepage'))  
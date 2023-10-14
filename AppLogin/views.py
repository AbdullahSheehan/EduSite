from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import StudnetProfile, TeacherProfile
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def signupUser(req):
    form = SignUpForm()
    if req.method == 'POST':
        form = SignUpForm (req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            acc_type = form.cleaned_data.get('type')
            user.is_teacher = True if acc_type == '2' else False
            user.is_student = True if acc_type == '1' else False
            user.save()
            return HttpResponseRedirect(reverse('AppLogin:login'))
    return render(req, 'AppLogin/signupUser.html', context={'form':form})
def loginUser(req):
    form = AuthenticationForm()
    if(req.method == 'POST'):
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if(user is not None):
                login(req, user)
                if(user.is_teacher):
                    if not TeacherProfile.objects.get(user=user).is_complete():
                        messages.warning(req, "Please complete your profile before you move on.")
                        return HttpResponseRedirect(reverse('AppLogin:editprofile'))
                        #print("NOT COMPLETED")
                elif(user.is_student):
                    if not StudnetProfile.objects.get(user=user).is_complete():
                        messages.warning(req, "Please complete your profile before you move on.")
                        return HttpResponseRedirect(reverse('AppLogin:editprofile'))
                        #print("NOT COMPLETED")
    return render (req,'AppLogin/loginUser.html', context={'form':form})
@login_required
def logoutUser(req):
    logout(req)
    return HttpResponseRedirect(reverse('AppLogin:login'))

@login_required
def editprofileUser(req):
    form = 1
    return render(req, 'AppLogin/editprofile.html', context={'form':form})
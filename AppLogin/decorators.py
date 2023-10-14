from functools import wraps
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
def student_test(user):
    return True if user.is_student else False
def teacher_test(user):
    return True if user.is_teacher else False
def student_required():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(req, *args, **kwargs):
            if not student_test(req.user):
                messages.warning(req, "You are not allowed to view this page!")
                return HttpResponseRedirect(reverse('homepage'))
            return view(req, *args, **kwargs)
        return _wrapped_view
    return decorator
def teacher_required():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(req, *args, **kwargs):
            if not teacher_test(req.user):
                messages.warning(req, "You are not allowed to view this page!")
                return HttpResponseRedirect(reverse('homepage'))
            return view(req, *args, **kwargs)
        return _wrapped_view
    return decorator
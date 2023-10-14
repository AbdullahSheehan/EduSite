from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

def index(req):
    return HttpResponseRedirect(reverse('AppBlog:articles')) 
from django.shortcuts import render, HttpResponseRedirect
from .forms import ArticleForm, AddCategory
from .models import Article
from uuid import uuid4
from django.urls import reverse
from django.views.generic import ListView, DetailView
# Create your views here.
def createArticle(req):
    form = AddCategory()
    if req.method == 'POST':
        form = AddCategory(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('AppBlog:createblog'))
    form2 = ArticleForm()
    if req.method == 'POST':
        form2 = ArticleForm(req.POST, req.FILES)
        if form2.is_valid():
            obj = form2.save(commit=False)
            obj.author = req.user
            title = obj.title
            obj.slug = title.replace(' ', '-') + "-" + str(uuid4())
            obj.save()
            return HttpResponseRedirect(reverse('homepage'))
    return render(req, 'AppBlog/createArticle.html', context={'category':form,'form':form2})

class ArticleList(ListView):
    model = Article
    template_name = "AppBlog/articlelist.html"
    context_object_name = 'articles'

class ArticleDetail(DetailView):
    model = Article
    template_name = "AppBlog/articledetail.html"
    context_object_name = 'article'
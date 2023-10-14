from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from AppLogin.decorators import student_required, teacher_required
# Create your views here.
def ForumCreate(req):
    form = QuestionForm()
    if req.method == 'POST':
        form = QuestionForm(req.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.student = req.user
            obj.save()
            return HttpResponseRedirect(reverse('AppForum:forumlist'))
    return render(req, 'AppForum/ask_question.html', context={'form':form})
class ForumList(ListView):
    model = Question
    template_name = "AppForum/forumlist.html"
    context_object_name = 'questions'

def forumdetails(req, pk):
    question = Question.objects.get(pk=pk)
    answer = Answer.objects.filter(question=question)
    form = AnswerForm()
    if req.method == 'POST':
        form = AnswerForm(req.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.teacher = req.user
            obj.question = question
            obj.save()
            return HttpResponseRedirect(reverse('AppForum:details', kwargs={'pk':pk}))
    return render(req, 'AppForum/questiondetails.html', context={'question':question, 'answers':answer, 'form':form})

@student_required()
def myquestions(req):
    question = Question.objects.filter(student=req.user)
    return render(req, 'AppForum/myquestions.html', context={'questions':question})
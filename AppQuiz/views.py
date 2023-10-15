from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Quiz, MCQ, Result
from django.views.generic import ListView
from .forms import CreateQuiz, CreateMCQ, ResultForm
from AppLogin.decorators import teacher_required, student_required
# Create your views here.

class AllQuiz(ListView):
    model = Quiz
    template_name = 'AppQuiz/allquiz.html'
    context_object_name = 'quizes'
@teacher_required()
def MyQuiz(req):
    quizes = Quiz.objects.filter(teacher=req.user)
    return render(req, 'AppQuiz/myquiz.html', context={'quizes':quizes})

@teacher_required()
def create_quiz(req):
    form = CreateQuiz()
    if req.method == "POST":
        form = CreateQuiz(req.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.teacher = req.user
            quiz.save()
            return HttpResponseRedirect(reverse('AppQuiz:myquizes'))
    return render(req, 'AppQuiz/createquiz.html', context={'form':form})

def quiz_details(req, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(req, 'AppQuiz/quizdetails.html', context={'quiz':quiz})

@teacher_required()
def customize_quiz(req, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = MCQ.objects.filter(quiz=quiz, teacher=req.user)
    form = CreateMCQ()
    if req.method == "POST":
        form = CreateMCQ(req.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.teacher = req.user
            question.save()
            return HttpResponseRedirect(reverse('AppQuiz:customizequiz', kwargs={'pk':pk}))
    return render(req, 'AppQuiz/customizequiz.html', context={'quiz':quiz, 'questions':questions, 'form':form})
@student_required()
def givequiz(req, pk):
    quiz = Quiz.objects.get(pk=pk)
    ques = MCQ.objects.filter(quiz=quiz)
    questions = [x.question for x in ques]
    answers = [str(x.correctOption) for x in ques]
    score = 0
    form = ResultForm()
    if(req.method == 'POST'):
        form = ResultForm(req.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.quiz = quiz
            obj.student = req.user
            data = req.POST
            for i in range(len(questions)):
                if(data[questions[i]] == answers[i]):
                    score += 1
            obj.score = score
            print(obj)
            obj.save()
    return render(req, 'AppQuiz/thequiz.html', context={'ques':ques, 'quiz':quiz, 'score':score, 'form':form})
@teacher_required()
def quizresult(req, pk):
    quiz = Quiz.objects.get(pk=pk)
    results = Result.objects.filter(quiz=quiz)
    return render(req, 'AppQuiz/quizresults.html', {'results':results,'quiz':quiz})
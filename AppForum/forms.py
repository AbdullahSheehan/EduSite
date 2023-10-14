from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'detail']
        labels = {
            'question':"Question Title",
            'detail':'Details about your question'
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields = ['answer']
        labels = {
            'answer' : 'Answer this question'
        }
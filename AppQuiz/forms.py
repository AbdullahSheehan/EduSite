from .models import Quiz, MCQ, Result
from django import forms

class CreateQuiz(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']
        labels = {
            'title':'Quiz Name',
            'description': 'Quiz Description',
            'duration': 'Duration (in minutes)'
        }
class CreateMCQ(forms.ModelForm):
    class Meta:
        model = MCQ
        fields = [
            'question',
            'option1',
            'option2',
            'option3',
            'option4',
            'correctOption',
        ]
        labels = {
            'question': 'Question',
            'option1': 'Option 1',
            'option2': 'Option 2',
            'option3': 'Option 3',
            'option4': 'Option 4',
            'correctOption': "Correct Answer(1-4)",
        }

class ResultForm(forms.ModelForm):
    class Meta:
        model= Result
        exclude = ['quiz', 'student', 'score']
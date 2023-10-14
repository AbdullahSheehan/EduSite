from django import forms
from .models import Article, Category
class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'category', 'content', 'poster')
        labels = {
            'title': 'Article Title',
            'content': 'Article',
            'poster': 'Article Poster',
        }
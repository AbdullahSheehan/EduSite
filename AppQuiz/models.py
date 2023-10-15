from django.db import models
from django.conf import settings
# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacherquiz')
    description = models.TextField()
    duration = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Quiz: {self.title}"
class MCQ(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teachermcq')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quizmcq')
    question = models.CharField(max_length=2000)
    option1  = models.CharField(max_length=2000)
    option2   = models.CharField(max_length=2000)
    option3 = models.CharField(max_length=2000)
    option4 = models.CharField(max_length=2000)
    correctOption = models.IntegerField()
    
    def __str__(self):
        return f"Question: {self.question}"

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quizresult')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='studentresult')
    score = models.IntegerField()
    # time = models.IntegerField()
    def __str__(self):
        return f"{self.student}'s Score = {self.score}"
    class Meta:
        ordering = ['-score']
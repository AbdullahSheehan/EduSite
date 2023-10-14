from django.db import models
from django.conf import settings
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
    
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogauthor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogcategory')
    title = models.CharField(max_length=300)
    content = models.TextField()
    slug = models.SlugField(max_length=600, unique=True)
    poster = models.ImageField(upload_to='Blog_Posters/')

    publish = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-publish']
    def __str__(self):
        return f"{self.title} by {self.author}"
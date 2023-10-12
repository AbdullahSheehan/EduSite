from django.contrib import admin
from .models import User, StudnetProfile, TeacherProfile
# Register your models here.
admin.site.register(User)
admin.site.register(StudnetProfile)
admin.site.register(TeacherProfile)
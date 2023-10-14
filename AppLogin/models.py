from django.db import models

# For Custom User Model
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy

# For creating profile when a user is created
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:                                           # Ensuring email is given
            raise ValueError("Email Must be given!")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):                         # Basic User Structure
    first_name = models.CharField(verbose_name=("First Name"), max_length=150, blank=True)
    last_name = models.CharField(verbose_name=("Last Name"), max_length=150, blank=True)
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(
        gettext_lazy('staff status'),
        default=False,
        help_text = gettext_lazy('Designates whether the user can log in this site')
    )

    is_active = models.BooleanField(
        gettext_lazy('active'),
        default=True,
        help_text=gettext_lazy('Designates whether this user should be treated as active. Unselect this instead of deleting accounts')
    )

    is_teacher = models.BooleanField(
        gettext_lazy('Teacher Status'),
        default=False,
        help_text="Designates whether this user is a teacher"
    )

    is_student = models.BooleanField(
        gettext_lazy('Student Status'),
        default=False,
        help_text="Designates whether this user is a student"
    )
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        if(self.is_teacher):
            return f"Teacher: {self.first_name} {self.last_name}"
        elif(self.is_student):
            return f"Student: {self.first_name} {self.last_name}"
        else:
            return self.email

class StudnetProfile(models.Model):                                     # Student Profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='studentprofile')
    profilepic = models.ImageField(upload_to='students/', blank=True, null=True)
    clas = models.IntegerField(blank=True, null=True)
    institute = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Student: {self.user.first_name} {self.user.last_name}"
    
    def is_complete(self):
        return True if (self.clas and self.institute and self.city and self.contact) else False
class TeacherProfile(models.Model):                                     # Teacher Profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacherprofile')
    profilepic = models.ImageField(upload_to='teachers/', blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Teacher: {self.user.first_name} {self.user.last_name}"
    def is_complete(self):
        return True if (self.subject and self.contact) else False
@receiver(post_save, sender=User)               # Creating a profile object when a user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        if(instance.is_teacher):            # Checking if the user is a teacher
            TeacherProfile.objects.create(user=instance)
        elif(instance.is_student):          # Checking if the user is a student
            StudnetProfile.objects.create(user=instance)

@receiver(post_save, sender=User)            # Saving the profile object
def save_profile(sender, instance, **kwargs):
    if(instance.is_teacher):            # Checking if the user is a teacher
        instance.teacherprofile.save()
    elif(instance.is_student):          # Checking if the user is a student
        instance.studentprofile.save()

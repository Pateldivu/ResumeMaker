from typing import ClassVar
from django.db import models
from django.core import validators

# Board/University Model
class Board_University(models.Model):
    Name = models.CharField(max_length=50)
    Location = models.TextField(max_length=100)

    class Meta:
        db_table = 'BoardOrUniversity'
        verbose_name_plural = 'Board Or Universities'

# Course/Stream
class Course_Stream(models.Model):
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=10)
    Duration = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(4)])

    class Meta:
        db_table = 'Course Or Stream'


# Create your models here.
class Master(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False) 
    
    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email

class User(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    
    Image = models.FileField(upload_to="users/profile/", default="avatar.png")
    About = models.TextField(max_length=255, default="")
    FullName = models.CharField(max_length=30, default="")
    Mobile = models.CharField(max_length=10, default="")
    BirthDate = models.DateField(auto_now=True)
    Country = models.CharField(max_length=20, default="")
    State = models.CharField(max_length=20, default="")
    City = models.CharField(max_length=20, default="")
    Address = models.TextField(max_length=255, default="")

    class Meta:
        db_table = 'user'

class Education(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    
    BoardUniversity = models.ForeignKey(Board_University, on_delete=models.CASCADE)
    CourseStream = models.ForeignKey(Course_Stream, on_delete=models.CASCADE)
    StartDate = models.DateField(auto_now=True)
    EndDate = models.DateField(auto_now=True)
    Score = models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[validators.MinValueValidator(0.00)])
    IsPercent = models.BooleanField(default=True)
    Description = models.CharField(max_length=100)
    IsCompleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'education'

class Skill(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Skill = models.CharField(max_length=50)
    Level = models.CharField(max_length=100)

    class Meta:
        db_table = 'skill'

class Experience(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    JobTitle = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    StartDate = models.DateField(auto_now=True)
    EndDate = models.DateField(auto_now=True)
    Description = models.CharField(max_length=100)

    class Meta:
        db_table = 'experience'


class Project(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    # Image = models.FileField(upload_to="projects/", default="project.png")
    Title = models.CharField(max_length=50)
    Category = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)

    class Meta:
        db_table = 'project'

class Reference(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Link = models.URLField(max_length=100)
    Description = models.CharField(max_length=100)

    class Meta:
        db_table = 'reference'
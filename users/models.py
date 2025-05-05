from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # related_name bilan to'qnashuv oldini olish
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set_permissions',  # related_name bilan to'qnashuv oldini olish
        blank=True
    )

    def save(self, *args, **kwargs):
        # Parol allaqachon hashlanganmi tekshirish
        if self.pk is None or not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)



class Teacher(CustomUser):
    GRADES = (
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior')
    )
    rating = models.IntegerField(default=1)
    grade = models.CharField(max_length=50, choices=GRADES, default='Junior')
    salary = models.IntegerField(default=0)
    phone = models.CharField(max_length=13)

class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name

class Group(models.Model):
    DAYS = (
        ('Even', 'Even'),
        ('Odd', 'Odd'),
        ('Weekend', 'Weekend')
    )
    name = models.CharField(max_length=50, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    day = models.CharField(max_length=10, choices=DAYS)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    start_date = models.DateField()
    end_date = models.DateField()
    start_lesson_time = models.TimeField()
    end_lesson_time = models.TimeField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Student(CustomUser):
    LIGAS = (
        ('Hacker', 'Hacker'),
        ('Coder', 'Coder'),
        ('Gamer', 'Gamer')
    )
    liga = models.CharField(max_length=50, choices=LIGAS)
    power = models.IntegerField(default=0)
    strike = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group')
    phone = models.CharField(max_length=13)


class Admin(CustomUser):
    salary = models.IntegerField(default=0)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='admin')
    phone = models.CharField(max_length=13)
    kpi = models.IntegerField(default=0)

class Methodist(CustomUser):
    salary = models.IntegerField(default=0)
    phone = models.CharField(max_length=13)
    kpi = models.IntegerField(default=0)

class Instructor(CustomUser):
    salary = models.IntegerField(default=0)
    phone = models.CharField(max_length=13)
    kpi = models.IntegerField(default=0)



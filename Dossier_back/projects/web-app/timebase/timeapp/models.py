from django.db import models
from django.contrib.auth.models import User

#Course = cours
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

#Schedule = Emploi du temps
class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

#Student = Etudiant
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

#Teacher = Professeur
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

#Room = Salle de classe
class Room(models.Model):
    name = models.CharField(max_length=100)

#Department = Filière
class Department(models.Model):
    name = models.CharField(max_length=100)

#Group = Goupe
class Group(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


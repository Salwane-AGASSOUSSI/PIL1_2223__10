from django.shortcuts import render, get_object_or_404
from .models import Course, Schedule, Student, Teacher, Department, Group

def index(request):
    return render(request, 'index.html')

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule_list.html', {'schedules': schedules})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    students = Student.objects.filter(group=group)
    return render(request, 'group_detail.html', {'group': group, 'students': students})




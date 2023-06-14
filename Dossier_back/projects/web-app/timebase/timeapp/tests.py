from django.test import TestCase
from django.urls import reverse

from .models import Course, Schedule, Student, Teacher, Room, Department, Group


class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            code='COMP101',
            name='Introduction to Computer Science',
            department='Computer Science'
        )
        self.assertEqual(course.code, 'COMP101')
        self.assertEqual(course.name, 'Introduction to Computer Science')
        self.assertEqual(course.department, 'Computer Science')


class ScheduleModelTest(TestCase):
    def test_schedule_creation(self):
        course = Course.objects.create(
            code='COMP101',
            name='Introduction to Computer Science',
            department='Computer Science'
        )
        schedule = Schedule.objects.create(
            course=course,
            day='Monday',
            start_time='09:00',
            end_time='11:00'
        )
        self.assertEqual(schedule.course, course)
        self.assertEqual(schedule.day, 'Monday')
        self.assertEqual(schedule.start_time, '09:00')
        self.assertEqual(schedule.end_time, '11:00')


class StudentModelTest(TestCase):
    def test_student_creation(self):
        student = Student.objects.create(
            name='John Doe',
            department='Computer Science',
            group='A'
        )
        self.assertEqual(student.name, 'John Doe')
        self.assertEqual(student.department, 'Computer Science')
        self.assertEqual(student.group, 'A')


class TeacherModelTest(TestCase):
    def test_teacher_creation(self):
        teacher = Teacher.objects.create(
            name='Jane Smith',
            department='Computer Science'
        )
        self.assertEqual(teacher.name, 'Jane Smith')
        self.assertEqual(teacher.department, 'Computer Science')


class RoomModelTest(TestCase):
    def test_room_creation(self):
        room = Room.objects.create(
            number='101',
            capacity=30,
            building='Main Building'
        )
        self.assertEqual(room.number, '101')
        self.assertEqual(room.capacity, 30)
        self.assertEqual(room.building, 'Main Building')


class DepartmentModelTest(TestCase):
    def test_department_creation(self):
        department = Department.objects.create(
            name='Computer Science',
            code='CS'
        )
        self.assertEqual(department.name, 'Computer Science')
        self.assertEqual(department.code, 'CS')


class GroupModelTest(TestCase):
    def test_group_creation(self):
        department = Department.objects.create(
            name='Computer Science',
            code='CS'
        )
        group = Group.objects.create(
            name='A',
            department=department
        )
        self.assertEqual(group.name, 'A')
        self.assertEqual(group.department, department)


class ViewsTest(TestCase):
    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to the Timetable App')




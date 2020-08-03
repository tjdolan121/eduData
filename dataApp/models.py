from django.db import models
from django.urls import reverse

# Create your models here.

GRADES = (('A+', 'A+'), ('A', 'A'), ('A-', 'A-'),
          ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'),
          ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'),
          ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'),
          ('F', 'F'))

CREDITS = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'))


class Student(models.Model):
    fname = models.CharField(max_length=50, default='')
    lname = models.CharField(max_length=50, default='')
    enrolled_since = models.DateField()

    def __str__(self):
        return self.fname + ' ' + self.lname

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])


class Course(models.Model):
    dept = models.CharField(max_length=4)
    num = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    credits = models.IntegerField(choices=CREDITS, default=3)

    def __str__(self):
        return self.dept + ' ' + self.num

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])


class Grade(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    letter_grade = models.CharField(max_length=5, choices=GRADES)

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Course, Grade


############# HOME VIEW  ################

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


############# LIST VIEWS ################


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_list.html'


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'course_list.html'


class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'grade_list.html'


############# DETAIL VIEWS ################


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student_detail.html'


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course_detail.html'


class GradeDetailView(LoginRequiredMixin, DetailView):
    model = Grade
    template_name = 'grade_detail.html'


############# CREATE VIEWS ################

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'student_create.html'
    fields = ('fname', 'lname', 'enrolled_since')


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'course_create.html'
    fields = ('dept', 'num', 'name', 'credits')


class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    template_name = 'course_create.html'
    fields = ('sid', 'course', 'letter_grade')
    success_url = reverse_lazy('grade_list')


############# UPDATE VIEWS ################


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ('fname', 'lname', 'enrolled_since')
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student_list')


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ('dept', 'num', 'name', 'credits')
    template_name = 'course_edit.html'
    success_url = reverse_lazy('course_list')


class GradeUpdateView(LoginRequiredMixin, UpdateView):
    model = Grade
    fields = ('sid', 'course', 'letter_grade')
    template_name = 'grade_edit.html'
    success_url = reverse_lazy('grade_list')


############# DELETE VIEWS ################


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student_list')


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course_list')


class GradeDeleteView(LoginRequiredMixin, DeleteView):
    model = Grade
    template_name = 'grade_delete.html'
    success_url = reverse_lazy('grade_list')

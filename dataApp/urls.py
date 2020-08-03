from django.contrib import admin
from django.urls import path, include

from .views import HomePageView, StudentListView, CourseListView, GradeListView, StudentUpdateView, CourseUpdateView, \
    GradeUpdateView, StudentDeleteView, CourseDeleteView, GradeDeleteView, StudentDetailView, CourseDetailView, \
    GradeDetailView, StudentCreateView, CourseCreateView, GradeCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('students', StudentListView.as_view(), name="student_list"),
    path('courses', CourseListView.as_view(), name="course_list"),
    path('grades', GradeListView.as_view(), name="grade_list"),
    path('students/<int:pk>', StudentDetailView.as_view(), name="student_detail"),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name="student_edit"),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name="student_delete"),
    path('students/new/', StudentCreateView.as_view(), name="student_create"),
    path('courses/<int:pk>', CourseDetailView.as_view(), name="course_detail"),
    path('courses/<int:pk>/edit/', CourseUpdateView.as_view(), name="course_edit"),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name="course_delete"),
    path('courses/new/', CourseCreateView.as_view(), name="course_create"),
    path('grades/<int:pk>', GradeDetailView.as_view(), name="grade_detail"),
    path('grades/<int:pk>/edit/', GradeUpdateView.as_view(), name="grade_edit"),
    path('grades/<int:pk>/delete/', GradeDeleteView.as_view(), name="grade_delete"),
    path('grades/new/', GradeCreateView.as_view(), name="grade_create"),
]

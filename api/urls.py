from django.urls import path

from .views import HomeAPIView, StudentAPIView, CourseAPIView, GradeAPIView

urlpatterns = [
    path('', HomeAPIView.as_view(), name='api_home'),
    path('students', StudentAPIView.as_view(), name='api_students'),
    path('courses', CourseAPIView.as_view(), name='api_courses'),
    path('grades', GradeAPIView.as_view(), name='api_grades'),
]

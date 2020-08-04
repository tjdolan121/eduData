from rest_framework import generics

from django.views.generic import TemplateView

from dataApp.models import Student, Course, Grade
from .serializers import StudentSerializer, CourseSerializer, GradeSerializer


class HomeAPIView(TemplateView):
    template_name = 'api.html'


class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GradeAPIView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

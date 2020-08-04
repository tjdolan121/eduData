from rest_framework import serializers

from dataApp.models import Student, Course, Grade


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'fname', 'lname', 'enrolled_since')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'dept', 'num', 'name', 'credits')


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'sid', 'course', 'letter_grade')

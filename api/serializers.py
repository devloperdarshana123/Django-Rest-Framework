from rest_framework import serializers
from rohii.models import Rohii
from employees.models import Employee
from blogs.models import Blog, Comment  # Import models once

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rohii
        fields = '__all__'  # or specify required fields

# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# Blog Serializer
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

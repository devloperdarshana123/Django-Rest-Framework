from rest_framework import serializers
from rohii.models import Rohii
from employees.models import Employee


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rohii
        fields = '__all__'  # or specify the fields you want to include, e.g
        
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' 
        

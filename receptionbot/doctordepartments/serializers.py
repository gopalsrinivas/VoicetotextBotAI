from rest_framework import serializers
from .models import *


class DrDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrDepartment
        fields = '__all__'


class DoctorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetails
        fields = '__all__'

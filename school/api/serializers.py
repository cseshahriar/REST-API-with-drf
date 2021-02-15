from rest_framework import serializers
from school.models import Student, Profile, School, Klass

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class KlsddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['school'] = SchoolSerializer(instance.school).data #m2o
        response['student'] = StudentSerializer(
            instance.student, many=True).data # m2m
        return response

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'url'
        )


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'title', 'status', 'created_by', 'start_date', 'end_date')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer_text')

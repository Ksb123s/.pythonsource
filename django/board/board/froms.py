from .models import Question,Answer
from django import forms


class QuestionFrom(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]

class AnswerFrom(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
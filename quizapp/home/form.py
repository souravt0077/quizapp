from django.forms import ModelForm
from .models import quizModel

class addQuestionForm(ModelForm):
    class Meta:
        model=quizModel
        fields='__all__'
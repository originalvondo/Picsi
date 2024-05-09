from django.forms import ModelForm
from .models import Pic

class CreatePicForm(ModelForm):
    class Meta:
        model = Pic
        fields = ['title', 'image']
from django import forms
from board.models import *


class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':22}), label="Описание")

    class Meta:
        model = Task
        fields = ('description', 'priority', 'assigned', 'status')

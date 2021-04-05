from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput({
        'placeholder': 'Add your new todo',
    }))
    completed = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    class Meta:
        model = Todo
        fields = ['title', 'completed']
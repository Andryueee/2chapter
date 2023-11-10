from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, CharField, Select, EmailInput
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'name', 'email', 'category']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название заявки'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание заявки'
            }),
            "category": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
        }
from django.forms import ModelForm
from .models import Post
from django import forms


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'body', 'tags']
        labels = {
            'body': 'Комментарий',
            'tags': 'Категории'
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Добавьте Ваш комментарий...',
                'class': 'font1 text-4xl'}),
            'image': forms.TextInput(attrs={
                'placeholder': 'Укажите адрес картинки...'}),
            'tags': forms.CheckboxSelectMultiple(),
        }


class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body': '',
            'tags': 'Категории',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'class': 'font1 text-4xl'}),
            'tags': forms.CheckboxSelectMultiple(),
        }


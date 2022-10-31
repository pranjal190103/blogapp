from dataclasses import fields
from django import forms
from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']
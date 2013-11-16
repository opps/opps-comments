#coding: utf-8

from django import forms
from .models import Comment


class CommentsForm(forms.ModelForm):
    path = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ["author_name", "author_email", "path", "body"]

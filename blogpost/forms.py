from django import forms
from django.db.models.fields import DateTimeField
from django.forms import widgets
from blogpost.models import Post


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("author","title","body" )
        widgets={
            'author': forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }








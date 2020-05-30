from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta:
        model=Blog
        # fields='__all__'   #모든 항목 입력시 
        fields=['title','body']
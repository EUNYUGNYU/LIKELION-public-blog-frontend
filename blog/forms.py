from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta: #메타 클래스
        model=Blog
        fields=['title','body','photo'] #항목지정가능
        # fields='__all__'   #모든 항목 입력 가능


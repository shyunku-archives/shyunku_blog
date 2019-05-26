from django import forms
from django_summernote import fields as summer_fields
from .models import SummerNote


class UserForm(forms.Form):
    user_id = forms.CharField(label='id', max_length=15)
    user_nickname = forms.CharField(label='nickname', max_length=20)
    user_pw = forms.CharField(label='pw', max_length=15)


class PostForm(forms.ModelForm):
    fields = summer_fields.SummernoteTextFormField(error_messages={'required': (u'데이터를 입력해주세요'), })

    class Meta:
        model = SummerNote
        fields = ('fields',)
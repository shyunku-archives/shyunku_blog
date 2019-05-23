from django import forms


class UserForm(forms.Form):
    user_id = forms.CharField(label='id', max_length=15)
    user_nickname = forms.CharField(label='nickname', max_length=20)
    user_pw = forms.CharField(label='pw', max_length=15)
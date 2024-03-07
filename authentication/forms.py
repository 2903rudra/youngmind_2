from django import forms
from .models import *

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices = CustomUser.User_choice)


class CollegeSPOCSignupForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'

class CollegeStudentSignupForm(forms.ModelForm):
    class Meta:
        model = CollegeStudent
        fields = '__all__'

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'
        exclude = ['user','team_name']


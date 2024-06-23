from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PublicQuestions, Users, Leaderboard
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class AddQuestionsForm(forms.ModelForm):
    title = forms.CharField(max_length=1000, required=True)
    a = forms.CharField(max_length=100, required=True)
    b = forms.CharField(max_length=100, required=True)
    c = forms.CharField(max_length=100, required=True)
    d = forms.CharField(max_length=100, required=True)
    correct_answer = forms.CharField(max_length = 1, required=True)
    diff = forms.CharField(max_length=20, required=True)
    topic = forms.CharField(max_length=100, required=True)

    class Meta:
        model = PublicQuestions
        fields = ['title', 'a', 'b', 'c', 'd', 'correct_answer', 'diff', 'topic']

class UserCreateForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ['username', 'password1', 'password2', 'points']

    def clean_password(self):
        password = self.cleaned_data.get("password1")
        if password:
            try:
                validate_password(password, self.instance)
            except ValidationError as e:
                self.add_error('password1', e)
        return password

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'password']

class PointsForm(forms.ModelForm):
    username = forms.CharField(max_length = 100)
    points = forms.IntegerField()

    class Meta:
        model = Leaderboard
        fields = ['username', 'points']
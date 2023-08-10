# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
 
# 회원 가입 폼
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
 
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'old', 'phone', 'address', 'email', 'volunteer', 'followings')
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            accounts = get_user_model().objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")
 
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            accounts = get_user_model().objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"UserID {username} is already in use.")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'old', 'phone', 'address', 'email')
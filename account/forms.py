from django import forms
from django.contrib.auth.models import User
from .models import Profile 

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        # Save the user instance first
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
    
        user.save()  # Fully save the User instance to the database

        return user
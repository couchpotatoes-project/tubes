from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
    attrs={
        'class': 'form-control',
        'placeholder': 'Enter Email'
    }
    ))
    username = forms.CharField( min_length=5, widget=forms.TextInput(
    attrs={
        'class': 'form-control',
        'placeholder': 'Enter UserName: Should Contain Atleast 5 characters'
    }
    ))
    password1 = forms.CharField( min_length=8, label="Password",widget=forms.PasswordInput(
    attrs={
        'class': 'form-control',
       'placeholder': 'Enter Password: Should Contain Atleast 8 characters'
    }
    ))
    password2 = forms.CharField( label="Confirm Password",widget=forms.PasswordInput(
    attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }
    ))
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2')

    def clean_email(self):
            email = self.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                raise forms.ValidationError("This email address already exists. Did you forget your password?")
            except User.DoesNotExist:
                return email  

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user
		
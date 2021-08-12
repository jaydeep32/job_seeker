from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from user.models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder': 'Username', 'onfocus':"this.placeholder = ''" ,'onblur':"this.placeholder = 'Username'"}
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder': 'Password', 'onfocus':"this.placeholder = ''" ,'onblur':"this.placeholder = 'Password'"}
        ))

    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', )
        widgets = {
            'about': forms.Textarea(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'About your self',
                                        }),
            'address': forms.Textarea(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Address',
                                            'rows': 2,
                                        }),
        }


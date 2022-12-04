from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
from captcha.fields import CaptchaField, CaptchaTextInput


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'label_suffix' not in kwargs:
            kwargs['label_suffix'] = ''
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category"

    class Meta:
        model = FilmReview
        fields = ['title', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'add_review__form',
                                            'placeholder': "Title"}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 15,
                                             'class': 'add_review__form',
                                             'placeholder': "Text"}),
            'photo': forms.FileInput(attrs={'class': 'add_review__form add_review__img',
                                            'placeholder': ""}),
            'is_published': forms.CheckboxInput(attrs={'class': 'add_review__form add_review__publish '
                                                                'add_review__checkbox'}),
            'cat': forms.Select(attrs={'class': 'add_post_form'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Your title is too long")
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'reg_log__form form_input_register',
                                                                       'placeholder': "Username"}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'reg_log__form form_input_register',
                                                                      'placeholder': "Email"}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'reg_log__form '
                                                                                     'form_input_register',
                                                                            'placeholder': "Password"}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'reg_log__form '
                                                                                     'form_input_register',
                                                                            'placeholder': "Repeat password"}))
    captcha = CaptchaField(label='', widget=CaptchaTextInput(attrs={'class': 'reg_log__captcha',
                                                                    'placeholder': "CAPTCHA"
                                                                    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'reg_log__form',
                                                                'placeholder': "Username"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'reg_log__form',
                                                                    'placeholder': "Password"}))

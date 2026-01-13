from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

TAILWIND_INPUT_CLASSES = (
    "w-full px-4 py-2 border border-gray-300 rounded-lg "
    "focus:outline-none focus:ring-2 focus:ring-indigo-500 "
    "focus:border-indigo-500 bg-white text-gray-800"
)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'rows': 5,
                'placeholder': 'Write your post content here...'
            }),
            'category': forms.Select(attrs={
                'class': TAILWIND_INPUT_CLASSES
            }),
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': TAILWIND_INPUT_CLASSES
        })
        self.fields['password2'].widget.attrs.update({
            'class': TAILWIND_INPUT_CLASSES
        })

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': TAILWIND_INPUT_CLASSES
        })
        self.fields['password'].widget.attrs.update({
            'class': TAILWIND_INPUT_CLASSES
        })

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter username"}),
            "email": forms.EmailInput(attrs={"placeholder": "johndoe@gmail.com"})
            # password widgets are already PasswordInput by default
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Labels exactly as you want
        self.fields["username"].label = "Name"
        self.fields["email"].label = "Email"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm password"

        # Crispy helper: vertical stack (label above input)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_tag = False          # keep your <form> in template
        # Make each field blocky with spacing
        self.helper.layout = Layout(
            Div(Field("username"), css_class="mb-3"),
            Div(Field("email"), css_class="mb-3"),
            Div(Field("password1"), css_class="mb-3"),
            Div(Field("password2"), css_class="mb-2"),
        )

# - Login User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
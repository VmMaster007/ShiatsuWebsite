from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter username"}),
            # password widgets are already PasswordInput by default
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Labels exactly as you want
        self.fields["username"].label = "Username"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm password"

        # Optional: remove the long default help text
        for name in ("username", "password1", "password2"):
            self.fields[name].help_text = "" #change info text if you want but only for certain field e.g. username

        # Crispy helper: vertical stack (label above input)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_tag = False          # keep your <form> in template
        # Make each field blocky with spacing
        self.helper.layout = Layout(
            Div(Field("username"), css_class="mb-3"),
            Div(Field("password1"), css_class="mb-3"),
            Div(Field("password2"), css_class="mb-2"),
        )

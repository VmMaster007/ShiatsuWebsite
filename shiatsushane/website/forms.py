from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div

class CreateUserForm(UserCreationForm):
    # email = forms.EmailField(
    #     required=True,
    #     help_text="Your email is confidential",
    #     widget=forms.EmailInput(attrs={"placeholder": "johndoe@gmail.com"})
    # )

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

        # Optional: remove the long default help text
        # for name in ("username", "password1", "password2", "email"):
        #     self.fields[name].help_text = "" #change info text if you want but only for certain field e.g. username

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

        # Validate email uniqueness at the form level
        # def clean_email(self):
        #     # email = self.cleaned_data.get("email", "").strip()
        #     if User.objects.filter(email_iexact=email).exists():
        #         raise forms.ValidationError("An account with this email already exists.")
        #     return email
        
        # # Save the email onto the user
        # def save(self, commit=True):
        #     user = super().save(commit=False) # UserCreationForm already set username + password hash
        #     user.email = self.cleaned_data["email"]  # add email
        #     if commit:
        #         user.save()
        #     return user

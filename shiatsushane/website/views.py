# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import CreateUserForm, LoginForm
import logging

# -------------------------------
# Logging setup
# -------------------------------
logging.basicConfig(
    filename="my_log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def home(request):
    """
    Render the homepage and process both auth modals on POST.

    Context keys used by templates:
      - form:           register form instance
      - display:        register modal CSS toggle ("" or "show")
      - login_form:     login form instance
      - login_display:  login modal CSS toggle ("" or "show")

    Notes:
      - Each form in the template must include:
          <input type="hidden" name="form_type" value="register">  (or "login")
      - Modals should use IDs: #register-modal and #login-modal
      - CSS should toggle .modal.show { display:block; }
    """
    logger.info("HOME: view loaded")

    # Initial state (GET): both forms empty, both modals closed
    register_form = CreateUserForm()
    login_form = LoginForm(request)
    display = ""        # register modal ("" closed, "show" open)
    login_display = ""  # login modal   ("" closed, "show" open)

    # ---------------------------------------
    # Handle POST from either modal via form_type
    # ---------------------------------------
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        logger.info(f"POST received for: {form_type}")

        # ----- REGISTER FLOW -----
        if form_type == "register":
            register_form = CreateUserForm(request.POST)

            if register_form.is_valid():
                email = register_form.cleaned_data["email"]

                # Prevent duplicate emails
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists!")
                    display = "show"  # keep register modal open to show message
                else:
                    # Create user
                    user = register_form.save()
                    messages.success(request, "Account created successfully.")

                    # Optional auto-login:
                    # auth_login(request, user)

                    # PRG: redirect to clear POST and avoid resubmits
                    return redirect("home")
            else:
                # Validation errors: keep modal open and show errors
                display = "show"

        # ----- LOGIN FLOW -----
        elif form_type == "login":
            login_form = LoginForm(request, data=request.POST)

            if login_form.is_valid():
                # Log the user in
                auth_login(request, login_form.get_user())
                messages.success(request, "Welcome back!")

                # PRG after success
                return redirect("home")
            else:
                # Validation errors: keep login modal open
                login_display = "show"

    # Render page with whichever modal(s) should be open
    context = {
        "form": register_form,
        "display": display,
        "login_form": login_form,
        "login_display": login_display,
    }
    return render(request, "pages/index.html", context)


def about(request):
    """
    About page: same context keys so templates can include both modals.
    Both modals closed by default.
    """
    context = {
        "form": CreateUserForm(),
        "display": "",
        "login_form": LoginForm(request),
        "login_display": "",
    }
    return render(request, "pages/about.html", context)


def logout(request):
    """
    Simple logout view with a flash message, then return to home.
    """
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")
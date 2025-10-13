# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm

def home(request):
    show_register_modal = False

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("home")  # avoids resubmitting on refresh
        else:
            # Keep the invalid form so errors render
            show_register_modal = True
    else:
        form = CreateUserForm()

    context = {
        "form": form,
        "show_register_modal": show_register_modal,
    }
    return render(request, "pages/index.html", context)

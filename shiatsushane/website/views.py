# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.models import User

# Register Modal Function
def register(request):

    form = CreateUserForm() # brings form through to view
    display = "" # display block later changes form to be on screen/if error

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        print(form.errors) # for debug purposes
        if form.is_valid():
            # checking email exists in data base
            email = form.cleaned_data["email"]
            # print(email) # for debug purposes
            obj = User.objects.filter(email=email).exists()  # check if user with that email
            
            if obj == True:
                messages.error(request, "Email already exists!")
                display = "blockclass"
            else:
                form.save()
                messages.success(request, "Account created successfully.")
                return redirect("home")  # avoids resubmitting on refresh
        else:
            display = "blockclass"
            messages.error(request, form.errors)
    return form, display

def home(request):
    form, display = register(request)
    context = {
        "form": form,
        "display": display,
    }
    return render(request, "pages/index.html", context=context)

def about(request):
    form, display = register(request)
    context = {
        "form": form, 
        "display": display,
    }
    return render(request, "pages/about.html", context=context)
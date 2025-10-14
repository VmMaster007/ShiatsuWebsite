# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.models import User
import logging

logging.basicConfig(filename="my_log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Register Modal Function
def register(request):

    form = CreateUserForm() # brings form through to view
    display = "" # display block later changes form to be on screen/if error
    logger.info("REGISTER: view running")
    if request.method == "POST":
        logger.info("REGISTER: post recieved")
        form = CreateUserForm(request.POST)
        print(form.errors) # for debug purposes
        if form.is_valid():
            logger.info("REGISTER: form is valid")
            # checking email exists in data base
            email = form.cleaned_data["email"]
            # print(email) # for debug purposes
            obj = User.objects.filter(email=email).exists()  # check if user with that email
            
            if obj == True:
                logger.info("REGISTER: Email exists")
                messages.error(request, "Email already exists!")
                display = "blockclass"
            else:
                form.save()
                logger.info("REGISTER: Saved form")
                # messages.success(request, "Account created successfully.")
                display = "hideclass"
                return  form, display# avoids resubmitting on refresh
        else:
            logger.info("REGISTER: Form is not valid")
            display = "blockclass"
            messages.error(request, form.errors)
    return form, display

def home(request):
    #print(register(request))
    logger.info("HOME: view loaded")
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
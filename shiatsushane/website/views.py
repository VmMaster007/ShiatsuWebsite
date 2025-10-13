from django.shortcuts import render
from .forms import CreateUserForm

def home(request):
    print("Loading home page")
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('')
    
    context = {'form': form}

    return render(request, "pages/index.html", context=context)
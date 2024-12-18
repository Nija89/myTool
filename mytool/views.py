from django.shortcuts import render, HttpResponse, redirect
from .forms import addTask
from .models import firstDB

# Create your views here.
def firsFunction(request):
    myList = firstDB.objects.all()[:2]

    context = {
        'apple' : myList
    }
    return render(request, 'mytool/index.html', context)
    # return HttpResponse("Hello World")

def success(request):
    return render(request, 'mytool/success.html')

def fail(request):
    return render(request, 'mytool/fail.html')

def add_task(request):
    if request.method == "POST":
        form = addTask(request.POST)
        if form.is_valid():
            # Extract data from form
            name = form.cleaned_data['nameFirst']
            description = form.cleaned_data['description']

            # Save to the database
            firstDB.objects.create(name=name, description=description)

            # Create a context with name and description for the success page
            context = {'name': name, 'description': description}
            return render(request, 'mytool/success.html', context)  # Render the success page
        else:
            # If the form is not valid, show the form again with errors
            print(form.errors)
            return render(request, 'mytool/add_task.html', {'form': form})  # Show the form again for corrections

    else:
        form = addTask()  # Create a new empty form

    return render(request, 'mytool/add_task.html', {'form': form})  # Render the form page initially

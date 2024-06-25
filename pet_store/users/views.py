from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_view(request):
    # If the form submission is a POST meaning we want to save data
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # And the form data is valid too.
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # Catering for page load, this is a GET condition
        form = UserCreationForm()

    return render(request, 'users/register.html', {"form": form})

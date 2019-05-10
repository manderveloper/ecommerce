from django.shortcuts import render

from .forms import ProfileForm


# Create your views here.
def profile_create_view(request):
    my_form = ProfileForm(request.POST or None)
    if my_form.is_valid():
        my_form = ProfileForm()



    context = {
        'form': my_form
    }

    return render(request, "profiles/profile_create.html", context)

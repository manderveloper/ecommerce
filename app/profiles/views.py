from .forms import ProfileForm
from django.views.generic import FormView
from django.contrib.auth import login, authenticate
from .mixins import AjaxFormMixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import ensure_csrf_cookie

class ProfileFormView(AjaxFormMixins, FormView):
    template_name = 'profiles/profile_create.html'
    form_class = ProfileForm
    success_url = reverse_lazy('home')

@ensure_csrf_cookie
def create_success(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect(render(request, "index.html"))
        else:
            form = ProfileForm()
        return render(request, 'profiles/profile_create.html', {'form': form})

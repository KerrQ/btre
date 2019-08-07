from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.utils.http import is_safe_url
from django.contrib.auth import get_user_model
from django.contrib import messages
from Contacts.models import Inquiry


def dashboard(request):
    proper = Inquiry.objects.all().filter(user_id=request.user.id)

    return render(request, 'registration/dashboard.html', {'properties': proper})


def logout_page(request):
    logout(request)
    return redirect('/')


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    next_path = next_post or next_ or None
    print(next_path)
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if is_safe_url(next_path, request.get_host()):
                    print(is_safe_url(next_path, request.get_host()))
                    return redirect(next_path)
                else:
                    return redirect('accounts:dashboard')
            else:
                messages.error(request, 'username or password not correct')

    return render(request, 'registration/login.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                last_name=last_name,
                first_name=first_name
                )
        new_user.save()
        return redirect('accounts:login')

    return render(request, 'registration/register.html', context)

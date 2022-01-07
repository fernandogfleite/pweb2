from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from jogos_blog.apps.authentication.forms import LoginForm, RegisterForm


@login_required(login_url="login/")
def main(request):
    return render(request, 'main.html')


def register_user(request):
    context = dict()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)

        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(**data)
            return redirect('login')

        context['form'] = form
        print(form.non_field_errors)
        print(form.errors)

    else:
        context['form'] = RegisterForm()

    return render(request, 'register.html', context)


def do_login(request):
    context = dict()
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is not None:
                login(request, user)

                return redirect('main')

            form.add_error(None, "Credenciais incorretas")

        context['form'] = form

    else:
        context['form'] = LoginForm()

    return render(request, 'login.html', context)


def do_logout(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render
from .forms import CreateClientForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # django le diyeko inbuilt messages featueres lai import gareko

from django.shortcuts import render, get_object_or_404, redirect
import sweetify


# Create your views here.

def clientRegister(request):
    if request.method == 'GET':
        return render(request, 'login_signup/signup.html')

    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account creation successful for  ' + username)
            msg = 'Please Login!'
            msg_type = 'success'
            msg_class = 'text-success'
            return render(request, 'login_signup/login.html', {'msg_type': msg_type, 'msg': msg, 'msg_class': msg_class})
        else:
            context = {'form': form}
            return render(request, 'login_signup/signup.html', context)

    return render(request, 'home/index.html')


def loginPage(request):
    if request.method == 'GET':
        return render(request, 'login_signup/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:  # user ko value TRUE xa i.e FALSE chaina vani vaneko... khas ma mathi ko authenticate le Boolean Value return garxa i.e user authenticate vayo vani TRUE return garxa & vayena vani chai FALSE return garxa
            login(request,
                  user)  # login(request, user) django ko inbuilt keyword jastai ho jasle login vaye ko user ko session lai database ko django_session table ma hold garera rakhcha.

            if request.user.is_superuser:
                return redirect('adminHome')

            elif request.user.is_client:
                return redirect('home')

        else:
            messages.error(request,
                           'Username OR Password is incorrect!!')  # SYNTAX: messages.info(request, 'Custom Message').......django le provide gareko informative message lai display garaune kaam garxa
            msg = 'Something went wrong!'
            msg_type = 'error'
            msg_class = 'text-danger'
            return render(request, 'login_signup/login.html', {'msg_type': msg_type, 'msg': msg, 'msg_class':msg_class})

    # context= {'form': form}
    # return render(request, 'khullasikshya/login.html', context)


def logoutall(request):
    if request.method == "POST":
        logout(request)  # logout(request) chai django le diyeko inbuilt features ho
        return redirect('login')  # logout garepaxi  feri login page ma redirect gardinxa
    return redirect('home')

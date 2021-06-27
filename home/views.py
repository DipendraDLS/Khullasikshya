from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ImageUploadForm, AddNameForm
from login_signup.models import User

# Create your views here.
from blog.models import Blog

from notice.models import Notice


def homePage(request):
    blogs = Blog.objects.all().order_by('-id')[:3]
    notices = Notice.objects.all().order_by('-id')[:3]
    context = {'blogs': blogs, 'notices': notices}
    return render(request, 'home/index.html', context)


def profile(request):
    return render(request, 'profile/profile.html')


@login_required
def uploadPic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = User.objects.get(id=request.user.id)
            m.image = form.cleaned_data['image']
            m.save()
        return redirect('profile')


@login_required
def addName(request):
    if request.method == 'POST':
        form = AddNameForm(request.POST)
        if form.is_valid():
            name = User.objects.get(id=request.user.id)
            name.first_name = form.cleaned_data['first_name']
            name.last_name = form.cleaned_data['last_name']
            name.save()
        return redirect('profile')

from login_signup.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required  # For bydefault django login_required decorator
from .decorators import admin_required  # For Using the functionality of decorators.py
from django.http import HttpResponseRedirect, HttpResponse
from login_signup.forms import UserEditForm
from typing import overload
import sweetify

from blog.models import Blog
from note.models import Level
from programming.models import ProgrammingLanguage
from notice.models import Notice


@login_required  # @login_required are bydefault given by django but in setting.py we need to add LOGIN_URL ='path' as like this =>(LOGIN_URL = 'login')
@admin_required
def adminHome(request):
    user_count = User.objects.count()
    admin_count = User.objects.filter(is_superuser=True).count()
    blog_count = Blog.objects.count()
    levels = Level.objects.all()
    context = {'user_count': user_count, 'admin_count': admin_count, 'blog_count': blog_count, 'levels': levels}
    return render(request, 'admin_home/admin_home.html', context)


@admin_required
def userShow(request):
    users = User.objects.all()
    user_count = User.objects.count()
    admin_count = User.objects.filter(is_superuser=True).count()
    context = {'users': users, 'user_count': user_count, 'admin_count': admin_count}
    return render(request, 'admin_home/admin_user.html', context)


@admin_required
def userDelete(request, id):
    if request.method == 'POST':
        user_del = User.objects.get(pk=id)
        user_del.delete()
        # return render(request, 'khullasikshya/admin_home.html')
        return HttpResponseRedirect('/userList')


@admin_required
def userEdit(request, id):
    users = User.objects.all()
    form = UserEditForm()

    if request.method == 'POST':

        edit_record = User.objects.get(pk=id)
        form = UserEditForm(request.POST, instance=edit_record)

        if form.is_valid:
            form.save()
            sweetify.success(request, 'User edit successful!',
                             text='Good job! You have successfully edited user.',
                             persistent='ok')
        return HttpResponseRedirect('/userList')

    else:
        edit_record = User.objects.get(pk=id)  # edit_record ma particular edit button click garda id ayerako huncha
        form = UserEditForm(
            instance=edit_record)  # form ma edit garda form ko field ma edit garna ko lagi previsous value haru show garirakhna ko lagi ho

    context = {'users': users, 'form': form}
    return render(request, 'admin_home/user_edit.html', context)


def search(request):
    search_result = request.GET['search']
    if search_result:
        programs = ProgrammingLanguage.objects.filter(p_title__icontains=search_result)
        blogs = Blog.objects.filter(blog_title__icontains=search_result)
        notices = Notice.objects.filter(notice_title__icontains=search_result)

    else:
        blogs = ''
        programs = ''
        notices = ''
    context = {'blogs': blogs, 'programs': programs, 'notices': notices}
    return render(request, 'admin_home/search.html', context)

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Notice
from django.shortcuts import render, redirect
from admin_home.decorators import admin_required
from .forms import AdminNoticeForm
import sweetify


# Create your views here.


# Create your views here.

################################## Frontend View Notice ##################################################################
def notice(request):
    query = request.GET.get('search')
    if query:
        page_obj = Notice.objects.filter(Q(notice_title__icontains=query) | Q(notice_content__icontains=query)).distinct()
        context = {'page_obj': page_obj, 'query': query}
        return render(request, 'notice/frontend/user_notice.html', context)

    show = Notice.objects.filter().order_by('-id')
    paginator = Paginator(show, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, }

    return render(request, 'notice/frontend/user_notice.html', context)


################################## Backend View admin notice ##################################################################
@admin_required
def adminNotice(request):
    form = AdminNoticeForm()
    if request.method == 'POST':
        form = AdminNoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice_title = form.cleaned_data['notice_title']
            notice_content = form.cleaned_data['notice_content']
            notice_url = form.cleaned_data['notice_url']
            user = request.user
            notice = Notice(notice_title=notice_title, notice_content=notice_content, notice_url=notice_url, )
            notice.save()
            sweetify.success(request, 'Notice added successfully!',
                             text='Good job! You have successfully added Notice.',
                             persistent='ok')
            return redirect('adminNotice')

    notices = Notice.objects.all().order_by('-id')

    context = {'form': form, 'notices': notices}
    return render(request, 'notice/backend/admin_notice.html', context)


@admin_required
def adminNoticeDelete(request, id):
    if request.method == 'POST':
        delete_notice = Notice.objects.get(pk=id)
        delete_notice.delete()
        sweetify.success(request, 'Notice deleted successfully!',
                         text='Good job! You have successfully deleted Notice.',
                         persistent='ok')
        return redirect('adminNotice')


@admin_required
def adminNoticeEdit(request, id):
    form = AdminNoticeForm()
    if request.method == 'POST':
        edit_record = Notice.objects.get(pk=id)
        form = AdminNoticeForm(request.POST, instance=edit_record)
        if form.is_valid:
            form.save()
            sweetify.success(request, 'Notice edited successfully!',
                             text='Good job! You have successfully edited Notice.',
                             persistent='ok')

        return redirect('adminNotice')
    else:
        edit_record = Notice.objects.get(pk=id)
        form = AdminNoticeForm(instance=edit_record)
    return render(request, 'notice/backend/admin_edit_notice.html', {'form': form})

from django.shortcuts import render, redirect
from ...models import Syllabus
from ...forms import AdminSyllabusForm
from admin_home.decorators import admin_required

import sweetify

@admin_required
def adminAddSyllabus(request):
    if request.method == 'POST':

        form = AdminSyllabusForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                syllabus_title = form.cleaned_data['syllabus_title']
                syllabus_description = form.cleaned_data['syllabus_description']
                document = form.cleaned_data['document']
                subject_id = request.POST.get('subject_name')

                syllabus = Syllabus(syllabus_title=syllabus_title, syllabus_description=syllabus_description,
                                    document=document,

                                    subject_id=subject_id)
                syllabus.save()
                redirect_subject_id = request.POST.get('redirect_subject_id')
                sweetify.success(request, 'Syllabus added successfully!',
                                 text='Good job! You have successfully added Syllabus.',
                                 persistent='ok')
                return redirect('adminViewResources', redirect_subject_id)
            except Exception as e:
                sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
                return redirect('adminViewResources', redirect_subject_id)


def adminDeleteSyllabus(request, syllabus_id):
    if request.method == 'POST':
        delete_syllabus = Syllabus.objects.get(pk=syllabus_id)
        delete_syllabus.delete()
        redirect_subject_id = request.POST.get('redirect_subject_id')
        sweetify.success(request, 'Syllabus deleted successfully!',
                         text='Good job! You have successfully deleted Syllabus.',
                         persistent='ok')
        return redirect('adminViewResources', redirect_subject_id)


def adminEditSyllabus(request, syllabus_id, subject_id):
    if request.method == 'POST':
        edit_record = Syllabus.objects.get(pk=syllabus_id)
        form = AdminSyllabusForm(request.POST or None, request.FILES or None,
                                 instance=edit_record)  # request.FILES is needed for updating the image field as well and while saving form we need to do this => edit = form.save(commit=False) and then only edit.save()
        if form.is_valid:
            edit = form.save(commit=False)
            edit.save()
            sweetify.success(request, 'Syllabus edited successfully!',
                             text='Good job! You have successfully edited Syllabus.',
                             persistent='ok')

        return redirect('adminViewResources', subject_id)
    else:
        edit_record = Syllabus.objects.get(pk=syllabus_id)
        form = AdminSyllabusForm(instance=edit_record)
        subject_id = subject_id  # Edit page ma go back button lai chaincha faculty_id

    return render(request, 'note/backend/syllabus/admin_edit_syllabus.html',
                  {'form': form, 'subject_id': subject_id})

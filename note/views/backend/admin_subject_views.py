from django.shortcuts import render, redirect
from ...models import Faculty, Subject
from ...forms import AdminSubjectForm
from admin_home.decorators import admin_required

import sweetify


@admin_required
def adminViewSubject(request, faculty_id):
    form = AdminSubjectForm()
    subjects = Subject.objects.filter(faculty_id=faculty_id)
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'form': form, 'faculty': faculty, 'subjects': subjects}

    return render(request, 'note/backend/subject/admin_view_subject.html', context)


@admin_required
def adminAddSubject(request):
    if request.method == 'POST':
        form = AdminSubjectForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                subject_name = form.cleaned_data['subject_name']
                subject_semester = form.cleaned_data['subject_semester']
                subject_description = form.cleaned_data['subject_description']
                year = form.cleaned_data['year']
                grade = request.POST.get('grade')
                faculty_id = request.POST.get('faculty_name')
                subject_order = form.cleaned_data['subject_order']

                subject = Subject(subject_name=subject_name, subject_semester=subject_semester,
                                  subject_description=subject_description, year=year, grade=grade,
                                  faculty_id=faculty_id, subject_order=subject_order)
                subject.save()
                sweetify.success(request, 'Subject added successfully!',
                                 text='Good job! You have successfully added Subject.',
                                 persistent='ok')

                redirect_faculty_id = request.POST.get('redirect_faculty_id')
                return redirect('adminViewSubject', redirect_faculty_id)
            except Exception as e:
                sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
                return redirect('adminViewSubject', redirect_faculty_id)


@admin_required
def adminDeleteSubject(request, subject_id):
    if request.method == 'POST':
        delete_subject = Subject.objects.get(pk=subject_id)
        delete_subject.delete()
        redirect_faculty_id = request.POST.get('redirect_faculty_id')
        sweetify.success(request, 'Subject deleted successfully!',
                         text='Good job! You have successfully deleted Subject.',
                         persistent='ok')
        return redirect('adminViewSubject', redirect_faculty_id)


@admin_required
def adminEditSubject(request, subject_id, faculty_id):
    if request.method == 'POST':
        edit_record = Subject.objects.get(pk=subject_id)
        form = AdminSubjectForm(request.POST or None, request.FILES or None,
                                instance=edit_record)  # request.FILES is needed for updating the image field as well and while saving form we need to do this => edit = form.save(commit=False) and then only edit.save()
        if form.is_valid:
            edit = form.save(commit=False)
            edit.save()
            sweetify.success(request, 'Subject edited successfully!',
                             text='Good job! You have successfully edited Subject.',
                             persistent='ok')

        return redirect('adminViewSubject', faculty_id)
    else:
        edit_record = Subject.objects.get(pk=subject_id)
        form = AdminSubjectForm(instance=edit_record)
        faculty_id = faculty_id  # Edit page ma go back button lai chaincha faculty_id
        faculty = Faculty.objects.get(id=faculty_id)  # needed for if condition in admin_edit_notice.html

    return render(request, 'note/backend/subject/admin_edit_subject.html',
                  {'form': form, 'faculty_id': faculty_id, 'faculty': faculty})

from django.shortcuts import render, redirect
from ...models import Subject, Note
from ...forms import AdminNoteForm, AdminSyllabusForm
from admin_home.decorators import admin_required

import sweetify


@admin_required
def adminAddNotes(request):
    if request.method == 'POST':

        form = AdminNoteForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                note_title = form.cleaned_data['note_title']
                note_description = form.cleaned_data['note_description']
                document = form.cleaned_data['document']
                subject_id = request.POST.get('subject_name')

                note = Note(note_title=note_title, note_description=note_description, document=document,
                            subject_id=subject_id)
                note.save()
                redirect_subject_id = request.POST.get('redirect_subject_id')
                sweetify.success(request, 'Note added successfully!',
                                 text='Good job! You have successfully added Note.',
                                 persistent='ok')
                return redirect('adminViewResources', redirect_subject_id)
            except Exception as e:
                sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
                return redirect('adminViewResources', redirect_subject_id)

@admin_required
def adminDeleteNotes(request, note_id):
    if request.method == 'POST':
        delete_note = Note.objects.get(pk=note_id)
        delete_note.delete()
        redirect_subject_id = request.POST.get('redirect_subject_id')
        sweetify.success(request, 'Note deleted successfully!',
                         text='Good job! You have successfully deleted Note.',
                         persistent='ok')
        return redirect('adminViewResources', redirect_subject_id)

@admin_required
def adminEditNotes(request, note_id, subject_id):
    if request.method == 'POST':
        edit_record = Note.objects.get(pk=note_id)
        form = AdminNoteForm(request.POST or None, request.FILES or None,
                             instance=edit_record)  # request.FILES is needed for updating the image field as well and while saving form we need to do this => edit = form.save(commit=False) and then only edit.save()
        if form.is_valid:
            edit = form.save(commit=False)
            edit.save()
            sweetify.success(request, 'Note edited successfully!',
                             text='Good job! You have successfully edited Note.',
                             persistent='ok')

        return redirect('adminViewResources', subject_id)
    else:
        edit_record = Note.objects.get(pk=note_id)
        form = AdminNoteForm(instance=edit_record)
        subject_id = subject_id  # Edit page ma go back button lai chaincha faculty_id

    return render(request, 'note/backend/notes/admin_edit_notes.html',
                  {'form': form, 'subject_id': subject_id})

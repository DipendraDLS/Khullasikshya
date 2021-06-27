from django.shortcuts import render, redirect
from ...models import PastQuestion
from ...forms import AdminPastQuestionForm
from admin_home.decorators import admin_required

import sweetify

@admin_required
def adminAddPastQuestion(request):
    if request.method == 'POST':
        form = AdminPastQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                pq_title = form.cleaned_data['pq_title']
                pq_description = form.cleaned_data['pq_description']
                document = form.cleaned_data['document']
                subject_id = request.POST.get('subject_name')

                pastQuestion = PastQuestion(pq_title=pq_title, pq_description=pq_description,
                                            document=document,
                                            subject_id=subject_id)
                pastQuestion.save()
                redirect_subject_id = request.POST.get('redirect_subject_id')
                sweetify.success(request, 'PastQuestion added successfully!',
                                 text='Good job! You have successfully added PastQuestion.',
                                 persistent='ok')
                return redirect('adminViewResources', redirect_subject_id)
            except Exception as e:
                sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
                return redirect('adminViewResources', redirect_subject_id)

@admin_required
def adminDeletePastQuestion(request, past_question_id):
    if request.method == 'POST':
        delete_pq = PastQuestion.objects.get(pk=past_question_id)
        delete_pq.delete()
        redirect_subject_id = request.POST.get('redirect_subject_id')
        sweetify.success(request, 'Past Question deleted successfully!',
                         text='Good job! You have successfully deleted Past Question.',
                         persistent='ok')
        return redirect('adminViewResources', redirect_subject_id)

@admin_required
def adminEditPastQuestion(request, past_question_id, subject_id):
    if request.method == 'POST':
        edit_record = PastQuestion.objects.get(pk=past_question_id)
        form = AdminPastQuestionForm(request.POST or None, request.FILES or None,
                                     instance=edit_record)              # request.FILES is needed for updating the image field as well and while saving form we need to do this => edit = form.save(commit=False) and then only edit.save()
        if form.is_valid:
            edit = form.save(commit=False)
            edit.save()
            sweetify.success(request, 'Past Question edited successfully!',
                             text='Good job! You have successfully edited Past Question.',
                             persistent='ok')

        return redirect('adminViewResources', subject_id)
    else:
        edit_record = PastQuestion.objects.get(pk=past_question_id)
        form = AdminPastQuestionForm(instance=edit_record)
        subject_id = subject_id  # Edit page ma go back button lai chaincha faculty_id

    return render(request, 'note/backend/pastQuestion/admin_edit_pq.html',
                  {'form': form, 'subject_id': subject_id})

from django.shortcuts import render, redirect
from ...models import PastQuestionSolution
from ...forms import AdminPastQuestionSolutionForm
from admin_home.decorators import admin_required

import sweetify

@admin_required
def adminAddPastQuestionSolution(request):
    if request.method == 'POST':
        form = AdminPastQuestionSolutionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                pqs_title = form.cleaned_data['pqs_title']
                pqs_description = form.cleaned_data['pqs_description']
                pqs_order = form.cleaned_data['pqs_order']
                document = form.cleaned_data['document']
                subject_id = request.POST.get('subject_name')
                pastQuestionSolution = PastQuestionSolution(pqs_title=pqs_title, pqs_description=pqs_description,
                                                            pqs_order=pqs_order,
                                                            document=document,
                                                            subject_id=subject_id)
                pastQuestionSolution.save()
                redirect_subject_id = request.POST.get('redirect_subject_id')
                sweetify.success(request, 'Solution added successfully!',
                                 text='Good job! You have successfully added Solution.',
                                 persistent='ok')
                return redirect('adminViewResources', redirect_subject_id)
            except Exception as e:
                sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
                return redirect('adminViewResources', redirect_subject_id)

@admin_required
def adminDeletePastQuestionSolution(request, pqs_id):
    if request.method == 'POST':
        delete_pq = PastQuestionSolution.objects.get(pk=pqs_id)
        delete_pq.delete()
        redirect_subject_id = request.POST.get('redirect_subject_id')
        sweetify.success(request, 'Past Question Solution deleted successfully!',
                         text='Good job! You have successfully deleted Past Question Solution.',
                         persistent='ok')
        return redirect('adminViewResources', redirect_subject_id)

@admin_required
def adminEditPastQuestionSolution(request, pqs_id, subject_id):
    if request.method == 'POST':
        edit_record = PastQuestionSolution.objects.get(pk=pqs_id)
        form = AdminPastQuestionSolutionForm(request.POST or None, request.FILES or None,
                                             instance=edit_record)  # request.FILES is needed for updating the image field as well and while saving form we need to do this => edit = form.save(commit=False) and then only edit.save()
        if form.is_valid:
            edit = form.save(commit=False)
            edit.save()
            sweetify.success(request, 'Past Question Solution edited successfully!',
                             text='Good job! You have successfully edited Past Question.',
                             persistent='ok')

        return redirect('adminViewResources', subject_id)
    else:
        edit_record = PastQuestionSolution.objects.get(pk=pqs_id)
        form = AdminPastQuestionSolutionForm(instance=edit_record)
        subject_id = subject_id  # Edit page ma go back button lai chaincha faculty_id

    return render(request, 'note/backend/pastQuestion/admin_edit_pq.html',
                  {'form': form, 'subject_id': subject_id})

from django.shortcuts import render, redirect
from ...models import Subject, Note, Syllabus, PastQuestion,PastQuestionSolution
from ...forms import AdminNoteForm, AdminSyllabusForm, AdminPastQuestionForm, AdminPastQuestionSolutionForm
from admin_home.decorators import admin_required

@admin_required
def adminViewResources(request, subject_id):
    subject = Subject.objects.get(
        id=subject_id)  # This is needed in adminAddNotes.html which is included in admin_view_resources.html also needed for redirect url
    note_form = AdminNoteForm()
    syllabus_form = AdminSyllabusForm()
    pq_form = AdminPastQuestionForm()
    pqs_form = AdminPastQuestionSolutionForm()
    notes = Note.objects.filter(subject_id=subject_id)
    syllabuses = Syllabus.objects.filter(subject_id=subject_id)
    past_questions = PastQuestion.objects.filter(subject_id=subject_id)
    past_question_solutions = PastQuestionSolution.objects.filter(subject_id=subject_id)

    context = {'subject': subject, 'note_form': note_form, 'syllabus_form': syllabus_form, 'pq_form': pq_form,
               'pqs_form': pqs_form,
               'notes': notes, 'syllabuses': syllabuses, 'past_questions': past_questions,
               'past_question_solutions': past_question_solutions}
    return render(request, 'note/backend/admin_view_resources.html', context)

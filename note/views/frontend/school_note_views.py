from django.shortcuts import render

from ...models import Level, Faculty, Subject, Note, Syllabus, PastQuestion, PastQuestionSolution


def schoolLevel(request):
    faculties = Faculty.objects.filter(level_id=Level.objects.get(level_name='School'))
    context = {'faculties': faculties}
    return render(request, 'note/frontend/school/school_level.html', context)


def schoolLevelSubjects(request, faculty_id):
    subjects = Subject.objects.filter(faculty_id=faculty_id).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects': subjects, 'faculty': faculty}
    return render(request, 'note/frontend/school/school_level_subjects.html', context)


def schoolLevelResources(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    notes = Note.objects.filter(subject_id=subject_id)
    syllabus = Syllabus.objects.filter(subject_id=subject_id)
    past_question = PastQuestion.objects.filter(subject_id=subject_id)
    past_question_solution = PastQuestionSolution.objects.filter(subject_id=subject_id)
    context = {'notes': notes, 'subject': subject, 'syllabus': syllabus, 'past_question': past_question,
               'past_question_solution': past_question_solution}
    return render(request, 'note/frontend/school/school_level_resources.html', context)

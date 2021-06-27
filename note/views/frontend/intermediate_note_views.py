from django.shortcuts import render

from ...models import Level, Faculty, Subject, Note, Syllabus, PastQuestion, PastQuestionSolution


def intermediateLevel(request):
    faculties = Faculty.objects.filter(level_id=Level.objects.get(level_name='+2|11')) | Faculty.objects.filter(
        level_id=Level.objects.get(level_name='+2|12'))
    context = {'faculties': faculties}
    return render(request, 'note/frontend/intermediate/intermediate_course.html', context)


# ******************* intermediate +2|12  *********************************************************
def intermediateTwelveSubjects(request, faculty_id):
    subjects = Subject.objects.filter(faculty_id=faculty_id, grade=12).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects': subjects, 'faculty': faculty}
    return render(request, 'note/frontend/intermediate/twelve/twelve_subjects.html', context)


# *********************** intermediate +2|11 ******************************************************
def intermediateElevenSubjects(request, faculty_id):
    subjects = Subject.objects.filter(faculty_id=faculty_id, grade=11).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects': subjects, 'faculty': faculty}
    return render(request, 'note/frontend/intermediate/eleven/eleven_subjects.html', context)


# **************************** intermediate level resources *************************************
def intermediateResources(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    notes = Note.objects.filter(subject_id=subject_id)
    syllabus = Syllabus.objects.filter(subject_id=subject_id)
    past_question = PastQuestion.objects.filter(subject_id=subject_id)
    past_question_solution = PastQuestionSolution.objects.filter(subject_id=subject_id)
    context = {'notes': notes, 'subject': subject, 'syllabus': syllabus, 'past_question': past_question,
               'past_question_solution': past_question_solution}
    return render(request, 'note/frontend/intermediate/intermediate_resources.html', context)

from django.shortcuts import render
from ...models import Level, Faculty, Subject, Note, Syllabus, PastQuestion, PastQuestionSolution


def bachelor(request):
    faculties = Faculty.objects.filter(level_id=Level.objects.get(level_name='Bachelor'))
    context = {'faculties': faculties}
    return render(request, 'note/frontend/bachelor/bachelor_course.html', context)


def bachelorCourseDetail(request, faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)

    context = {'faculty': faculty}

    return render(request, 'note/frontend/bachelor/bachelor_course_detail.html', context)


###################################### Bachelor Semester Wise Course ######################################################
def bachelorFirstSem(request, faculty_id):
    subjects_first_sem = Subject.objects.filter(faculty_id=faculty_id, subject_semester=1).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects_first_sem': subjects_first_sem, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/semester_wise/bachelor_first_sem.html', context)


def bachelorSecondSem(request, faculty_id):
    subjects_second_sem = Subject.objects.filter(faculty_id=faculty_id, subject_semester=2).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)

    context = {'subjects_second_sem': subjects_second_sem, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/semester_wise/bachelor_second_sem.html', context)


def bachelorThirdSem(request, faculty_id):
    subjects_third_sem = Subject.objects.filter(faculty_id=faculty_id, subject_semester=3).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)

    context = {'subjects_third_sem': subjects_third_sem, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/semester_wise/bachelor_third_sem.html', context)


def bachelorFourthSem(request, faculty_id):
    subjects_fourth_sem = Subject.objects.filter(faculty_id=faculty_id, subject_semester=4).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects_fourth_sem': subjects_fourth_sem, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/semester_wise/bachelor_fourth_sem.html', context)


def bachelorFifthSem(request, faculty_id):
    subjects_fifth_sem = Subject.objects.filter(faculty_id=faculty_id, subject_semester=5).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects_fifth_sem': subjects_fifth_sem, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/semester_wise/bachelor_fifth_sem.html', context)


def bachelorSixthSem(request, faculty_id):
    subjects_sixth_sem = Subject.objects.filter(faculty_id=faculty_id, subject_semester=6).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)

    context = {'subjects_sixth_sem': subjects_sixth_sem, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/semester_wise/bachelor_sixth_sem.html', context)


def bachelorSeventhSem(request, faculty_id):
    subjects_seventh_sem = Subject.objects.filter(faculty_id=faculty_id, subject_semester=7).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)

    context = {'subjects_seventh_sem': subjects_seventh_sem, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/semester_wise/bachelor_seventh_sem.html', context)


def bachelorEighthSem(request, faculty_id):
    subjects_eighth_sem = Subject.objects.filter(faculty_id=faculty_id, subject_semester=8).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)

    context = {'subjects_eighth_sem': subjects_eighth_sem, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/semester_wise/bachelor_eighth_sem.html', context)


################# For Year Wise Bachelor Course (i.e BBS and BSW) ##################################################

def bachelorFirstYear(request, faculty_id):
    subjects_first_year = Subject.objects.filter(faculty_id=faculty_id, year=1).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects_first_year': subjects_first_year, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/year_wise/bachelor_first_year.html', context)


def bachelorSecondYear(request, faculty_id):
    subjects_second_year = Subject.objects.filter(faculty_id=faculty_id, year=2).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects_second_year': subjects_second_year, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/year_wise/bachelor_second_year.html', context)


def bachelorThirdYear(request, faculty_id):
    subjects_third_year = Subject.objects.filter(faculty_id=faculty_id, year=3).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects_third_year': subjects_third_year, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/year_wise/bachelor_third_year.html', context)


def bachelorFourthYear(request, faculty_id):
    subjects_fourth_year = Subject.objects.filter(faculty_id=faculty_id, year=4).order_by('subject_order')
    faculty = Faculty.objects.get(id=faculty_id)
    context = {'subjects_fourth_year': subjects_fourth_year, 'faculty': faculty}
    return render(request, 'note/frontend/bachelor/year_wise/bachelor_fourth_year.html', context)


########################## Get all Notes, Syllabus, PQ, and PQS ######################################################
def bachelorResources(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    notes = Note.objects.filter(subject_id=subject_id)
    syllabus = Syllabus.objects.filter(subject_id=subject_id)
    past_question = PastQuestion.objects.filter(subject_id=subject_id)
    past_question_solution = PastQuestionSolution.objects.filter(subject_id=subject_id)
    context = {'notes': notes, 'subject': subject, 'syllabus': syllabus, 'past_question': past_question,
               'past_question_solution': past_question_solution}
    return render(request, 'note/frontend/bachelor/bachelor_resources.html', context)

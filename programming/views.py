from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ProgrammingForm
from .models import ProgrammingLanguage, Programming
import sweetify
from django.contrib.auth.decorators import login_required  # For bydefault django login_required decorator
from admin_home.decorators import admin_required


####################################### Backend View ###############################################################
# Create your views here.
@admin_required
def programming(request):
    form = ProgrammingForm()
    language_types = Programming.objects.all()

    if request.method == 'POST':
        form = ProgrammingForm(request.POST)
        if form.is_valid():
            p_title = form.cleaned_data['p_title']
            p_link = form.cleaned_data['p_link']
            p_code = form.cleaned_data['p_code']
            p_language = form.cleaned_data['p_language']
            program_content = ProgrammingLanguage(p_title=p_title, p_code=p_code, p_link=p_link, p_language=p_language)
            program_content.save()
            sweetify.success(request, 'Programming added successfully!',
                             text='Good job! You have successfully added programming.',
                             persistent='ok')
            return HttpResponseRedirect('/programming')
    programs = ProgrammingLanguage.objects.all().order_by('-id')

    context = {'form': form, 'language_types': language_types, 'programs': programs}
    return render(request, 'programming/backend/programming.html', context)

@admin_required
def addProgrammingLanguage(request):
    if request.method == 'POST':
        try:
            language_type = request.POST.get('programming_language')
            form = Programming(language_type=language_type)
            form.save()
            sweetify.success(request, 'Programming Language added successfully!',
                             text='Good job! You have successfully added programming.',
                             persistent='ok')
            return HttpResponseRedirect('/programming')
        except Exception as e:
            sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
            return redirect('/programming')

@admin_required
def adminProgramDelete(request, program_id):
    if request.method == 'POST':
        delete_program = ProgrammingLanguage.objects.get(pk=program_id)
        delete_program.delete()
        sweetify.success(request, 'Program deleted successfully!',
                         text='Good job! You have successfully deleted Program.',
                         persistent='ok')
        return redirect('/programming')

@admin_required
def adminProgramEdit(request, program_id):
    if request.method == 'POST':
        edit_record = ProgrammingLanguage.objects.get(pk=program_id)
        form = ProgrammingForm(request.POST, instance=edit_record)
        if form.is_valid:
            form.save()
            sweetify.success(request, 'Program edited successfully!',
                             text='Good job! You have successfully edited Program.',
                             persistent='ok')

        return redirect('/programming')
    else:
        edit_record = ProgrammingLanguage.objects.get(pk=program_id)
        language_types = Programming.objects.all()
        form = ProgrammingForm(instance=edit_record)
    return render(request, 'programming/backend/admin_edit_program.html',
                  {'form': form, 'language_types': language_types})


############################## Frontend View ##########################################################
@login_required()
def programmingHomePage(request):
    java_programs = ProgrammingLanguage.objects.filter(p_language__language_type='Java')
    js_programs = ProgrammingLanguage.objects.filter(p_language__language_type='JavaScript')
    php_programs = ProgrammingLanguage.objects.filter(p_language__language_type='PHP')
    python_programs = ProgrammingLanguage.objects.filter(p_language__language_type='Python')

    context = {'java_programs': java_programs, 'js_programs': js_programs, 'php_programs': php_programs,
               'python_programs': python_programs}
    return render(request, 'programming/frontend/programming_home_page.html', context)


@login_required()
def programmingDetails(request, program_id):
    java_programs = ProgrammingLanguage.objects.filter(p_language__language_type='Java')
    js_programs = ProgrammingLanguage.objects.filter(p_language__language_type='JavaScript')
    php_programs = ProgrammingLanguage.objects.filter(p_language__language_type='PHP')
    python_programs = ProgrammingLanguage.objects.filter(p_language__language_type='Python')

    program = ProgrammingLanguage.objects.get(id=program_id)
    context = {'java_programs': java_programs, 'js_programs': js_programs, 'php_programs': php_programs,
               'python_programs': python_programs, 'program': program}
    return render(request, 'programming/frontend/programming_details.html', context)

from django.shortcuts import render, redirect
from ...forms import AdminLevelForm
from ...models import Level, Faculty
from admin_home.decorators import admin_required

import sweetify


# Create your views here.

################################### Level Backend Views ###########################################
@admin_required
def adminLevel(request):
    form = AdminLevelForm()
    levels = Level.objects.all()

    ############ For Maintaining Counts on adminLevel Page  ################
    # using django reverse relation as=>  ".faculty_set.all()" here, "faculty" is the model name in small letter and this will hit reverse relation and sets all the faculty related to level name and counts it's value.
    bachelor_faculty_count = Level.objects.get(level_name='Bachelor').faculty_set.all().count()
    twelve_faculty_count = Level.objects.get(level_name='+2|12').faculty_set.all().count()
    eleven_faculty_count = Level.objects.get(level_name='+2|11').faculty_set.all().count()
    school_faculty_count = Level.objects.get(level_name='School').faculty_set.all().count()

    # print(Level.objects.get(level_name='Bachelor').faculty_set.all().count())

    if request.method == 'POST':
        form = AdminLevelForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                level_name = form.cleaned_data['level_name']
                level_image = form.cleaned_data['level_image']
                level_order = form.cleaned_data['level_order']

                level = Level(level_name=level_name, level_image=level_image, level_order=level_order)
                level.save()
                sweetify.success(request, 'Level added successfully!',
                                 text='Good job! You have successfully added Level.',
                                 persistent='ok')
                return redirect('adminLevel')
            except Exception as e:
                sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
                return redirect('adminLevel')

    context = {'form': form, 'levels': levels,
               'bachelor_faculty_count': bachelor_faculty_count,
               'twelve_faculty_count': twelve_faculty_count, 'eleven_faculty_count': eleven_faculty_count,
               'school_faculty_count': school_faculty_count}

    return render(request, 'note/backend/level/admin_level.html', context, )

@admin_required
def adminLevelDelete(request, id):
    if request.method == 'POST':
        delete_blog = Level.objects.get(pk=id)
        delete_blog.delete()
        sweetify.success(request, 'Level deleted successfully!',
                         text='Good job! You have successfully deleted Level.',
                         persistent='ok')
        return redirect('adminLevel')

@admin_required
def adminLevelEdit(request, id):
    if request.method == 'POST':
        edit_record = Level.objects.get(pk=id)
        form = AdminLevelForm(request.POST or None, request.FILES or None,
                              instance=edit_record)  # request.FILES is needed for updating the image field as well and while saving form we need to do this => edit = form.save(commit=False) and then only edit.save()
        if form.is_valid:
            edit = form.save(commit=False)
            edit.save()
            sweetify.success(request, 'Level edited successfully!',
                             text='Good job! You have successfully edited Level.',
                             persistent='ok')

        return redirect('adminLevel')
    else:
        edit_record = Level.objects.get(pk=id)
        form = AdminLevelForm(instance=edit_record)
    return render(request, 'note/backend/level/admin_edit_level.html', {'form': form})

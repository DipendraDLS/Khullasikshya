from django.shortcuts import render, redirect
from ...models import Level, Faculty
from ...forms import AdminFacultyForm
import sweetify
from admin_home.decorators import admin_required


@admin_required
def adminViewFaculty(request, level_id):
    faculties = Faculty.objects.filter(level=level_id)
    level = Level.objects.get(id=level_id)  # this is needed for admin_add_faculty.html which is included in admin_view_faculty.html
    bachelor_faculty_count = Faculty.objects.filter(level=level_id).count
    return render(request, 'note/backend/faculty/admin_view_faculty.html', {'faculties': faculties, 'level': level, 'bachelor_faculty_count':bachelor_faculty_count})


@admin_required
def adminAddFaculty(request):
    if request.method == 'POST':
        try:
            faculty_name = request.POST.get('faculty_name')
            faculty_description = request.POST.get('faculty_description')
            faculty_image = request.FILES.get('faculty_image')
            level_id = Level.objects.get(id=int(request.POST.get(
                'level_name')))  # For storing the values in foreign we need to make instance as this using the query for Parent Model i.e 'Level Model

            add_faculty = Faculty(faculty_name=faculty_name, faculty_description=faculty_description,
                                  faculty_image=faculty_image,
                                  level=level_id)
            add_faculty.save()

            redirect_level_id = request.POST.get('redirect_level_id')
            # print(redirect_level_id)
            sweetify.success(request, 'Faculty added successfully!', persistent='Close')
            return redirect('adminViewFaculty', redirect_level_id)

        except Exception as e:
            sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
            return redirect('adminLevel')
    return redirect('adminLevel')

@admin_required
def adminDeleteFaculty(request, faculty_id):
    if request.method == 'POST':
        delete_faculty = Faculty.objects.get(pk=faculty_id)
        delete_faculty.delete()
        redirect_level_id = request.POST.get('redirect_level_id')
        sweetify.success(request, 'Faculty deleted successfully!',
                         text='Good job! You have successfully deleted Faculty.',
                         persistent='ok')
        return redirect('adminViewFaculty', redirect_level_id)

@admin_required
def adminEditFaculty(request, faculty_id, level_id):
    if request.method == 'POST':
        edit_record = Faculty.objects.get(pk=faculty_id)
        form = AdminFacultyForm(request.POST or None, request.FILES or None,
                                instance=edit_record)  # request.FILES is needed for updating the image field as well and while saving form we need to do this => edit = form.save(commit=False) and then only edit.save()
        if form.is_valid:
            edit = form.save(commit=False)
            edit.save()
            sweetify.success(request, 'Faculty edited successfully!',
                             text='Good job! You have successfully edited Faculty.',
                             persistent='ok')

        return redirect('adminViewFaculty', level_id)
    else:
        edit_record = Faculty.objects.get(pk=faculty_id)
        form = AdminFacultyForm(instance=edit_record)
        level_id = level_id
    return render(request, 'note/backend/faculty/admin_edit_faculty.html', {'form': form, 'level_id': level_id})

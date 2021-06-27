from django import forms
from .models import Level, Faculty, Subject, Note, Syllabus, PastQuestion, PastQuestionSolution


class AdminLevelForm(forms.ModelForm):
    # If you want to give select option through forms.py to template we will do as below.
    CHOICES = (('Bachelor', 'Bachelor'), ('+2|12', '+2|12'), ('+2|11', '+2|11'), ('School', 'School'))
    level_name = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Level
        fields = ('level_name', 'level_image', 'level_order')

        widgets = {
            'level_order': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }


class AdminFacultyForm(forms.ModelForm):
    faculty_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Faculty
        fields = ('faculty_description', 'faculty_image')
        widgets = {
            'faculty_description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AdminSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = (
            'subject_name', 'subject_semester', 'subject_description', 'year', 'grade', 'subject_image',
            'subject_order')

        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Name'}),
            'subject_semester': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 8}),
            'subject_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 4}),
            'grade': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 12}),
            'subject_order': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 100})

        }


class AdminNoteForm(forms.ModelForm):
    document = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Note
        fields = ('note_title', 'note_description', 'document', 'document_cover')
        widgets = {
            'note_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note Title'}),
            'note_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }


class AdminSyllabusForm(forms.ModelForm):
    document = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Syllabus
        fields = ('syllabus_title', 'syllabus_description', 'document', 'document_cover')
        widgets = {
            'syllabus_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Syllabus Title'}),
            'syllabus_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }


class AdminPastQuestionForm(forms.ModelForm):
    document = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = PastQuestion
        fields = ('pq_title', 'pq_description', 'document', 'document_cover')
        widgets = {
            'pq_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Past Question Title'}),
            'pq_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }


class AdminPastQuestionSolutionForm(forms.ModelForm):
    document = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = PastQuestionSolution
        fields = ('pqs_title', 'pqs_description', 'pqs_order', 'document', 'document_cover')
        widgets = {
            'pqs_title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Past Question Solution Title'}),
            'pqs_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'pqs_order': forms.NumberInput(attrs={'class': 'form-control'})
        }

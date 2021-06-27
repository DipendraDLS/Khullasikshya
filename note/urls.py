from django.urls import path
from .views.backend import admin_level_views, admin_faculty_views, admin_subject_views, admin_notes_views, \
    admin_syllabus_views, admin_resources_views, admin_past_question_views, admin_past_question_solution_views
from .views.frontend import bachelor_note_views, intermediate_note_views, school_note_views

urlpatterns = [
    # **************************************** Backend urls ********************************************************************

    ##################################### Level urls ##################################################
    path('adminLevel/', admin_level_views.adminLevel, name="adminLevel"),
    path('adminLevelEdit/<int:id>', admin_level_views.adminLevelEdit, name="adminLevelEdit"),
    path('adminLevelDelete/<int:id>', admin_level_views.adminLevelDelete, name="adminLevelDelete"),

    ######################################## Faculty urls #############################################
    path('adminViewFaculty/<int:level_id>', admin_faculty_views.adminViewFaculty, name="adminViewFaculty"),
    path('adminAddFaculty', admin_faculty_views.adminAddFaculty, name="adminAddFaculty"),
    path('adminDeleteFaculty/<int:faculty_id>', admin_faculty_views.adminDeleteFaculty, name="adminDeleteFaculty"),
    path('adminEditFaculty/<int:faculty_id>/<int:level_id>', admin_faculty_views.adminEditFaculty,
         name="adminEditFaculty"),

    ######################################## Subject urls #############################################
    path('adminViewSubject/<int:faculty_id>', admin_subject_views.adminViewSubject, name="adminViewSubject"),
    path('adminAddSubject', admin_subject_views.adminAddSubject, name="adminAddSubject"),
    path('adminDeleteSubject/<int:subject_id>', admin_subject_views.adminDeleteSubject, name="adminDeleteSubject"),
    path('adminEditSubject/<int:subject_id>/<int:faculty_id>', admin_subject_views.adminEditSubject,
         name="adminEditSubject"),
    ######################################### Showing All Notes, Syllabus, PQ and PQS #######################
    path('adminViewResources/<int:subject_id>', admin_resources_views.adminViewResources, name="adminViewResources"),

    ######################################## Notes urls ###################################################
    path('adminAddNotes', admin_notes_views.adminAddNotes, name="adminAddNotes"),
    path('adminDeleteNotes/<int:note_id>', admin_notes_views.adminDeleteNotes, name="adminDeleteNotes"),
    path('adminEditNotes/<int:note_id>/<int:subject_id>', admin_notes_views.adminEditNotes, name="adminEditNotes"),

    ########################################## Syllabus urls #############################################
    path('adminAddSyllabus', admin_syllabus_views.adminAddSyllabus, name="adminAddSyllabus"),
    path('adminDeleteSyllabus/<int:syllabus_id>', admin_syllabus_views.adminDeleteSyllabus, name="adminDeleteSyllabus"),
    path('adminEditSyllabus/<int:syllabus_id>/<int:subject_id>', admin_syllabus_views.adminEditSyllabus,
         name="adminEditSyllabus"),
    ############################################### Past Question Urls ##########################################
    path('adminAddPastQuestion', admin_past_question_views.adminAddPastQuestion, name="adminAddPastQuestion"),
    path('adminDeletePastQuestion/<int:past_question_id>', admin_past_question_views.adminDeletePastQuestion,
         name="adminDeletePastQuestion"),
    path('adminEditPastQuestion/<int:past_question_id>/<int:subject_id>',
         admin_past_question_views.adminEditPastQuestion,
         name="adminEditPastQuestion"),

    ############################################### Past Question Solution Urls ##########################################
    path('adminAddPastQuestionSolution', admin_past_question_solution_views.adminAddPastQuestionSolution,
         name="adminAddPastQuestionSolution"),
    path('adminDeletePastQuestionSolution/<int:pqs_id>',
         admin_past_question_solution_views.adminDeletePastQuestionSolution,
         name="adminDeletePastQuestionSolution"),

    path('adminEditPastQuestionSolution/<int:pqs_id>/<int:subject_id>',
         admin_past_question_solution_views.adminEditPastQuestionSolution,
         name="adminEditPastQuestionSolution"),

    # *****************************************************************************************************************

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  Frontend urls   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ************************* Bachelor Frontend  urls ***********************************************
    path('bachelor', bachelor_note_views.bachelor, name="bachelor"),
    path('bachelorCourseDetail/<int:faculty_id>', bachelor_note_views.bachelorCourseDetail,
         name="bachelorCourseDetail"),
    # ************************* Bachelor Frontend Semester Wise urls ***********************************************
    path('bachelorFirstSem/<int:faculty_id>', bachelor_note_views.bachelorFirstSem, name="bachelorFirstSem"),
    path('bachelorSecondSem/<int:faculty_id>', bachelor_note_views.bachelorSecondSem, name="bachelorSecondSem"),
    path('bachelorThirdSem/<int:faculty_id>', bachelor_note_views.bachelorThirdSem, name="bachelorThirdSem"),
    path('bachelorFourthSem/<int:faculty_id>', bachelor_note_views.bachelorFourthSem, name="bachelorFourthSem"),
    path('bachelorFifthSem/<int:faculty_id>', bachelor_note_views.bachelorFifthSem, name="bachelorFifthSem"),
    path('bachelorSixthSem/<int:faculty_id>', bachelor_note_views.bachelorSixthSem, name="bachelorSixthSem"),
    path('bachelorSeventhSem/<int:faculty_id>', bachelor_note_views.bachelorSeventhSem, name="bachelorSeventhSem"),
    path('bachelorEighthSem/<int:faculty_id>', bachelor_note_views.bachelorEighthSem, name="bachelorEighthSem"),
    # ************************* Bachelor Frontend Year Wise urls ***********************************************
    path('bachelorFirstYear/<int:faculty_id>', bachelor_note_views.bachelorFirstYear, name="bachelorFirstYear"),
    path('bachelorSecondYear/<int:faculty_id>', bachelor_note_views.bachelorSecondYear, name="bachelorSecondYear"),
    path('bachelorThirdYear/<int:faculty_id>', bachelor_note_views.bachelorThirdYear, name="bachelorThirdYear"),
    path('bachelorFourthYear/<int:faculty_id>', bachelor_note_views.bachelorFourthYear, name="bachelorFourthYear"),

    path('bachelorResources/<int:subject_id>', bachelor_note_views.bachelorResources, name="bachelorResources"),

    # ********************************* +2 Frontend urls ******************************************************
    path('intermediate', intermediate_note_views.intermediateLevel, name="intermediate"),
    path('intermediateTwelveSubjects/<int:faculty_id>', intermediate_note_views.intermediateTwelveSubjects,
         name="intermediateTwelveSubjects"),
    path('intermediateElevenSubjects/<int:faculty_id>', intermediate_note_views.intermediateElevenSubjects,
         name="intermediateElevenSubjects"),

    path('intermediateResources/<int:subject_id>', intermediate_note_views.intermediateResources,
         name="intermediateResources"),

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # @@@@@@@@@@@@@@@@@@@@@@@@ School Frontend urls @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    path('schoolLevel', school_note_views.schoolLevel, name="schoolLevel"),
    path('schoolLevleSubjects/<int:faculty_id>', school_note_views.schoolLevelSubjects, name="schoolLevelSubjects"),
    path('schoolLevleResources/<int:subject_id>', school_note_views.schoolLevelResources, name="schoolLevelResources"),

]

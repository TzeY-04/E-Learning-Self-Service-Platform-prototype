"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app import views as main_views
from EnrollCourse import views as EnrollCourse_views
from StudentSubmission import views as StudentSubmission_views
from ExamineMarketTrends import views as ExamineMarketTrends_views
from PartnerCourseExperts import views as PartnerCourseExperts_views
from EnhanceUserExperience import views as EnhanceUserExperience_views
from TrackLearningProgress import views as TrackLearningProgress_views
from ProvideFeedback import views as ProvideFeedback_views
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from app.views import logout
from CreateAndManageCourse import views as CreateAndManageCourse_views
from CreateAndMarkAssignment import views as CreateAndMarkAssignment_views
from ViewStudentProgress import views as ViewStudentProgress_views
from ManageUserAccount import views as ManageUserAccount_views
from RemoveCourseVideo import views as RemoveCourseVideo_views
from OverseePlatform import views as OverseePlatform_views




admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', main_views.home, name='home'),
    re_path(r'^contact$', main_views.contact, name='contact'),
    re_path(r'^about$', main_views.about, name='about'),
    re_path(r'^login/$',
        LoginView.as_view(template_name = 'app/login.html'),
        name='login'),
    re_path(r'^logout$',
        LogoutView.as_view(template_name = 'app/index.html'),
        name='logout'),
    re_path(r'^menu$', main_views.menu, name='menu'),
    re_path(r'^ShowCourseDetail$', EnrollCourse_views.ShowCourseDetail, name='ShowCourseDetail'),
    re_path(r'^ShowPurchasedCourse$', main_views.ShowPurchasedCourse, name='ShowPurchasedCourse'),
    re_path(r'^check_user$', main_views.check_user, name='check_user'),
    re_path('logout/', logout, name='logout'),
    re_path(r'^analytics-board$', main_views.analytics_board, name='analytics_board'),
    path('select-course/<str:course_id>/', EnrollCourse_views.select_course, name='select_course'),
    path('enroll-course/<str:course_id>/',EnrollCourse_views.enroll_course, name='enroll_course'),
    path('studentmainpage', main_views.studentmainpage, name='studentmainpage'),
    path('submission', StudentSubmission_views.submission, name='submission'),
    path('assignmentsubmission', StudentSubmission_views.assignmentsubmission, name='assignmentsubmission'),
    path('pmanagermainpage', main_views.pmanagermainpage, name='pmanagermainpage'),
    path('AnalyticsBoardPage',ExamineMarketTrends_views.analytics_board_page, name='AnalyticsBoardPage'),
    path('UserFeedback',ExamineMarketTrends_views.user_feedback,name='UserFeedback'),
    path('SalesPerformance',ExamineMarketTrends_views.sales_performance,name="SalesPerformance"),
    path('UserFeedbackReport',ExamineMarketTrends_views.user_feedback_report,name="UserFeedbackReport"),
    path('SalesPerformanceReport', ExamineMarketTrends_views.sales_performance_report,name="SalesPerformanceReport"),
    path('InviteCourseExperts', PartnerCourseExperts_views.invite_course_experts,name="InviteCourseExperts"),
    path('SurveyCreation',EnhanceUserExperience_views.create_survey,name="SurveyCreation"),
    path('creating_survey',EnhanceUserExperience_views.creating_survey,name="creating_survey"),
    path('show_survey_reply',EnhanceUserExperience_views.show_survey_reply,name="show_survey_reply"),
    path('show_survey',EnhanceUserExperience_views.show_survey,name="show_survey"),
    path('submit_assignment',StudentSubmission_views.submit,name="submit_assignment"),
    path('uploadfile',StudentSubmission_views.uploadfile,name="uploadfile"),
    path('track_learning_progress',TrackLearningProgress_views.track_learning_progress,name="track_learning_progress"),
    path('providefeedback',ProvideFeedback_views.providefeedback,name="providefeedback"),
    path('uploadfeedback',ProvideFeedback_views.uploadfeedback,name="uploadfeedback"),
    path('courses',main_views.courses,name="courses"),
    path('teachermainpage',main_views.teachermainpage,name="teachermainpage"),
    path('createcourse',CreateAndManageCourse_views.createcourse,name="createcourse"),
    path('uploadcourse',CreateAndManageCourse_views.uploadcourse,name="uploadcourse"),
    path('editcourse',CreateAndManageCourse_views.editcourse,name="editcourse"),
    path('teacher_choice',main_views.teacher_choice,name="teacher_choice"),
    path('deletecourse',CreateAndManageCourse_views.deletecourse,name="deletecourse"),
    path('createassignment',CreateAndMarkAssignment_views.createassignment,name="createassignment"),
    path('listassignment',CreateAndMarkAssignment_views.listassignment,name="listassignment"),
    path('viewassignmentsubmission',CreateAndMarkAssignment_views.viewassignmentsubmission,name="viewassignmentsubmission"),
    path('markassignment',CreateAndMarkAssignment_views.markassignment,name="markassignment"),
    path('liststudentprogress',ViewStudentProgress_views.liststudentprogress,name="liststudentprogress"),
    path('showstudentprogress',ViewStudentProgress_views.showstudentprogress,name="showstudentprogress"),
    path('OverseeEntirePlatform', main_views.OverseeEntirePlatform, name='OverseeEntirePlatform'),
    path('ManageUserAccount', main_views.ManageUserAccount, name='ManageUserAccount'),
    path('ShowContent', main_views.ShowContent, name='ShowContent'),
    path('adminmainpage', main_views.adminmainpage, name='adminmainpage'),
    path("manageuseraccount", ManageUserAccount_views.manage_user_account, name="manageuseraccount"),
    path("viewuser", ManageUserAccount_views.view_user, name="viewuser"),
    path("deleteuser", ManageUserAccount_views.delete_user, name="deleteuser"),
    path("confirm_delete_user", ManageUserAccount_views.confirm_delete_user, name="confirm_delete_user"),
    path('courselist', RemoveCourseVideo_views.course_list, name="courselist"),
    path('viewcourse/<str:course_id>/', RemoveCourseVideo_views.view_course, name="viewcourse"),
    path("removecourse/<str:course_id>/", RemoveCourseVideo_views.remove_course, name="removecourse"),
    path("confirm_delete_course/<str:course_id>/", RemoveCourseVideo_views.confirm_delete_course, name="confirm_delete_course"),
    path("viewvideos/<str:course_id>/<str:video_id>/", RemoveCourseVideo_views.view_video, name="viewvideos"),
    path("removevideo/<str:course_id>/<str:video_id>/", RemoveCourseVideo_views.remove_video, name="removevideo"),
    path("confirm_delete_video/<str:course_id>/<str:video_id>/", RemoveCourseVideo_views.confirm_delete_video, name="confirm_delete_video"),
    path('allProgress', OverseePlatform_views.all_progress, name="allProgress"),
    path('allPurchased', OverseePlatform_views.all_purchased, name="allPurchased"),
    path('haveMarks', OverseePlatform_views.have_marks, name="haveMarks"),
    path('noMarks', OverseePlatform_views.no_marks, name="noMarks"),


]

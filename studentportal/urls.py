from django.urls import path
from . import views

urlpatterns = [
    path('portal/register/', views.Register.as_view(), name= 'portalregister'),
    path('portal/login/', views.CustomLoginView.as_view(next_page='portal'), name= 'portallogin'),
    path('portal/logout/', views.CustomLogout.as_view(next_page='portal'), name= 'portallogout'),
    path('portal/', views.Portal.as_view(), name= 'portal'),
    path('portal/studentdashboard', views.Studentdashboard.as_view(), name= 'studentdashboardlink'),
    path('portal/studentprofile', views.Studentdata.as_view(), name= 'studentprofile'),
    path('portal/createprofile', views.Createstudentdata.as_view(), name= 'createstudentprofile'),
    path('portal/updateprofile/<int:pk>', views.Updatestudentdata.as_view(), name= 'updatestudentprofile'),
    #path('portal/studentdashboard', views.Studentdashboard.as_view(), name= 'studentdashboard'),
    path('portal/staffdashboard', views.Staffdashboard.as_view(), name= 'staffdashboard'),
    path('portal/staffprofile', views.Staffdata.as_view(), name= 'staffprofile'),
    path('portal/createstaffprofile', views.Createstaffdata.as_view(), name= 'createstaffprofile'),
    path('portal/updatestaffprofile/<int:pk>', views.Updatestaffdata.as_view(), name= 'updatestaffprofile'),
    path('portal/compileresult', views.CreateExam.as_view(), name= 'newexamscores'),  
    path('portal/viewscores', views.Viewscores.as_view(), name= 'viewexamscores'),  
    path('portal/apply/', views.ApplicationForm.as_view(), name= 'apply'),
    path('portal/admissionstat/', views.AdmissionStat.as_view(), name= 'admissionstat'),
    path('portal/allapplicants/', views.Applicantlist.as_view(), name= 'applicantlist'),
    path('portal/allapplicants/<slug>/', views.ApplicantlistDetail.as_view(), name= 'applicantdetail'),




]




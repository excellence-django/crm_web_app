from django.urls import path
from studentapp import views


urlpatterns=[
   # path("enroll/list/", views.StudentListView.as_view(), name="elist"),
     path("",views.LoginView.as_view(),name="index"),
    path("home/",views.HomeCreateView.as_view(),name="home"),
    path("accounts/register/", views.StudentCreateView.as_view(), name="signup"),
    path("accounts/list/", views.StudentListView.as_view(), name="list"),
    path("accounts/<str:stid>", views.StudentDetailView.as_view(), name="std-details"),
    path("edit/<str:std_id>", views.StudentEditView.as_view(), name="std-eid"),
    path("remove/<str:sid>", views.remove_student, name="delete"),
    path("course/register/", views.CourseCreateView.as_view(), name="cadd"),
    path("course/list/", views.CourseListView.as_view(), name="clist"),
    path("course/<str:c_id>", views.CourseEditView.as_view(), name="c-id"),
    path("coursed/<str:cid>", views.remove_course, name="cdelete"),
    path("coursev/<str:cid>", views.CourseDetailView.as_view(), name="cv"),
    path("enroll/new", views.EnrollCreateView.as_view(), name="en"),
    path("enroll/list", views.EnrollListView.as_view(), name="elist"),
    path("enroll/<str:e_id>", views.EnrollEditView.as_view(), name="e-id"),
    path("enrolle/<str:eid>", views.EnrollDetailView.as_view(), name="e-details"),
    path("enrolld/<str:eid>", views.remove_enroll, name="e-delete"),
    path("single/sview/", views.EnrollSingleView.as_view(), name="sview"),
    path('team_info/<str:erid>', views.en_info, name="get_team_info"),
    path('team_email/', views.send_email, name="team_email"),
    path("clear/", views.logoutview, name="logout"),

]
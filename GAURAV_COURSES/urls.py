from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.GAURAV_lmsSignupUser.as_view()),
    path("getAllUsers/", views.GAURAV_lmsGetUserDetails.as_view()),
    path("updateEmail/", views.GAURAV_lmsUpdateEmail.as_view()),
    path("deleteUser/<number>/", views.GAURAV_lmsDeleteUser.as_view())
]
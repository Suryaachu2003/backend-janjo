from django.urls import path
from .views import hi, page2, display_form, display_teacherform, management, homepage, viewalldata, specificdata, courses, contact, resume_form, login_view, logout_view, about

urlpatterns = [
    path('hi', hi),
    path('page2', page2),
    path('displayform', display_form, name='studentforms'),
    path('teacherform', display_teacherform, name='teacherforms'),
    path('management', management),
    path('homepage', homepage, name='homepage'),
    path('viewalldata', viewalldata, name='display'),
    path('specificdata/<int:userid>/', specificdata, name='specificdata'),
    path('courses', courses, name='courses'),
    path('email', contact, name='contact'),
    path('resume/', resume_form, name='resume_form'),
    path('login/',login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('about', about, name='about'),]

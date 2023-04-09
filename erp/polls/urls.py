from django.urls import path
from . import views
app_name =  'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.logout, name='logout'),
    path('', views.faculty_logout, name='faculty_logout'),
    path('student_login.html',views.student_login, name="student_login"),
    path('faculty_login.html', views.faculty_login, name="faculty_login"),
    #path('student_registration.html', views.student_registration, name="student_registration"),
    path('admin_login.html', views.admin_login, name="admin_login"),
    #path('',views.index, name="student_homepage/homepage.html"),
    path('student_homepage/<user_id>',views.student_homepage, name="student_homepage"),
    path('faculty_homepage/<user_id>',views.faculty_homepage, name="faculty_homepage"),
    path('departments',views.view_departments, name="view_departments"),
    path('faculty', views.view_faculty_list, name="view_faculty_list"),
    path('courses', views.view_courses, name="view_courses"),
    path('students/<course_id>', views.view_students_in_a_course, name="show_courses_by_a_faculty")
]



from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import student, department, course, enrollment
from .models import faculty as faculty
from django.shortcuts import HttpResponse
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib import messages



class student_info():
   student_id: any
   student_name: any
   student_email:any
   student_phone_no:any
   student_dob:any
   student_dept_id: any
   student_dept_name: any
   username: any
   password:any

class department_info():
   dept_id:any
   dept_name:any

class Course_info:
   course_id: any
   course_name: any
   credits: any
   course_faculty_id:any
   course_faculty_name: any
   course_dept_id:any
   course_dept_name:any

class enrolled_Course:
   course_id: any
   course_name: any
   credits: any
   course_faculty_id: any
   course_faculty_name: any
   course_dept_id: any
   course_dept_name: any
   enroll_id: any
   grade: any

class faculty_info():
   faculty_id: any
   faculty_name: any
   dept_id: any
   dept_name: any
   username: any
   password: any


@cache_control(no_cache=True, must_revalidate=True)
def index(request):
    return render(request, 'polls/homepage.html',{'title':"homepage"})

can_login = False
can_faculty_login = False


@cache_control(no_cache=True, must_revalidate=True)
def student_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if student.objects.filter(username=username).exists():
           pass
        else:
            #messages.error(request, "Invalid username or password.")
            return render(request, 'polls/student_login.html', {'title': "student_login"})
        
        user_credential = student.objects.get(username = username)
        if user_credential.password == password:
           #print("Test0")
           global can_login
           can_login = True

           return redirect('polls:student_homepage', user_id = username,#kwargs= {{'can_login':True}}
           )
        else:
           #messages.error(request, "Invalid username or password.")
           pass

    return render(request, 'polls/student_login.html', {'title': "student_login"})


@cache_control(no_cache=True, must_revalidate=True)
def faculty_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if faculty.objects.filter(username=username).exists():
           pass
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'polls/faculty_login.html', {'title': "student_login"})

        user_credential = faculty.objects.get(username=username)
        if user_credential.password == password:
           # print("Test0")
           global can_faculty_login
           can_faculty_login = True
           return redirect('polls:faculty_homepage', user_id=username)
        else:
           #messages.error(request, "Invalid username or password.")
           pass

    return render(request, 'polls/faculty_login.html', {'title': "faculty_login"})
    

# def student_registration(request):
#   if request.method == "POST":
#     name = request.POST["name"]
#     student_id = request.POST["student_id"]
#     department_id = request.POST.get("department_id")
#     email = request.POST.get("email")
#     phone_number = request.POST.get("phone_number")
#     dob = request.POST.get("dob")
#     username = request.POST["username"]
#     password = request.POST["password"]

#     dept = department.objects.get(department_id = department_id)
#     new_student = student(name = name, student_id = student_id, 
#                           department_id = dept,email = email, 
#                           phone_number = phone_number,dob = dob)
#     new_student.save()

#     new_credential = student_credential(username = username, password = password, student_id = new_student)
#     new_credential.save()

#     return redirect('polls:student_login')
#   return render(request, 'polls/student_registration.html', {'title': "student_registration", "departmentcontext": department.objects.all()})

@cache_control(no_cache=True, must_revalidate=True)
# @login_required(login_url='homepage.html')
def student_homepage(request, user_id):
    global can_login
    print(can_login)
    if can_login == False:
      return render(request, 'polls/homepage.html', {'title': "homepage"})
    
    student_credentials = student.objects.get(username=user_id)
    stud_id = student_credentials.student_id
    student_details = student.objects.get(student_id=stud_id)

    personal_info = student_info()
    personal_info.student_name = student_details.name
    personal_info.student_id = stud_id
    personal_info.student_dept_id = student_details.department_id.department_id
    personal_info.student_dept_name = student_details.department_id.name
    personal_info.student_email = student_details.email
    personal_info.student_phone_no = student_details.phone_number
    personal_info.student_dob = student_details.dob
    personal_info.username = user_id
    personal_info.password = student_credentials.password

    courses_enrolled = []
    for enroll in enrollment.objects.all():
       if enroll.student_id.student_id == stud_id:
        course_dict = enrolled_Course()
        course_dict.course_id = enroll.course_id.course_id
        course_dict.course_name = enroll.course_id.name
        course_dict.credits = enroll.course_id.credits
        course_dict.course_faculty_id = enroll.course_id.faculty_id.faculty_id
        course_dict.course_faculty_name = enroll.course_id.faculty_id.name
        course_dict.course_dept_id = enroll.course_id.course_dept_id.department_id
        course_dict.course_dept_name = enroll.course_id.course_dept_id.name
        course_dict.grade = enroll.grade
        course_dict.enroll_id = enroll.enrollment_id
        courses_enrolled.append(course_dict)

    # print("--printing courses")
    # print(courses_enrolled)
    return render(request, 'polls/student_homepage.html', {"personal_info": personal_info,
                                                           'courses_enrolled': courses_enrolled})


@cache_control(no_cache=True, must_revalidate=True)
def faculty_homepage(request, user_id):
    if can_faculty_login == False:
      return render(request, 'polls/faculty_homepage.html', {'title': "homepage"})
    
    if request.method=="POST":
       course_id_to_show = request.POST.get('course_id')
       return redirect('polls:show_courses_by_a_faculty', course_id = course_id_to_show)

    faculty_credentials = faculty.objects.get(username=user_id)
    faculty_details = faculty_info()
    faculty_details.username = faculty_credentials.username
    faculty_details.password = faculty_credentials.password
    faculty_details.faculty_id = faculty_credentials.faculty_id
    faculty_details.faculty_name = faculty_credentials.name
    faculty_details.dept_id = faculty_credentials.department_id.department_id
    faculty_details.dept_name = faculty_credentials.department_id.name

    courses_taken = []
    for cour in course.objects.all():
       if cour.faculty_id.faculty_id == faculty_credentials.faculty_id:
          course_temp = Course_info()
          course_temp.course_id = cour.course_id
          course_temp.course_name = cour.name
          course_temp.course_faculty_id = cour.faculty_id.faculty_id
          course_temp.course_faculty_name = cour.faculty_id.name
          course_temp.course_dept_id = cour.course_dept_id.department_id
          course_temp.course_dept_name = cour.course_dept_id.name
          course_temp.credits = cour.credits
          courses_taken.append(course_temp)
    return render(request, 'polls/faculty_homepage.html', {"faculty_info":faculty_details,
                                                          "courses_taught":courses_taken})



def view_departments(request):
    return render(request,"polls/departments.html",{"departments_list":department.objects.all()})



def view_courses(request):
    courses_list = []
    for cour in course.objects.all():
       course_dict = Course_info()
       course_dict.course_id = cour.course_id
       course_dict.course_name = cour.name
       course_dict.credits = cour.credits
       course_dict.course_faculty_id = cour.faculty_id.faculty_id
       course_dict.course_faculty_name = cour.faculty_id.name
       course_dict.course_dept_id = cour.course_dept_id.department_id
       course_dict.course_dept_name = cour.course_dept_id.name
       courses_list.append(course_dict)
    return render(request, "polls/courses.html", {"courses_list": courses_list})


def view_faculty_list(request):

    departments_all = []
    for dept in department.objects.all():
       dept_dict = department_info()
       dept_dict.dept_id = dept.department_id
       dept_dict.dept_name = dept.name
       departments_all.append(dept_dict)

    faculty_all = []
    for prof in faculty.objects.all():
       faculty_dict = faculty_info()
       faculty_dict.faculty_id = prof.faculty_id
       faculty_dict.faculty_name = prof.name
       faculty_dict.dept_id = prof.department_id.department_id
       faculty_dict.dept_name = prof.department_id.name
       faculty_all.append(faculty_dict)
    return render(request, "polls/faculty.html", {"faculty_list": faculty_all})


@cache_control(no_cache=True, must_revalidate=True)
def logout(request):
    global can_login 
    can_login = False
    # print("Logout function accessed")
    # print(can_login)
    request.session.flush()
    try:
        del request.session['user_id']
        del request.session['password']
    except KeyError:
        pass
    return render(request, 'polls/homepage.html',{'title':"homepage"})


@cache_control(no_cache=True, must_revalidate=True)
def faculty_logout(request):
    global can_faculty_login
    can_faculty_login = False
    #print(can_faculty_login)
    try:
        del request.session['user_id']
        del request.session['password']
    except KeyError:
        pass
    return render(request, 'polls/homepage.html', {'title': "homepage"})


def admin_login(request):
    return render(request, 'polls/admin_login.html', {'title': "admin_login"})


class student_info_for_course():
   student_id: any
   student_name: any
   student_dept_id: any
   student_dept_name: any
   enrollment_id:any
   grade:any

def view_students_in_a_course(request,course_id):
   enrolled_students = []
   for enroll in enrollment.objects.all():
       if enroll.course_id.course_id == course_id:
        student_taken = student_info_for_course()
        student_taken.student_name = enroll.student_id.name
        student_taken.student_id= enroll.student_id.student_id
        student_taken.student_dept_id = enroll.student_id.department_id.department_id
        student_taken.student_dept_name = enroll.student_id.department_id.name
        student_taken.enrollment_id = enroll.enrollment_id
        student_taken.grade = enroll.grade
        enrolled_students.append(student_taken) 
   return render(request, 'polls/show_courses_by_a_faculty.html', {'course_id':course_id,
                                                                   'course_name':course.objects.get(course_id=course_id).name,
                                                                   'students_taken':enrolled_students})

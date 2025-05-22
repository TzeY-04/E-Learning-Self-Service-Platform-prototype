from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.contrib.auth.decorators import login_required
from app.models import User,Student,Course,Assignment,CourseFeedback,video


def home(request):
    """Renders the home page."""
    request.session['logincheck'] = False
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year': datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Mr. Ali.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'E-Learning Self-Service',
            'message':'This platform is designed to provide users with easy access to educational content and course materials. It enables students to self-enroll in courses, access learning resources, track progress, and receive feedback from teacher.',
            'year':datetime.now().year,
        }
    )

def check_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        request.session['username'] = username
    users = User.objects.all()
    user_found = False    
    for user in users:
        if str(user.user_id) == user_id and user.user_name == username and user.user_password == password and user.user_type == user_type:
            request.session['logincheck'] = True
            user_found = True
            if user_type == "Teacher":
    
                return render(
                    request,
                    'app/teachermainpage.html',
                    {
                        'username':username,
                    }
                    )

            elif user_type == "Admin":
                return render(
                    request,
                    'app/adminmainpage.html',
                    {}
                    )

            elif user_type == "Student":
                return render(
                    request,
                    'app/studentmainpage.html',
                    {
                        'user_id':user_id
                    }
                    )

            elif user_type == "PManager":
                return render(
                    request,
                    'app/pmanagermainpage.html',
                    {}
                    )
                    
    if user_found == False:
        request.session['logincheck'] = False
        return render(
            request,
            'app/userlogin.html',
            {
                'year':datetime.now().year,
            }
            )

def logout(request):
    request.session['logincheck'] = False
    return render(
        request,
        'app/userlogin.html',
        {
            'year':datetime.now().year,
        }
        )

def ShowPurchasedCourse(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
    if request.method == 'POST':
        user_id = request.POST.get('user_id')  
    enrolledcourses = Student.objects.filter(user_id=user_id)
    return render(
        request,    
        'app/ShowPurchasedCourse.html',
        {
            'user_id': user_id,
            'enrolledcourses': enrolledcourses,
        }
        )

def OverseeEntirePlatform(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
    if request.method == 'POST':
        user_id = request.POST.get('user_id') 

    return render(
        request,
        'app/OverseeEntirePlatform.html',
        {'user_id': user_id}
    )


def ManageUserAccount(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
    if request.method == 'POST':
        user_id = request.POST.get('user_id') 
    return render(
        request,
        'app/ManageUserAccount.html',
        {
            'user_id':user_id,
        }
        )

def ShowContent(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
    if request.method == 'POST':
        user_id = request.POST.get('user_id') 
    courses = Course.objects.all()
    return render(
        request,
        'app/ShowContent.html',
        {
            'user_id':user_id,
            'courses':courses,
        }
        )

def studentmainpage(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
    return render(
        request,
        'app/studentmainpage.html',
        {'user_id':user_id}
        )

def pmanagermainpage(request):
    return render(
        request,
        'app/pmanagermainpage.html',
        {}
        )
    
def teachermainpage(request):
    username = request.POST.get('username')
    courses = Course.objects.filter(teacher_name=username)

    return render(
        request,
        'app/teachermainpage.html',
        { 
            'username': username,
            'courses': courses,
         }
        ) 

def adminmainpage(request):
    if request.method == 'POST':
        request.session['user_id'] = request.POST.get('user_id')
    user_id = request.session.get('user_id', None)
    return render(
        request,
        'app/adminmainpage.html',
        {'user_id': user_id}
    )

@login_required
def menu(request):
    check_employee = request.user.groups.filter(name='employee').exists()

    context = {
            'title':'Main Menu',
            'is_employee': check_employee,
            'year':datetime.now().year,
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)


def analytics_board(request):
    """Renders the Analytics Board page."""
    return render(
        request,
        'ExamineMarketTrends/analytics_board_page.html', 
        {
            'title': 'Analytics Board',
            'year': datetime.now().year,
        }
    )

def courses(request):
    username = request.GET.get('username')
    
    courses = Course.objects.filter(teacher_name=username)
    return render(
        request,
        'app/courses.html',
        {
            'username':username,
            'courses':courses,
        }
    )
    
def teacher_choice(request):
    if request.method == 'POST':
        teacherchoice = request.POST.get('teacherchoice')
        username = request.POST.get('username')
        course_id = request.POST.get('course_id')
        
    if teacherchoice == "Edit_course":
        course = Course.objects.get(course_id=course_id, teacher_name=username)
        return render(
            request,
            'CreateAndManageCourse/editcourse.html',
            {
                'course': course,
                'username': username,
            }
        )
    elif teacherchoice == "Create_assignment":

        return render(
            request,
            'CreateAndMarkAssignment/createAssignment.html',
            {
                'course_id': course_id,
                'username': username,
            }

        )   
    elif teacherchoice == "Mark_assignment":
        course = Course.objects.get(course_id=course_id, teacher_name=username)
        assignments = Assignment.objects.filter(course_id=course_id)
        return render(
            request,
            'CreateAndMarkAssignment/listassignment.html',
            {
                'course_id': course_id,
                'course': course,
                'username': username,
                'assignments': assignments,
            
            }
        )   
    elif teacherchoice == "View_student_progress":
        course = Course.objects.get(course_id=course_id)
        all_students = Student.objects.filter(
            course_id=course_id,
            teacher_name=username
        )

        seen_names = set()
        unique_students = []
        for student in all_students:
            if student.student_name not in seen_names:
                seen_names.add(student.student_name)
                unique_students.append(student)

        return render(
            request,
            'ViewStudentProgress/liststudentprogress.html',
            {
                'course_id': course_id,
                'username': username,
                'course': course,
                'students': unique_students,

            }
        )   
    else:
        return render(
            request,
            'app/teachermainpage.html',
            {
                'username': username,
            }
        )  
        


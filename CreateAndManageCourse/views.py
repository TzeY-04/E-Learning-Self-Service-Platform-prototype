from django.shortcuts import render
from app.models import Course,Teacher,User
from django.contrib import messages
from app.views import courses
# Create your views here.

def createcourse(request):
    username = request.POST.get('username')
    
    

    return render(
        request,
        'CreateAndManageCourse/createcourse.html',
        {
            'username':username,
        }
        )
    
    
def uploadcourse(request):
    username = request.POST.get('username')
    course_name = request.POST.get('course_name')
    course_price = request.POST.get('course_price')
    course_id = request.POST.get('course_id')
    courses = Course.objects.filter(teacher_name=username)
    
    if Teacher.objects.filter(course_id=course_id).exists():
        return render(
            request,
            'app/courses.html',
            {
                'username':username,
                'courses':courses,
                'error_message': "This course ID has already been taken. Please use a different one."
            }
        )
    else:
        course = Course(
            teacher_name=username,
            course_name=course_name,
            course_price=course_price,
            course_id=course_id,
            salesAmount= 0,
        )
        course.save()

        user = User.objects.get(user_name = username)
        teacher = Teacher(
            teacher_name=username,
            user_id = user,
            course_id = course,
            cooperate = b'0',
        )
        teacher.save()

        return render(
            request,
            'app/courses.html',
            {
                'username':username,
                'courses':courses,
            }
        )
    
def editcourse(request):
    username = request.POST.get('username')
    course_name = request.POST.get('course_name')
    course_price = request.POST.get('course_price')
    course_id = request.POST.get('course_id')
    
    
    course = Course.objects.get(course_id=course_id, teacher_name=username)
    
    course.course_name=course_name
    course.course_price=course_price
    
    
    course.save()
    
    courses = Course.objects.filter(teacher_name=username)
    
    return render(
        request,
        'app/courses.html',
        {
            'username':username,
            'courses':courses,
        }
    )
    
def deletecourse(request):
    print("Received POST data:", request.POST)
    username = request.POST.get('username')
    course_id = request.POST.get('course_id')
    
    print(f"Attempting to delete - Username: {username}, Course ID: {course_id}") 
    
    course = Course.objects.filter(course_id=course_id, teacher_name=username)
    if course.exists():
        course.delete()
        success_message = "Course successfully deleted"
    else:
        success_message = None
    
    courses = Course.objects.filter(teacher_name=username)
    
    return render(
        request,
        'app/courses.html',
        {
            'username': username,
            'courses': courses,
            'success_message': success_message,
        }
    )



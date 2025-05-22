from django.shortcuts import render
from app.models import CourseFeedback,Course,Student
# Create your views here.

def providefeedback(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        course_id = request.POST.get('course_id')
        courses = Course.objects.filter(course_id=course_id)
    return render(
        request,
        'ProvideFeedback/providefeedback.html',
        {
            'user_id':user_id,
            'course_id':course_id,
            'courses':courses,
        }
    )

def uploadfeedback(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        course_id = request.POST.get('course_id')
        studentfeedback = request.POST.get('feedback')

        course = Course.objects.get(course_id=course_id)
        feedback = CourseFeedback.objects.create(feedback = studentfeedback,course_id = course)
        feedback.save()
        enrolledcourses = Student.objects.filter(user_id=user_id)
    return render(
        request,
        'app/ShowPurchasedCourse.html',
        {
            'user_id':user_id,
            'enrolledcourses': enrolledcourses,
        }
    )
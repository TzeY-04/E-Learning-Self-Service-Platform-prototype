from django.shortcuts import render,get_object_or_404
from app.models import User,Course,video,Assignment,CourseFeedback,Student,StudentAssignment
# Create your views here.

def ShowCourseDetail(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
    elif request.method == 'GET':
        user_id = request.GET.get('user_id')
    courses = Course.objects.all()
    return render(
        request,
        'EnrollCourse/ShowCourseDetail.html',
        {
            'courses':courses,
            'user_id':user_id,
        }
    )

def select_course(request, course_id):
    user_id = request.POST.get('user_id')
    course = get_object_or_404(Course, course_id=course_id)
    coursefeedback = CourseFeedback.objects.filter(course_id=course)
    num_videos = video.objects.filter(course_id=course).count()
    num_assignments = Assignment.objects.filter(course_id=course).count()
    return render(
        request, 
        'EnrollCourse/CourseDetail.html', 
        {
            'course': course,
            'num_videos': num_videos,
            'num_assignments': num_assignments,
            'coursefeedback': coursefeedback,
            'user_id':user_id,
        }
        )

def enroll_course(request, course_id):
    user_id = request.POST.get('user_id')
    if request.method == 'POST':
        username = request.POST.get('username')
        course = get_object_or_404(Course, course_id=course_id)
        user_ID = get_object_or_404(User, user_id=user_id)
        assignments = Assignment.objects.filter(course_id=course_id)

    studentrecord = Student(student_name = username, 
                            user_id = user_ID, 
                            course_id = course, 
                            teacher_name = course.teacher_name
                            )
    studentrecord.save()

    course.salesAmount += 1
    course.save()
    
    for assignment in assignments:
        studentassignment = StudentAssignment(
            student_name=username,
            assignment_id=assignment, 
            assignment_mark=None
        )
        studentassignment.save()
    

    courses = Course.objects.all()
    return render(
        request,
        'EnrollCourse/ShowCourseDetail.html',
        {
            'courses':courses,
            'user_id':user_id,
        }
    )

from django.shortcuts import render, redirect, get_object_or_404
from app.models import Course, User, Student, Teacher, video, Assignment, CourseFeedback
from django.contrib import messages
from app.views import ShowContent

def course_list(request):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')
    course_id = request.GET.get('course_id')

    if not course_id:
        courses = Course.objects.all() 
        # check if course exists
        if not courses.exists():
            error_message = "No course registered."
        else:
            error_message = None
        
        return render(request, 'RemoveCourseVideo/courselist.html', {'courses': courses, 'user_id': user_id, 'error_message': error_message})

    course = get_object_or_404(Course, course_id=course_id)
    num_videos = video.objects.filter(course_id=course).count()

    return render(
        request,
        'RemoveCourseVideo/courselist.html',
        {
            'course': course,
            'num_videos': num_videos,
            'user_id': user_id,
            'error_message': None, 
        }
    )

def view_course(request, course_id):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')

    course = get_object_or_404(Course, course_id=course_id)

    videos = video.objects.filter(course_id=course)

    error_message = "No video for this course." if not videos.exists() else None

    return render(
        request,
        'RemoveCourseVideo/viewcourse.html',
        {
            'course': course,
            'videos': videos,
            'user_id': user_id,
            'error_message': error_message, 
        }
    )

def remove_course(request, course_id):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')

    course = get_object_or_404(Course, course_id=course_id)

    num_videos = video.objects.filter(course_id=course).count()

    num_assignment = Assignment.objects.filter(course_id=course).count()

    studentFeedback = CourseFeedback.objects.filter(course_id=course)

    return render(
        request,
        'RemoveCourseVideo/removecourse.html',
        {
            'course': course,
            'num_videos': num_videos,
            'num_assignment': num_assignment,
            'studentFeedback': studentFeedback,
            'user_id': user_id,
        }
    )

def confirm_delete_course(request, course_id):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')
    course = get_object_or_404(Course, course_id=course_id)
    course.delete()
    success_message = "Course successfully deleted."
    courses = Course.objects.all()
    return render(
        request,
        'RemoveCourseVideo/courselist.html',
        {
            'success_message': success_message,
            'user_id': user_id,
            'courses': courses,
        }
    )

def view_video(request, course_id, video_id):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')

    course = get_object_or_404(Course, course_id=course_id)

    video_obj = get_object_or_404(video, course_id=course, video_id=video_id)

    return render(
        request,
        'RemoveCourseVideo/viewvideos.html',
        {
            'course': course,
            'video': video_obj,
            'user_id': user_id,
        }
    )

def remove_video(request, course_id, video_id):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')

    course = get_object_or_404(Course, course_id=course_id)

    video_obj = get_object_or_404(video, course_id=course, video_id=video_id)

    return render(
        request,
        'RemoveCourseVideo/removevideo.html',
        {
            'course': course,
            'video': video_obj,
            'user_id': user_id,
        }
    )

def confirm_delete_video(request, course_id, video_id):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')
    course = get_object_or_404(Course, course_id=course_id)
    video_obj = get_object_or_404(video, course_id=course, video_id=video_id)
    video_obj.delete()
    success_message = "Video successfully deleted."
    videos = video.objects.filter(course_id=course)
    return render(
        request,
        'RemoveCourseVideo/courselist.html',
        {
            'success_message': success_message,
            'course': course,
            'videos': videos,
            'user_id': user_id,
        }
    )

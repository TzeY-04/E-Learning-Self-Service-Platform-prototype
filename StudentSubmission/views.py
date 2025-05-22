from django.shortcuts import render,get_object_or_404
from app.models import Course,Assignment,Student,StudentAssignment

# Create your views here.

def submission(request):
    user_id = request.POST.get('user_id')
    return render(
        request,
        'StudentSubmission/submission.html',
        {
            'user_id': user_id,
        }
    )

def assignmentsubmission(request):
    
    user_id = request.POST.get('user_id')
    course_id = request.POST.get('course_id')
    studentcourse = Student.objects.filter(course_id=course_id, user_id=user_id).first()

    if not studentcourse:
        return render(
            request,
            'StudentSubmission/assignmentsubmission.html',
            {
                'error_message': "You have not enrolled in this course. Please enroll before submitting an assignment.",
                'user_id': user_id,
            }
        )
    course = Course.objects.filter(course_id=course_id)
    assignment = Assignment.objects.filter(course_id=course_id)
    return render(
        request,
        'StudentSubmission/assignmentsubmission.html',
        {
            'user_id': user_id,
            'courses':course,
            'assignments':assignment,
        }
    )

def submit(request):
    user_id = request.POST.get('user_id')
    assignment_id = request.POST.get('assignment_id')
    assignment = Assignment.objects.filter(assignment_id=assignment_id)
    return render(
        request,
        'StudentSubmission/submit.html',
        {
            'user_id': user_id,
            'assignment': assignment
        }
    )

def uploadfile(request):
    user_id = request.POST.get('user_id')
    file_path = request.POST.get('file_path')
    assignment_id = request.POST.get('assignment_id')
    student = Student.objects.filter(user_id=user_id).first()
    student_assignment= StudentAssignment.objects.get(assignment_id=assignment_id,student_name=student.student_name)
    student_assignment.assignment_file_path=file_path
    student_assignment.save()
    return render(
        request,
        'StudentSubmission/submission.html',
        {
            'user_id': user_id,
        }
    )
from django.shortcuts import render, redirect
from app.models import Assignment, Course, StudentAssignment, Student


def createassignment(request):
    course_id = request.POST.get('course_id')
    assignment_id = request.POST.get('assignment_id')  
    assignment_title = request.POST.get('assignment_title')
    assignment_content = request.POST.get('assignment_content')
    assignment_fullmark = request.POST.get('assignment_fullmark')
    username = request.POST.get('username')
    error_message = None
    courses = Course.objects.filter(teacher_name=username)
    assignment = Assignment.objects.filter(assignment_id=assignment_id)

    if assignment.exists():
        error_message = "Assignment ID already exists. Please choose a unique ID."


        return render(
            request, 
            'CreateAndMarkAssignment/createAssignment.html', 
            {
                'courses': courses,
                'error_message': error_message,
                'username': username
                }
            )
        
    try:
        course_id = Course.objects.get(course_id=course_id)
    except Course.DoesNotExist:
        error_message = "Course not found."

        return render(
            request, 
            'app/courses.html', 
            {
            'courses': courses,
            'error_message': error_message,
            'username': username
            }
        )

    success_message = "Assignment created successfully."
    
    Assignment.objects.create(
        assignment_id=assignment_id,
        assignment_title=assignment_title,
        assignment_content=assignment_content,
        assignment_fullmark=assignment_fullmark,
        course_id=course_id
    )
    
    students = Student.objects.filter(course_id=course_id)
    createdassignment = Assignment.objects.get(assignment_id=assignment_id)
    for student in students:
        studentas=StudentAssignment(
            student_name = student.student_name,
            assignment_id = createdassignment,
            assignment_mark = None,
            assignment_file_path = None,
        )
        studentas.save()
    
    return render(
        request,
        'app/courses.html',
        {
            'username': username,
            'courses': courses,
            'success_message': success_message
        }
    )




def listassignment(request):
    assignment_id = request.POST.get('assignment_id')
    username = request.POST.get('username')
    assignment = Assignment.objects.get(assignment_id=assignment_id)
    submissions = StudentAssignment.objects.filter(assignment_id=assignment_id)

    return render(
        request,

        'CreateAndMarkAssignment/viewassignmentsubmission.html',
        {
            'username': username,
            'submissions': submissions,
            'assignment_id': assignment_id,
            'assignment': assignment,
        }
    )



def viewassignmentsubmission(request):
    assignment_id = request.POST.get('assignment_id')
    username = request.POST.get('username')
    submission_id = request.POST.get('submission_id')
    student_name = request.POST.get('student_name')
    assignment = Assignment.objects.get(assignment_id=assignment_id)
    submissions = StudentAssignment.objects.get(assignment_id=assignment_id, id=submission_id, student_name=student_name)

    if submissions.assignment_file_path:
        return render(
            request,
            'CreateAndMarkAssignment/markassignment.html',
        {
            'assignment': assignment,
            'username': username,
            'submissions': submissions,
            'assignment_id': assignment_id,
        }
    )
        
    else:
        error_message = "Assignment not submitted."
        courses = Course.objects.filter(teacher_name=username)
        return render(
            request,
            'app/courses.html',
            {

                'courses': courses,
                'username': username,
                'error_message': error_message
            }
        )
        
    


def markassignment(request):
    username = request.POST.get('username')
    courses = Course.objects.filter(teacher_name=username)
    assignment_mark = request.POST.get('assignment_mark')
    submission_id = request.POST.get('submission_id')
    student_name = request.POST.get('student_name')
    assignment_id = request.POST.get('assignment_id')
    
    
    try:
        assignment_mark = int(assignment_mark)
    except (ValueError, TypeError):
        assignment_mark = None
        
    try:
        student_assignment = StudentAssignment.objects.get(assignment_id=assignment_id, student_name=student_name, id=submission_id)
        student_assignment.assignment_mark = assignment_mark
        student_assignment.save() 
        success_message = "Assignment marked successfully."
    except StudentAssignment.DoesNotExist:
        success_message = "Student assignment not found."
    
    
    return render(
        request,
        'app/courses.html',
        {
            'username': username,
            'courses': courses,
            'success_message': success_message
        }
    )

from django.shortcuts import render, get_object_or_404
from app.models import Student,Course,StudentAssignment,TeacherFeedback,Teacher,User
from django.http import HttpResponse
# Create your views here.
def liststudentprogress(request):
    username = request.POST.get('username')
    course_id = request.POST.get('course_id')
    student_name = request.POST.get('student_name')
    
    assignments = StudentAssignment.objects.filter(
        student_name=student_name,
        assignment_id__course_id=course_id
    )
    
    students = Student.objects.filter(course_id=course_id)
    return render(
        request, 
        'ViewStudentProgress/showstudentprogress.html', 
        {
            'selected_student': student_name, 
            'username': username, 
            'course_id': course_id,
            'assignments': assignments
        }
    )

def showstudentprogress(request):
    if request.method == 'POST':
        teacher_feedback_text = request.POST.get('teacher_feedback')
        student_name = request.POST.get('student_name')
        course_id = request.POST.get('course_id')
        username = request.POST.get('username')  
        
        teacher = Teacher.objects.filter(teacher_name=username).first()
        user_obj = get_object_or_404(User, user_name=username)
        course = get_object_or_404(Course, course_id=course_id)
        
        TeacherFeedback.objects.create(
            teacher_feedback = teacher_feedback_text,
            teacher_name     = teacher.teacher_name,  
            student_name     = student_name,
            user_id          = user_obj,         
            course_id        = course
        )
        
        courses = Course.objects.filter(teacher_name=username)
        return render(request, 
            'app/courses.html', 
            {
                'username': username,
                'courses': courses,
                'success_message': "Feedback submitted successfully!"
            }
        )
    

    username = request.POST.get('username')
    courses = Course.objects.filter(teacher_name=username)
    return render(request, 
        'app/courses.html', 
        {
            'username': username,
            'courses': courses
        }
    )




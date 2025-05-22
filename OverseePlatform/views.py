from django.shortcuts import render, redirect, get_object_or_404
from app.models import Course, User, Student, Teacher, video, Assignment, StudentAssignment
from django.contrib import messages
from app.views import OverseeEntirePlatform

def all_purchased(request):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')
    studentenrolls = Student.objects.select_related('course_id').all() 
    return render(
        request, 
        'OverseePlatform/allPurchased.html', 
        {
            'studentenrolls': studentenrolls, 
            'user_id': user_id,
        }
    )

def all_progress(request):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')
    students = Student.objects.all()
    studentassignments = StudentAssignment.objects.all()

    return render(
        request, 
        'OverseePlatform/allProgress.html', 
        {
            'students': students, 
            'user_id': user_id, 
            'studentassignments': studentassignments,
        }
    )

def have_marks(request):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')
    assignments = Assignment.objects.all()
    
    # Filter StudentAssignment objects to include only those with non-null assignment_mark
    studentassignments_with_marks = StudentAssignment.objects.filter(assignment_mark__isnull=False)
    
    # Get unique student names from the filtered assignments
    student_names_with_marks = studentassignments_with_marks.values_list('student_name', flat=True).distinct()
    
    # Filter Student objects based on the student names with marks
    students_with_marks = Student.objects.filter(student_name__in=student_names_with_marks)
    
    # Attach the filtered assignments to each student
    for student in students_with_marks:
        student.mark = studentassignments_with_marks.filter(student_name=student.student_name)
    
    students = Student.objects.all()
    studentassignments = StudentAssignment.objects.all()
    return render(
        request, 
        'OverseePlatform/haveMarks.html', 
        {
            'students': students, 
            'user_id': user_id, 
            'studentassignments': studentassignments,
        }
    )



def no_marks(request):
    user_id = request.POST.get('user_id') if request.method == 'POST' else request.GET.get('user_id')
    students = Student.objects.all()
    studentassignments = StudentAssignment.objects.all()

    return render(
        request, 
        'OverseePlatform/noMarks.html', 
        {
            'students': students, 
            'user_id': user_id, 
            'studentassignments': studentassignments,
        }
    )
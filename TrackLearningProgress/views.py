from django.shortcuts import render
from app.models import User,StudentAssignment,Course,TeacherFeedback 
# Create your views here.

def track_learning_progress(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        course_id = request.POST.get('course_id')

        user = User.objects.filter(user_id=user_id).first()
        user_name = user.user_name
        studentassignments=StudentAssignment.objects.filter(student_name=user_name)

        teacherfeedback = TeacherFeedback.objects.filter(course_id=course_id,student_name=user_name)
        courses = Course.objects.filter(course_id=course_id)
    return render(
        request,
        'TrackLearningProgress/track_learning_progress.html',
        {
            'user_id':user_id,
            'courses':courses,
            'studentassignments':studentassignments,
            'teacherfeedbacks':teacherfeedback,
        }
    )
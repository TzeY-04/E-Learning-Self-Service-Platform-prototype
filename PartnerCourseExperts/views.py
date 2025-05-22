from django.shortcuts import render
from app.models import Teacher

# Create your views here.

def invite_course_experts(request):
    teacher=Teacher.objects.filter(cooperate=b'0')
    return render(
        request,
        'PartnerCourseExperts/InviteCourseExperts.html',
        {
            'teachers':teacher
        }
    )
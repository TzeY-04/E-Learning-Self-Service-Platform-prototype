from django.shortcuts import render
from app.models import Survey,SurveyAnswer


# Create your views here.

def create_survey(request):
    return render(
        request,
        'EnhanceUserExperience/SurveyCreation.html',
        {
        
        }
    )


def creating_survey(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        survey_question = request.POST.get('survey_question')
        survey_name = request.POST.get('survey_name')
    survey_save = Survey(question_id = question_id, 
                            survey_question = survey_question,
                            survey_name = survey_name, 
                            )
    survey_save.save()

    return render(
        request,
        'EnhanceUserExperience/SurveyCreation.html',
        {
        
        }
    )
    
def show_survey_reply(request):
    if request.method == 'POST':
        survey_name = request.POST.get('survey_name')
    surveys = Survey.objects.filter(survey_name=survey_name)
    return render(
        request,
        'EnhanceUserExperience/ShowSurveyReply.html',
        {
            'surveys':surveys
        }
    )

def show_survey(request):
    surveys=Survey.objects.all()
    return render(
        request,
        'EnhanceUserExperience/ShowSurvey.html',
        {
            'surveys':surveys
        }
    )
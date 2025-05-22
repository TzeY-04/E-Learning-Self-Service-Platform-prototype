from django.shortcuts import render
from app.models import Course,CourseFeedback

# Create your views here.

def analytics_board_page(request):

    return render(
        request,
        'ExamineMarketTrends/AnalyticsBoardPage.html',
        {}
    )


def user_feedback(request):
    feedback=CourseFeedback.objects.filter()
    feedback_num=CourseFeedback.objects.filter().count()
    
    return render(
        request,
        'ExamineMarketTrends/UserFeedback.html',
        {
            'feedbackAll':feedback,
            'NumFeedback':feedback_num
        }
    )

def sales_performance(request):
    course_sales_amount=Course.objects.filter()
    course=Course.objects.filter()
    
    return render(
        request,
        'ExamineMarketTrends/SalesPerformance.html',
        {
            'NumSalesAmount':course_sales_amount,
            'courseAll':course
        }
    )

def user_feedback_report(request):
    feedback=CourseFeedback.objects.filter()
    feedback_num=CourseFeedback.objects.filter().count()
    
    return render(
        request,
        'ExamineMarketTrends/UserFeedbackReport.html',
        {
            'feedbackAll':feedback,
            'NumFeedback':feedback_num
        }
    )


def sales_performance_report(request):
    course_sales_amount=Course.objects.filter()
    course=Course.objects.filter()
    
    return render(
        request,
        'ExamineMarketTrends/SalesPerformanceReport.html',
        {
            'NumSalesAmount':course_sales_amount,
            'courseAll':course
        }
    )


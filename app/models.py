"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User

#sharing entity

class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    item_name = models.TextField()
    item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.item_id)

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=10)
    user_name = models.TextField(max_length=30)
    user_password = models.CharField(max_length=10)
    user_type = models.CharField(max_length=10)
    def __str__(self):
        return str(self.user_id)

class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    course_name = models.CharField(max_length=30)
    course_price = models.IntegerField()
    teacher_name = models.CharField(max_length=30)
    salesAmount = models.IntegerField()

class video(models.Model):
    video_id = models.CharField(primary_key=True, max_length=10)
    video_path = models.CharField(max_length=250)
    video_title = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE) 

class Assignment(models.Model):
    assignment_id = models.CharField(primary_key=True, max_length=10)
    assignment_fullmark = models.IntegerField()
    assignment_content = models.TextField()
    assignment_title = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE) 

class Student(models.Model):
    student_name = models.TextField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,null=True, blank=True) 
    teacher_name = models.TextField(max_length=30,null=True, blank=True)

class StudentAssignment(models.Model):
    student_name = models.TextField(max_length=30)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE,null=True, blank=True) 
    assignment_mark = models.IntegerField(null=True, blank=True)
    assignment_file_path= models.CharField(max_length=300,null=True, blank=True)

class CourseFeedback(models.Model):
    feedback = models.TextField(max_length=200)
    course_id =  models.ForeignKey(Course, on_delete=models.CASCADE,null=True, blank=True)

class Teacher(models.Model):
    teacher_name =  models.TextField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,null=True, blank=True) 
    cooperate = models.BinaryField(default=b'0')

class TeacherFeedback(models.Model):
    teacher_feedback = models.TextField(null=True, blank=True)
    teacher_name =  models.TextField(max_length=30)
    student_name = models.TextField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id =  models.ForeignKey(Course, on_delete=models.CASCADE,null=True, blank=True)
    
class Survey(models.Model):
    question_id=models.CharField(primary_key=True,max_length=10)
    survey_question=models.TextField(max_length=300)
    survey_name=models.TextField(max_length=300)
    survey_ans_yes=models.IntegerField(default=0)
    survey_ans_no=models.IntegerField(default=0)

class SurveyAnswer(models.Model):
    question_id=models.ForeignKey(Survey,on_delete=models.CASCADE)
    survey_answer=models.BinaryField(default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


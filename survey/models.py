from multiprocessing.connection import answer_challenge
from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=200, primary_key = True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    
class SurveyQuestion(models.Model):
    question = models.CharField(max_length=200)
    surveyTitle = models.ForeignKey(Survey, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question

class SurveyQuestionAlternative(models.Model):
    questionAlternative = models.CharField(max_length=200)
    surveyQuestion = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    def __str__(self):
        return self.questionAlternative

class SurveyUserAnswer(models.Model):
    surveyQuestionAlternative = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    def __str__(self):
        return self.answer
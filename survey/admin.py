from django.contrib import admin
from .models import SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer, Survey

admin.site.register(SurveyQuestion)
admin.site.register(Survey)
admin.site.register(SurveyQuestionAlternative)
admin.site.register(SurveyUserAnswer)

# Register your models here.

from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from survey.models import Survey
from . import views



class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ['title','pub_date']
        

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

router = routers.DefaultRouter()
router.register(r'surveys', SurveyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')


]
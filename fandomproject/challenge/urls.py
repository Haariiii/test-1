from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ChallengeMain,ChallengeOne,ChallegeUpload1,ChallengeCompareResult

app_name = 'challenge'

urlpatterns = [
    path('',ChallengeMain.as_view(),name='index'),
    path('/1',ChallengeOne.as_view(),name='one'),
    path('/1/upload',ChallegeUpload1.as_view(),name='upload1'),
    path('/1/challenge_result', ChallengeCompareResult.as_view(), name='compare'),
    path('/1/test_upload', views.upload_video, name='test')
]# path('/1/challenge_result', ChallengeCompareResult.as_view(), name='compare'),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# 개발 환경에서만 media 파일을 제공하기 위한 설정
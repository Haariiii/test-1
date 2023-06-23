from django.shortcuts import render
from rest_framework.views import APIView
from .forms import VideoForm
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from dance_30 import compare_video
from .models import Video
from django.db.models import Max
from .models import Score
# Create your views here.

# /videogallery 경로 인식 후 index함수가 호출 됨 index함순s html을 렌더링 context포함해서

class ChallengeMain(APIView):
    def get(self,request):
        challenges = Score.objects.all()
        context = {'challenges' : challenges}
        return render(request, "challenge/challenge.html", context)
    
class ChallengeOne(APIView):
    def get(self,request):
        return render(request,"challenge/ch1.html")
    
class ChallegeUpload1(APIView):
    def get(self,request):
        return render(request,"challenge/ch1.html")
    def post(self, request):
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            return Response({'video': video.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ChallengeCompareResult(APIView):
    def get(self, request):
        latest_video_id = Video.objects.all().aggregate(Max('id'))['id__max']
        video = Video.objects.get(id=latest_video_id)
        # print(video.video_file)
        video_path = f"./media/{video.video_file}"
        score = compare_video('challenge/static/video/knock1.mp4', video_path)
        nickname = request.user.nickname
        title = 'sample Title'
        score_instance = Score(user=request.user, nickname=nickname, score=score, title=title)
        score_instance.save()
        return render(request, "challenge/compare_result.html", {'score': score})
        # return render(request, "challenge/compare_result.html", {'score': 0})


######################################
from .forms import VideoForm

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()  # 동영상 저장
            # 모델에 동영상을 받아오는 로직 추가
            return render(request, "challenge/success.html")
    else:
        form = VideoForm()
    
    return render(request, 'challenge/upload.html', {'form': form})

# class upload_video(APIView):
#     def get(self, request):
#         return render(request, )
#     def upload_video(request):
#         if request.method == 'POST' and request.FILES['files']:
#             form = VideoForm(request.POST, request.FILES)
#             if form.is_valid():
#                 video = form.save()  # 동영상 저장
#                 # 모델에 동영상 전달하여 처리
#                 score = compare_video('challenge/static/video/knock_step.mp4', video)
#                 return render(request, "challenge/compare_result.html", {'score': score})
#         else:
#             form = VideoForm()
        
#         return render(request, 'ch1.html', {'form': form})


###################################################


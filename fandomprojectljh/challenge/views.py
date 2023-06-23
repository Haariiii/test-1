from django.db import models
from django.shortcuts import render
from rest_framework.views import APIView
from .forms import VideoForm
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from dance_30 import compare_video
from .models import *
from django.db.models import Max
from .forms import VideoForm


# Create your views here.

# /videogallery 경로 인식 후 index함수가 호출 됨 index함순s html을 렌더링 context포함해서

class ChallengeMain(APIView):
    def get(self,request):
        return render(request, "challenge/challenge.html")
    
class ChallengeOne(APIView):
    def get(self,request, pk):
        challenge = Ref_Video.objects.get(id=pk)
        return render(request,"challenge/ch1.html", {'challenge': challenge})
    
# class ChallegeUpload1(APIView):
#     def get(self,request):
#         return render(request,"challenge/ch1.html")
#     def post(self, request):
#         form = VideoForm(request.POST, request.FILES)
#         if form.is_valid():
#             video = form.save()
#             return Response({'video': video.id}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ChallengeCompareResult(APIView):
    def get(self, request, pk):
        challenge = Ref_Video.objects.get(id=pk)
        # print("="*100, pk, "="*100)
        
        ref_path = f"./media/{challenge.video_file}"
        # print("="*100, ref_path, "="*100)
        
        latest_video_id = Video.objects.all().aggregate(Max('id'))['id__max']
        video = Video.objects.get(id=latest_video_id)
        # print(video.video_file)
        video_path = f"./media/{video.video_file}"
        print("="*100, video_path, "="*100)
        
        score = compare_video(ref_path, video_path)
        
        context = {
            'score': score,
            'challenge': challenge
        }
        return render(request, "challenge/compare_result.html", context)


######################################

# 동영상 업로드
def upload_video(request, pk):
    challenge = Ref_Video.objects.get(id=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        form.ref_id = pk
        print('='*100, form.ref_id, '='*100)
        
        if form.is_valid():
            video = form.save(commit=False)  # commit=False를 사용하여 객체를 임시로 저장
            video.ref_id = pk  # 동영상 객체에 ref_id 할당
            video.save()  # 동영상 객체를 저장
            context = {
                'form': form,
                'challenge': challenge,  # challenge 객체 추가
            }
            return render(request, "challenge/success.html", context)
    else:
        form = VideoForm()
        form.ref_id = pk
        # print('-'*100, form.ref_id, '-'*100)
        
        context = {
            'form': form,
            'challenge': challenge,  # challenge 객체 추가
        }
    return render(request, 'challenge/upload.html', context)
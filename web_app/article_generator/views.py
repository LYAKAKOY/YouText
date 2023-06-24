import asyncio
import os
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .downloading_youtube_pictures import download_picture_from_video
from .forms import VideoUrlForm
from .downloading_youtube_videos import download_video, video_cropping, audio_cropping
from .speech_recognition import speech_recognition_base
from .tasks import task_download_audio
from .youtube_video import get_info_about_video


# Create your views here.
def generator(request):
    if request.method == 'POST':
        form = VideoUrlForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            task_download_audio.delay(video_url)
            download_video(video_url)
            info_about_video = get_info_about_video(video_url)
            video_data = info_about_video['items'][0]['snippet']
            audio_cropping(form.cleaned_data['start_time'], form.cleaned_data['end_time'])
            video_cropping(form.cleaned_data['start_time'], form.cleaned_data['end_time'])
            if form.cleaned_data['interval_picture']:
                asyncio.run(download_picture_from_video('video/youtube_video.mp4',
                                                        interval_seconds=form.cleaned_data['interval_picture']))
            else:
                asyncio.run(download_picture_from_video('video/youtube_video.mp4', 10))
            text = speech_recognition_base()
            os.remove('./audio/youtube_audio.mp3')
            os.remove('./video/youtube_video.mp4')
            return render(request, 'article_generator/html/generated.html', {
                'text': text, 'name_channel': video_data['channelTitle'],
                'annotation_length': form.cleaned_data['annotation_length'] or 'не задано',
                'article_length': form.cleaned_data['article_length'] or 'не задано',
                'interval_picture': form.cleaned_data['interval_picture'] or 20,
                'video': video_url
            })

    else:
        form = VideoUrlForm()
        return render(request, 'article_generator/html/index.html', {'form': form})


def logout_social(request):
    logout(request)
    return redirect('/')
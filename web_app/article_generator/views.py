import os
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import VideoUrlForm
from .downloading_youtube_videos import download_video, video_cropping, audio_cropping
from .speech_recognition import speech_recognition_base
from .tasks import task_download_audio, task_download_pictures
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
            audio_cropping(form.cleaned_data['start_time'], form.cleaned_data['end_time'])
            video_cropping(form.cleaned_data['start_time'], form.cleaned_data['end_time'])
            if form.cleaned_data['interval_picture']:
                task_download_pictures('video/youtube_video.mp4',
                                       interval_seconds=form.cleaned_data['interval_picture'])
            else:
                task_download_pictures('video/youtube_video.mp4')
            text = speech_recognition_base()
            os.remove('./audio/youtube_audio.mp3')
            os.remove('./video/youtube_video.mp4')
            file_list = os.listdir("./pictures_youtube")
            for file_name in file_list:
                file_path = os.path.join('./pictures_youtube', file_name)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            return render(request, 'article_generator/html/text.html', {'text': text})

    else:
        form = VideoUrlForm()
        return render(request, 'article_generator/html/index.html', {'form': form})


def logout_social(request):
    logout(request)
    return redirect('/')
from celery.result import AsyncResult
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import VideoUrlForm
from .downloading_youtube_videos import download_video, video_cropping
from .speech_recognition import speech_recognition_base
from .tasks import task_download_audio, task_audio_cropping, delete_file
from .youtube_video import get_info_about_video, get_video_duration, get_video_id


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
            duration = get_video_duration('video/youtube_video.mp4')

            task = task_audio_cropping.delay(form.cleaned_data['start_time'], form.cleaned_data['end_time'])
            task_result = AsyncResult(task.id)
            video_cropping(form.cleaned_data['start_time'], form.cleaned_data['end_time'])
            task_result.wait()

            if form.cleaned_data['annotation_length']:
                text = speech_recognition_base(form.cleaned_data['annotation_length'],
                                               form.cleaned_data['interval_picture'])
            else:
                text = speech_recognition_base(form.cleaned_data['interval_picture'])

            delete_file.delay()

            context = {
                'text': text,
                'name_channel': video_data['channelTitle'],
                'annotation_length': form.cleaned_data['annotation_length'] or 'не задано',
                'article_length': form.cleaned_data['article_length'] or 'не задано',
                'interval_picture': form.cleaned_data['interval_picture'] or 10,
                'video': get_video_id(video_url),
                'duration': duration
            }
            return render(request, 'article_generator/html/generated.html', context)

    else:
        form = VideoUrlForm()
        return render(request, 'article_generator/html/index.html', {'form': form})


def logout_social(request):
    logout(request)
    return redirect('/')

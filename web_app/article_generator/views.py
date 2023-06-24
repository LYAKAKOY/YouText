from django.shortcuts import render
from .forms import VideoUrlForm
from .downloading_youtube_videos import download_video, video_cropping
from .speech_recognition import speech_recognition_base
from .tasks import task_download_audio, task_download_pictures, task_audio_cropping
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
            task_audio_cropping.delay(form.cleaned_data['start_time'], form.cleaned_data['end_time'])
            video_cropping(form.cleaned_data['start_time'], form.cleaned_data['end_time'])
            if form.cleaned_data['interval_picture']:
                task_download_pictures('video/youtube_video.mp4',
                                       interval_seconds=form.cleaned_data['interval_picture'])
            else:
                task_download_pictures('video/youtube_video.mp4')
            text = speech_recognition_base()
            return render(request, 'article_generator/html/text.html', {'text': text})

    else:
        form = VideoUrlForm()
        return render(request, 'article_generator/html/greet_page.html', {'form': form})

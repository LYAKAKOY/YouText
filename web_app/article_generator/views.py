from django.shortcuts import render
from .forms import VideoUrlForm
from .downloading_youtube_videos import download_video
from .speech_recognition import speech_recognition_base
from .tasks import task_download_audio, task_download_pictures


# Create your views here.
def generator(request):
    if request.method == 'POST':
        form = VideoUrlForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            task_download_audio.delay(video_url)
            download_video(video_url)
            text = speech_recognition_base()
            task_download_pictures('video/youtube_video.mp4', 10, 30.0)
            return render(request, 'article_generator/html/text.html', {'text': text})

    else:
        form = VideoUrlForm()
        return render(request, 'article_generator/html/greet_page.html', {'form': form})

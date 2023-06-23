from celery import shared_task
from .downloading_youtube_videos import download_audio


@shared_task
def task_download_audio(video_url: str) -> None:
    download_audio(video_url)
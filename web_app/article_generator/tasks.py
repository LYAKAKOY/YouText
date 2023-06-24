import datetime
from celery import shared_task
from .downloading_youtube_videos import download_audio, audio_cropping
from .downloading_youtube_pictures import download_picture_from_video


@shared_task
def task_download_audio(video_url: str) -> None:
    download_audio(video_url)


@shared_task
def task_audio_cropping(start_time: datetime.time, end_time: datetime.time) -> None:
    audio_cropping(start_time, end_time)


@shared_task
def task_download_pictures(video_path: str, interval_seconds: int = 10) -> None:
    download_picture_from_video(video_path, interval_seconds)

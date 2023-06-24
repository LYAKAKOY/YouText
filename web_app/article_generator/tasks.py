import asyncio
import datetime
from celery import shared_task
from .downloading_youtube_videos import download_audio, audio_cropping
from .downloading_youtube_pictures import download_picture_from_video


@shared_task
def task_download_audio(video_url: str) -> None:
    download_audio(video_url)


@shared_task
def task_download_picture_from_video(interval: int = 10) -> None:
    if interval:
        download_picture_from_video('video/youtube_video.mp4',
                                    interval_seconds=interval)
    else:
        download_picture_from_video('video/youtube_video.mp4', interval)


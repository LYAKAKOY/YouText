import asyncio
from celery import shared_task
from .downloading_youtube_videos import download_audio
from .downloading_youtube_pictures import download_picture_from_video


@shared_task
def task_download_audio(video_url: str) -> None:
    download_audio(video_url)


@shared_task
def task_download_pictures(video_path: str, interval_seconds: int, threshold: float | int) -> None:
    asyncio.run(download_picture_from_video(video_path, interval_seconds, threshold))

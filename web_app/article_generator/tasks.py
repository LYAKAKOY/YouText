import datetime
import os
from celery import shared_task
from .downloading_youtube_videos import download_audio, audio_cropping
from .downloading_youtube_pictures import download_picture_from_video


@shared_task
def task_download_audio(video_url: str) -> None:
    download_audio(video_url)


@shared_task
def delete_file() -> None:
    os.remove('./audio/youtube_audio.mp3')
    os.remove('./video/youtube_video.mp4')
    file_list = os.listdir("./pictures_youtube")
    for file_name in file_list:
        file_path = os.path.join('./pictures_youtube', file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


@shared_task
def task_audio_cropping(start_time: datetime.time, end_time: datetime.time) -> None:
    audio_cropping(start_time, end_time)


@shared_task
def task_download_picture_from_video(interval: int | None) -> None:
    if interval:
        download_picture_from_video('video/youtube_video.mp4',
                                    interval_seconds=interval)
    else:
        download_picture_from_video('video/youtube_video.mp4', interval)

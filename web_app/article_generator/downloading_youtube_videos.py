from datetime import datetime
from pydub import AudioSegment
import youtube_dl
from moviepy.video.io.VideoFileClip import VideoFileClip


def download_video(video_url: str) -> None:
    # Опции для скачивания только видео
    video_options = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': './video/youtube_video.mp4',
    }

    ydl = youtube_dl.YoutubeDL(video_options)
    ydl.download([video_url])


def download_audio(video_url: str) -> None:
    audio_options = {
        'format': 'bestaudio/best',
        'outtmpl': './audio/youtube_audio.mp3',
    }
    ydl = youtube_dl.YoutubeDL(audio_options)
    ydl.download([video_url])


def video_cropping(start_time: datetime.time, end_time: datetime.time) -> None:
    video_path = './video/youtube_video.mp4'
    video = VideoFileClip(video_path)

    # Преобразуем время в секунды
    start_seconds = start_time.hour * 3600 + start_time.minute * 60 + start_time.second
    end_seconds = end_time.hour * 3600 + end_time.minute * 60 + end_time.second

    # Обрезаем видео
    cropped_video = video.subclip(start_seconds, end_seconds)
    cropped_video.write_videofile(video_path)


def audio_cropping(start_time: datetime.time, end_time: datetime.time) -> None:
    # Загружаем аудиофайл
    audio_path = './audio/youtube_audio.mp3'
    audio = AudioSegment.from_file(audio_path)

    # Преобразуем время начала и время окончания в миллисекунды

    start_ms = (start_time.hour * 3600 + start_time.minute * 60 + start_time.second) * 1000
    end_ms = (end_time.hour * 3600 + end_time.minute * 60 + end_time.second) * 1000

    cropped_audio = audio[start_ms:end_ms]

    cropped_audio.export(audio_path, format='mp3')

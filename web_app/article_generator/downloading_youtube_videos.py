import youtube_dl


def download_video(video_url: str) -> None:
    # Опции для скачивания только видео
    video_options = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': './video/youtube_vido.mp4',
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

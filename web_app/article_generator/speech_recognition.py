import os
import whisper
from autocorrect import Speller
import shutil
from celery.result import AsyncResult
from .tasks import task_download_picture_from_video
from .ru_model_rext import generate_text

model = whisper.load_model("base")
spell = Speller(lang='ru')


def speech_recognition_base(interval: int | None, n: int = 100) -> str:
    global model
    if interval is None:
        task = task_download_picture_from_video.delay()
    else:
        task = task_download_picture_from_video.delay(interval)
    task_result = AsyncResult(task.id)
    result = model.transcribe("./audio/youtube_audio.mp3", fp16=False)
    text = "<center><b>Аннотация</b></center>" + generate_text(result['text'], n) + '.</br> <center><b>Основной текст</b></center>'
    task_result.wait()
    capture = ''
    for segment in result['segments']:
        text += f"[{round(segment['start'], 2)}:{round(segment['end'], 2)}] {segment['text']}"
        for part in range(int(segment['start']) - 5, int(segment['start'])):
            if os.path.exists(f"pictures_youtube/picture_time{part}.jpg"):
                shutil.move(f"pictures_youtube/picture_time{part}.jpg",
                            f'article_generator/static/article_generator/picture/picture_time{part}.jpg')
                text += f"<img contenteditable=\"false\" class=\"textarea__img\" src=\'/static/article_generator/picture/picture_time{part}.jpg\' >"
                break
    return spell(text)

import os
import whisper
from autocorrect import Speller
import shutil
from .text_processing import extract_summary

model = whisper.load_model("base")
spell = Speller(lang='ru')


def speech_recognition_base(n: int = 100) -> str:
    global model
    result = model.transcribe("./audio/youtube_audio.mp3", fp16=False)
    text = "<center><b>Аннотация</b></center></br>" + extract_summary(result['text'], n).capitalize() + '.</br> <center><b>Основной текст</b></center>'
    for segment in result['segments']:
        text += f"[{round(segment['start'], 2)}:{round(segment['end'], 2)}] {segment['text']}"
        for part in range(int(segment['start']) - 5, int(segment['start'])):
            if os.path.exists(f"pictures_youtube/picture_time{part}.jpg"):
                shutil.move(f"pictures_youtube/picture_time{part}.jpg",
                            f'article_generator/static/article_generator/picture/picture_time{part}.jpg')
                text += f"<img contenteditable=\"false\" class=\"textarea__img\" src=\'/static/article_generator/picture/picture_time{part}.jpg\' >"
                break
    return spell(text)

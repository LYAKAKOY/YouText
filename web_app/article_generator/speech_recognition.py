import os
import whisper
from autocorrect import Speller
import shutil

model = whisper.load_model("base")
spell = Speller(lang='ru')


def speech_recognition_base():
    global model
    result = model.transcribe("./audio/youtube_audio.mp3", fp16=False)
    text = ''
    for segment in result['segments']:
        text += f"[{round(segment['start'], 2)}:{round(segment['end'], 2)}] {segment['text']}"
        for part in range(int(segment['start']) - 5, int(segment['start'])):
            if os.path.exists(f"pictures_youtube/picture_time{part}.jpg"):
                shutil.move(f"pictures_youtube/picture_time{part}.jpg",
                            f'article_generator/static/article_generator/picture_time{part}.jpg')
                text += f"<img src=\'/static/article_generator/picture_time{part}.jpg\' >"
                break
    return spell(text)

import whisper
from autocorrect import Speller

model = whisper.load_model("base")
spell = Speller(lang='ru')


def speech_recognition_base():
    global model
    result = model.transcribe("./audio/youtube_audio.mp3", fp16=False)
    text = ''
    for segment in result['segments']:
        text += f"[{round(segment['start'], 2)}:{round(segment['end'], 2)}] {segment['text']}"
    return spell(text)

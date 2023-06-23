import whisper

model = whisper.load_model("base")


def speech_recognition_base():
    global model
    result = model.transcribe("./audio/youtube_audio.mp3", fp16=False)
    return result["text"]

FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /web_app

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev \
    git \
    ffmpeg

# Устанавливаем Whisper и youtube-dl
RUN pip3 install "git+https://github.com/openai/whisper.git" \
    && pip3 install "git+https://github.com/ytdl-org/youtube-dl.git"

COPY requirements.txt /web_app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /web_app

EXPOSE 8000

FROM python:3.10-slim

WORKDIR /web_app

EXPOSE 8000

RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev
RUN apt-get update && apt-get install git -y
RUN pip3 install "git+https://github.com/openai/whisper.git"
RUN pip3 install "git+https://github.com/ytdl-org/youtube-dl.git"
RUN apt-get update && apt-get install ffmpeg -y

COPY requirements.txt /temp/requirements.txt

RUN pip3 install -r /temp/requirements.txt

COPY ./web_app .
import os


def deleting_nested_files(file_path: str) -> None:
    file_list = os.listdir(file_path)
    for file_name in file_list:
        file_nested_path = os.path.join(file_path, file_name)
        if os.path.isfile(file_nested_path):
            os.remove(file_nested_path)


def delete_temporary_files():
    audio_file_path = './audio/youtube_audio.mp3'
    video_file_path = './video/youtube_video.mp4'
    picture_int_article_directory = './article_generator/static/article_generator/picture'
    picture_directory = './pictures_youtube'
    if os.path.isfile(audio_file_path):
        os.remove(audio_file_path)

    if os.path.isfile(video_file_path):
        os.remove(video_file_path)

    deleting_nested_files(picture_int_article_directory)
    deleting_nested_files(picture_directory)

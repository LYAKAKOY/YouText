from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
from config.settings import YOUTUBE_API_KEY


def get_video_id(url: str):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    v_param = query_params.get("v")
    if v_param:
        v_value = v_param[0]
        return v_value


def get_info_about_video(video_url: str):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    video_id = get_video_id(video_url)
    response = youtube.videos().list(part='snippet', id=video_id).execute()
    return response

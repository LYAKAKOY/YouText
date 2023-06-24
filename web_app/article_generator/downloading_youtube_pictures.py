import asyncio
import numpy as np
from asyncio import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor
from moviepy.editor import VideoFileClip
from PIL import Image
import imagehash


def chunks_of_number(number):
    step = number // 5
    result = [step * i for i in range(5)]
    result.append(number)
    return result


def compute_frame_difference(frame1, frame2):
    diff = np.abs(frame1 - frame2)
    diff_mean = np.mean(diff)
    return diff_mean


def extract_still_frame(video_path, interval_seconds, start_video, end_video):
    clip = VideoFileClip(video_path)
    fps = clip.fps
    frame_interval = int(fps * interval_seconds)
    saved_frames = set()
    for frame_num in range(start_video, end_video, frame_interval):
        frame = clip.get_frame(frame_num / fps)
        if all(compute_frame_difference(frame, clip.get_frame(t / fps)) <= 30.0 for t in
               range(frame_num, frame_num + frame_interval)):
            frame_hash = imagehash.average_hash(Image.fromarray(np.uint8(frame)))
            if frame_hash not in saved_frames:
                saved_frames.add(frame_hash)
                image = Image.fromarray(np.uint8(frame))
                image = image.convert("RGB")  # Конвертируем в правильное цветовое пространство
                image.save(f'./pictures_youtube/picture_time{int(frame_num / fps)}.jpg', format='JPEG')

    clip.close()


def download_picture_from_video(video_path: str, interval_seconds: int):
    clip = VideoFileClip(video_path)
    fps = clip.fps
    duration = clip.duration
    len_video = int(duration * fps)
    extract_still_frame(video_path, interval_seconds, 0, len_video)

# async def download_picture_from_video(video_path: str, interval_seconds: int):
#     clip = VideoFileClip(video_path)
#     fps = clip.fps
#     duration = clip.duration
#     len_video = int(duration * fps)
#     with ThreadPoolExecutor() as thread_pool:
#         chunks = chunks_of_number(len_video)
#         tasks = []
#         loop: AbstractEventLoop = asyncio.get_running_loop()
#         for i, item in enumerate(chunks[:len(chunks) - 1], start=0):
#             tasks.append(loop.run_in_executor(thread_pool, extract_still_frame, video_path, interval_seconds, item,
#                                               chunks[i + 1]))
#
#         await asyncio.gather(*tasks)

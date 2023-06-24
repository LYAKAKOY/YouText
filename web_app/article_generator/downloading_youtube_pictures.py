import asyncio
import numpy as np
from asyncio import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from moviepy.editor import VideoFileClip
from PIL import Image


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
    for frame_num in range(start_video, end_video, frame_interval):
        frame = clip.get_frame(frame_num / fps)

        if all(compute_frame_difference(frame, clip.get_frame(t / fps)) <= 30.0 for t in
               range(frame_num, frame_num + frame_interval)):
            image = Image.fromarray(np.uint8(frame))
            image = image.convert("RGB")  # Конвертируем в правильное цветовое пространство
            image.save(f'./pictures_youtube/picture_time{round(frame_num / fps, 2)}.jpg', format='JPEG')

    clip.close()


async def download_picture_from_video(video_path: str, interval_seconds: int):
    clip = VideoFileClip(video_path)
    fps = clip.fps
    duration = clip.duration
    len_video = int(duration * fps)
    with ProcessPoolExecutor() as process_pool:
        chunks = chunks_of_number(len_video)
        tasks = []
        loop: AbstractEventLoop = asyncio.get_running_loop()
        for i, item in enumerate(chunks[:len(chunks) - 1], start=0):
            tasks.append(loop.run_in_executor(process_pool, extract_still_frame, video_path, interval_seconds, item,
                                              chunks[i + 1]))

        await asyncio.gather(*tasks)

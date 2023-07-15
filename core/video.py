import cv2
import os
from moviepy.editor import VideoFileClip, AudioFileClip

input_folder = './img4video'
output_path = './video/video.mp4'
audio_path = "./audio/audio.mp3"
result_path = "./result/result.mp4"
fps = 30


def img2video():
    # 获取文件夹中的所有图片路径
    image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.png') or f.endswith('.png')]
    image_files.sort()

    # 读取第一张图片，获取宽度和高度信息
    first_image = cv2.imread(image_files[0])
    height, width, _ = first_image.shape

    # 创建输出视频写入对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # 遍历图片并写入视频
    for image_file in image_files:
        image = cv2.imread(image_file)

        # 写入当前图片持续2秒的帧
        for _ in range(2*fps):
            output_video.write(image)

        # 添加过渡效果
        transition_duration_frames = int(fps * 0.5)  # 过渡效果持续帧数为0.5秒
        if image_file != image_files[-1]:
            next_image_file = image_files[image_files.index(image_file) + 1]
            next_image = cv2.imread(next_image_file)

            for i in range(transition_duration_frames):
                alpha = i / transition_duration_frames  # 过渡效果的权重
                blended = cv2.addWeighted(image, 1 - alpha, next_image, alpha, 0)
                output_video.write(blended)

    # 释放资源并关闭文件
    output_video.release()

def merge():
    video = VideoFileClip(output_path)
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)
    video.write_videofile(result_path, codec="libx264", audio_codec="aac")
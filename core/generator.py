import subprocess
from mutagen.mp3 import MP3
# from pydub import AudioSegment
from video import img2video, merge
import math
import shutil
import os
import random

img_repo = "e:/imgrepo"

target_img_path = "./img4video"


input_file = "./txt/SSML.xml"

out_file = "./audio/audio"

tts_path = "H:\\mc_sound\\tts\\python_cli_demo\\tts.py"

audio_path = "./audio/audio.mp3"

# 文字转音频
def translate_audio():
    command = ["python", tts_path , "--input", input_file, "--output", out_file]
    subprocess.call(command)

# 获取音频长度
def get_audio_sec():
    audio = MP3(audio_path)
    duration = audio.info.length
    # 将时长转换为整数秒数
    duration_seconds = int(duration)
    return duration_seconds

def copy_files(num_files):
    files = os.listdir(img_repo)
    random_files = random.sample(files, num_files)  # 随机选择指定数量的文件
    for file_name in random_files:
        source_file = os.path.join(img_repo, file_name)
        destination_file = os.path.join(target_img_path, file_name)
        shutil.copy2(source_file, destination_file)

def clear():
    file_list = os.listdir(target_img_path)
    for file_name in file_list:
        file_path = os.path.join(target_img_path, file_name)
        # 删除文件
        os.remove(file_path)

def main():
    translate_audio()
    sec = get_audio_sec()
    count = math.ceil(sec / 2.7)
    copy_files(count)
    img2video()
    merge()
    clear()





if __name__ == "__main__":
    main()




import os
import subprocess

# 设置你的文件夹路径
folder_path = ".\MQTT"

# 遍历文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        local_path = os.path.join(root, file)
        # 使用 mpremote 上传文件
        subprocess.run(["mpremote", "connect", "COM7", "fs", "cp", local_path, ":/{}".format(file)])

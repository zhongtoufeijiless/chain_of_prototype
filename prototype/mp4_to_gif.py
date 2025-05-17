import imageio
import os

# 输入输出文件名
mp4_path = 'demo-record.mp4'
gif_path = 'demo-record.gif'

# 读取视频帧
reader = imageio.get_reader(mp4_path)
# 获取视频帧率
fps = reader.get_meta_data()['fps']

frames = []
max_frames = fps * 15  # 最多15秒，防止gif过大
for i, frame in enumerate(reader):
    if i >= max_frames:
        break
    frames.append(frame)
reader.close()

# 保存为gif
imageio.mimsave(gif_path, frames, fps=10)
print(f'已生成GIF: {gif_path}') 
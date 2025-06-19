from moviepy import ImageClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np


# 入力画像パス
image_path = "your_image.png"  # アップロードした画像のファイル名
base_image = Image.open(image_path)
image_np = np.array(base_image)
video_width, video_height = base_image.size

# 動画設定
clip_duration = 3

# 背景動画
base_clip = ImageClip(image_np).with_duration(clip_duration)

## 羊の切り出し（座標調整必要）
# sheep_crop = base_image.crop((260, 180, 510, 360))
# sheep_clip = ImageClip(np.array(sheep_crop)).with_duration(clip_duration).resized(height=120)

# 羊のアニメーション
sheep_clip = ImageClip("sheep.png").with_duration(clip_duration).resized(height=880)

def sheep_pos(t):
    x = video_width - t * (video_width + 200) / clip_duration
    y = (video_height - sheep_clip.h) / 2 - 60 + 30 * np.sin(np.pi * t)
    return (x, y)

sheep_anim = sheep_clip.with_position(sheep_pos)

# 各クリップのサイズをプリント
print("Base clip size:", base_clip.size)
print("Sheep clip size:", sheep_anim.size)

# 合成
final_clip = CompositeVideoClip([base_clip, sheep_anim]).with_duration(clip_duration)
final_clip.write_videofile("sheep_animation.mp4", fps=24)

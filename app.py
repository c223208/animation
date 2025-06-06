from moviepy.editor import *
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
base_clip = ImageClip(image_np).set_duration(clip_duration)

# 羊の切り出し（座標調整必要）
sheep_crop = base_image.crop((280, 150, 490, 300))
sheep_clip = ImageClip(np.array(sheep_crop)).set_duration(clip_duration).resize(height=120)

def sheep_pos(t):
    x = video_width - t * (video_width + 200) / clip_duration
    y = video_height / 2 - 50 + 30 * np.sin(np.pi * t)
    return (x, y)

sheep_anim = sheep_clip.set_position(sheep_pos)

# テキストアニメーション（こまどりフォントはDL必要）
text = "ふたり反省会"
font_path = "KOMADORI.otf"  # フォントファイルのパス
font_size = 50
txt_img = Image.new("RGBA", (400, 80), (0, 0, 0, 0))
draw = ImageDraw.Draw(txt_img)
font = ImageFont.truetype(font_path, font_size)
draw.text((0, 0), text, font=font, fill="white")
txt_np = np.array(txt_img)
txt_clip = ImageClip(txt_np, transparent=True).set_duration(clip_duration)

def wave_position(t):
    x = video_width - t * (video_width + 200) / clip_duration
    y = video_height - 80 + 10 * np.sin(2 * np.pi * t)
    return (x, y)

txt_anim = txt_clip.set_position(wave_position)

# 合成
final_clip = CompositeVideoClip([base_clip, sheep_anim, txt_anim]).set_duration(clip_duration)
final_clip.write_videofile("sheep_animation.mp4", fps=24)

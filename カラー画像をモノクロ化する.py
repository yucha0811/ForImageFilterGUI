from helperlib import *
import cv2, numpy as np


"""
与えられた NumPy 配列 img を、カラー／モノクロ／バイナリの区別なくグレースケール画像に変換する関数

Parameters:
  img (np.ndarray): 入力画像。shape が (H, W, 3) ならカラー、(H, W) ならグレースケールまたはバイナリと想定

Returns:
  np.ndarray: グレースケール画像
"""

img = load_stdin_arr().astype(np.uint8)


# もし画像が 3 次元であれば、複数チャネル画像と判断
if img.ndim == 3:
    channels = img.shape[2]
    if channels == 3:
        # カラー画像 (BGR) をグレースケールに変換
        filtered_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif channels == 4:
        # 4チャネル画像 (BGRA) の場合
        filtered_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    else:
        raise ValueError(f"未対応のチャネル数 {channels} です。")
# もし画像が 2 次元であれば、既にモノクロまたはバイナリ画像と判断
elif img.ndim == 2:
    # もし画像データがバイナリ (0 と 1 のみ) であるなら 0～255 にスケールアップ
    unique_vals = np.unique(img)
    if set(unique_vals.tolist()).issubset({0, 1}):
        filtered_img = (img * 255).astype(np.uint8)
    else:
        filtered_img = img
else:
    raise ValueError("画像の次元が不正です。")

dump_img(filtered_img)
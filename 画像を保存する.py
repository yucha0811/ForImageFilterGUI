from helperlib import *
import cv2
import numpy as np

def convert_to_uint8(img):
    # 画像の最小値・最大値を確認して正規化
    # 最小値・最大値の取得
    min_val, max_val = np.min(img), np.max(img)

    # min と max が同じ場合（定数画像など）は、単にゼロ配列に変換
    if min_val == max_val:
        normalized = np.zeros_like(img, dtype=np.uint8)
    else:
        # 0～255 に正規化
        normalized = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    return normalized

arr = load_stdin_arr()
arr_8bit = convert_to_uint8(arr)
cv2.imwrite('filtered_arr.bmp', arr_8bit)

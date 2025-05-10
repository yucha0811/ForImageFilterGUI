# 平均化フィルタ
# 第2引数でカーネルの一辺の大きさを指定できる
# 第2引数を指定しない場合3x3pixのカーネルを適用する
from helperlib import *
from cv2 import blur
from sys import argv
import sys
arr = load_stdin_arr()

# 引数にフィルタサイズを指定された場合の
if len(argv) > 0:
    ksize = (int(argv[1]),int(argv[1]))
else:
    ksize = (3,3)

filtered_arr = blur(arr, ksize=ksize)
dump_img(filtered_arr)


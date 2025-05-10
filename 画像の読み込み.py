# ファイル名を受け取って画像を読み込みarrを標準出力でjson形式で返す
from helperlib import *
import sys
from matplotlib.pyplot import imread

if len(sys.argv)>1:
    arr = imread(sys.argv[1])
else:
    chosen_file = select_file()
    arr = imread(chosen_file)
print(dumps(arr.tolist()))
from json import dumps, loads
import sys
import numpy as np
import tkinter as tk
from tkinter import filedialog
def load_arg(num):
    return sys.argv[num]





def select_file():
    # Tkのルートウィンドウを作成
    root = tk.Tk()
    # メインウィンドウを非表示にする
    root.withdraw()

    # ファイル選択ダイアログを表示する
    file_path = filedialog.askopenfilename(
        title="ファイルを選択してください",
        filetypes=[("すべてのファイル", "*.*"), ("テキストファイル", "*.txt")]
    )
    return file_path


def dump_img(arr):
    print(dumps(arr.tolist()))
    return None

def load_stdin_arr():
    input_str = sys.stdin.read().strip()
    arr_list = loads(input_str)
    arr = np.array(arr_list)
    return arr
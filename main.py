import sys
import subprocess

def run_piped_scripts(_script_args, python_dir):
    """
    指定された Python スクリプトを順番に実行し、標準出力を次のスクリプトの標準入力に渡す。
    各スクリプトには個別の引数を渡すことが可能。

    Parameters:
      :param _script_args:
      :param python_dir:
    """
    if not _script_args:
        print("エラー: 実行するスクリプトが指定されていません。")
        sys.exit(1)

    # 最初のスクリプトを起動
    first_script, *first_args = _script_args[0]
    prev_process = subprocess.Popen([python_dir, first_script] + first_args, stdout=subprocess.PIPE)

    # 2つ目以降のスクリプトを順にパイプ接続して実行
    for script_info in _script_args[1:]:
        script, *args = script_info
        curr_process = subprocess.Popen([python_dir, script] + args, stdin=prev_process.stdout, stdout=subprocess.PIPE)
        prev_process.stdout.close()  # 出力を閉じて次に渡す
        prev_process = curr_process

    # 最後のスクリプトの出力を取得して表示
    output, _ = prev_process.communicate()
    print(output.decode("utf-8"))


if len(sys.argv) < 2:
    print("エラー: 実行するスクリプトと引数を指定してください。")
    sys.exit(1)

# スクリプトとそれぞれの引数を分離

raw_args = sys.argv[1:]  # 例: ["1.py", "arg1", "arg2", "2.py", "argA", "3.py"]
script_args = []
temp = []

for arg in raw_args:
    if arg.endswith(".py"):  # 新しいスクリプトが見つかったら現在のリストを保存
        if temp:
            script_args.append(temp)
        temp = [arg]
    else:
        temp.append(arg)

if temp:
    script_args.append(temp)

# 実行
run_piped_scripts(script_args, sys.executable)

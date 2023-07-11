import subprocess
import time

# rsyncのコマンドとパラメーター
source_dir = "{testdir}"
destination_dir = "{path}"
rsync_command = ["rsync", "-avP", source_dir, destination_dir]

# 現在の時刻を取得
start_time = time.time()

# rsyncコマンドのプロセスを開始
rsync_process = subprocess.Popen(rsync_command)

# n秒間の待機時間
wait_time = 20

# 中断フラグ
interrupted = False

# n秒間の待機時間を経過するか、rsyncコマンドが終了するまでループ
while True:
    # rsyncコマンドの状態を確認
    returncode = rsync_process.poll()
    if returncode is not None:
        # rsyncコマンドが終了した場合、ループを抜ける
        break

    # 経過時間を計算
    elapsed_time = time.time() - start_time

    # n秒経過した場合、rsyncコマンドを中断
    if elapsed_time >= wait_time:
        rsync_process.terminate()
        print("ファイル転送を中断しました（経過時間: {:.2f}秒）".format(elapsed_time))
        interrupted = True
        break

    # 0.1秒待機してループを続ける
    time.sleep(0.1)

# 中断後に再開する場合
if interrupted:
    print("ファイル転送を再開します...")
    # 中断時のコマンドとパラメーターを修正
    rsync_command[2] = source_dir
    rsync_process = subprocess.Popen(rsync_command)

    # 再開後の経過時間を計算
    resume_start_time = time.time()
    resume_elapsed_time = resume_start_time - start_time

    # 中断前の待機時間を考慮して、再開後に残りの待機時間を計算
    remaining_wait_time = wait_time - resume_elapsed_time

    # 残りの待機時間を経過するか、rsyncコマンドが終了するまでループ
    while True:
        # rsyncコマンドの状態を確認
        returncode = rsync_process.poll()
        if returncode is not None:
            # rsyncコマンドが終了した場合、ループを抜ける
            break

        # 経過時間を計算
        elapsed_time = time.time() - resume_start_time

        # 残りの待機時間を経過した場合、rsyncコマンドを中断
        if elapsed_time >= remaining_wait_time:
            rsync_process.terminate()
            print("ファイル転送を中断しました（経過時間: {:.2f}秒）".format(elapsed_time))
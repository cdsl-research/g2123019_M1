#!/bin/bash

# rsyncのコマンドとパラメーター
source_dir="[directory]"
destination_dir="[user]@[address]"
rsync_command=("rsync" "-avhP" "$source_dir" "$destination_dir")

# バックアップ期限までの秒数を入力
echo "バックアップ期限までの秒数を入力"
read backuplimit

# 繰り返し間隔（秒）
interval=20

# 無限ループで処理を続ける
while true; do
    # 現在の時刻を取得
    loop_start_time=$(date +%s)

    # rsyncコマンドの実行
    "${rsync_command[@]}" &

    # rsyncコマンドのプロセスIDを取得
    rsync_pid=$!

    # 指定した間隔待つ
    sleep $interval

    # rsyncコマンドを中断
    kill -TERM $rsync_pid
    echo "ファイル転送を中断しました"

    # rsyncコマンドが中断されるのを待つ
    wait $rsync_pid

    # rsyncコマンドが終了した後に残り時間とファイルサイズを表示
    loop_end_time=$(date +%s)
    rsync_elapsed_time=$((loop_end_time - loop_start_time))
    transfer_size=$(python3 filesize.py) # filesize.pyを実行して転送済みファイルサイズを取得

    limit=$(($backuplimit - $rsync_elapsed_time))
    leftsize=$(echo "$totalsize - $transfer_size" | bc)

    echo "転送が開始してから $rsync_elapsed_time 秒経過しました。"
    echo "バックアップ期限まであと $limit 秒"
    echo "残りファイルサイズ: $leftsize MB"

    # 次のループの前に残りの時間待機
    remaining_time=$((interval - rsync_elapsed_time))
    sleep $remaining_time
done

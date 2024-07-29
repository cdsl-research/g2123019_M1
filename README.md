# Garrulus 2
Ubnutu上で動作する.sh及び.pyファイル．

本ソフトウェアの使用を想定する状況として，ファイルサーバがファイルをバックアップ中にユーザからファイルが転送された場合，ユーザのファイル転送時間を増加させないために用いる．

## reculc.py
バックアップ速度を制限することでユーザにディスク帯域を渡し，ユーザのファイル転送時間の増加を防ぐ．

制限は，バックアップ期限を超えないように設定される．

ファイル内の[dirname]，[user]，[address]には，環境に合わせてそれぞれ任意のディレクトリ名，ユーザ名，IPアドレスを入力する必要がある．

実行すると，バックアップ期限までの時間を入力するよう求められる．
![image](https://github.com/user-attachments/assets/48d3c9fb-1c80-4319-bf3b-ee96b921c074)

interval=
の部分で設定した秒数ごとにファイル転送を中断し，バックアップの制限速度を変更する．
![image](https://github.com/user-attachments/assets/604367c1-35d1-47e7-ab8e-351b06dea6e9)

## filesize.py
転送中のファイルの残りファイルサイズを計算する．

バックアップ速度の制限に用いるため，reculc.pyにおいて実行される．

ファイル内の[path]には，環境に合わせて任意のファイルパスを入力する必要がある．

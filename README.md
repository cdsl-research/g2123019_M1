# Garrulus 2
Ubnutu上で動作する.sh及び.pyファイル．

本ソフトウェアの使用を想定する状況として，ファイルサーバがファイルをバックアップ中にユーザからファイルが転送された場合，ユーザのファイル転送時間を増加させないために用いる．

## reculc.py
バックアップ速度を制限することでユーザにディスク帯域を渡し，ユーザのファイル転送時間の増加を防ぐ．

制限は，バックアップ期限を超えないように設定される．

ファイル内の[dirname]，[user]，[address]には，環境に合わせて任意の文字列を入力する必要がある．

## filesize.py
転送中のファイルの残りファイルサイズを計算する．

バックアップ速度の制限に用いるため，reculc.pyにおいて実行される．

ファイル内の[path]には，環境に合わせて任意のファイルパスを入力する必要がある．

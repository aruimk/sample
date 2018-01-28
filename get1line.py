"""
指定したフォルダ内の*.c, *.hの1行目を抜き出して出力
"""

import os
import datetime

# 書き込みファイルの準備
date = datetime.date.today()  # date = 2018-01-28の形
writefile = 'output_topline.txt'
fw = open(writefile, 'w')
fw.write(str(date) + '\n')
fw.close()
fw = open(writefile, 'a')

# みたいパスの指定
PATH = '/Users/workspace/prog/*＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊'

# 変数定義
FileOrDirName = os.listdir(PATH)    # パスにあるファイル名やdir名の取得
print(FileOrDirName)
tmplist = list()                    # 指定されたパスの全部を格納する用
dirist = list()                     # *.hか*.cのみ格納

for i in FileOrDirName:
    tmplist.append(i)

for i in tmplist:
    filepath = PATH + '/' + i
    name, ext = os.path.splitext(filepath)
    if ext == '.c' or ext == '.h' or ext == '.txt':
        dirist.append(i)

for i in dirist:
    f = open(PATH + '/' + i, 'r')
    topline = f.readline()
    fw.write(topline + '\n')
    f.close()

fw.close()








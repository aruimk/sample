"""
指定したパスにあるファイルのファイル名を取得するプログラム
"""

import os

fw = open('/Users/*******/outputfile.txt','w')
PATH = '/Users/*********************' # ファイルネームを取得したいパス


list_filename = os.listdir(PATH)
#print(list_filename)

for i in range(len(list_filename)):
    print(PATH + '/' + list_filename[i])

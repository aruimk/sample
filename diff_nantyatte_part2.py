"""
比較元ファイルに書かれている名前が比較先ファイルに書かれているか検索
現在は6行目、7行目で指定しているファイルを比べている。
"""

# 比較するファイルやoutputファイルの設定
readfile_a = './diff_sample/hikakumoto.txt'
readfile_b = './diff_sample/hikakusaki.txt'
output = 'output_diff.txt'

# 各ファイルの行数を取得
num_line_a = sum(1 for line in open(readfile_a, 'r'))
num_line_b = sum(1 for line in open(readfile_b, 'r'))

# ファイルのopen
fr_a = open(readfile_a, 'r')
fr_b = open(readfile_b, 'r')
fw = open(output, 'w')

# 変数の定義
lst_data_a = list()
lst_data_b = list()
set_a = set()
set_b = set()

#検索元記載の比較要素が重複している可能性を考慮して一度集合にする
for line in fr_a:
	str_line = line.replace('\n','').replace('\r','').replace(' ','')
	lst_data_a.append(str_line)
set_a = sorted(set(lst_data_a), key = lst_data_a.index)    # 順番を保持したまま集合化する。

# 比較先のファイルについても同様にする。
for line in fr_b:
	str_line = line.replace('\n','').replace('\r','').replace(' ','')
	lst_data_b.append(str_line)
set_b = sorted(set(lst_data_b), key = lst_data_b.index)    # 順番を保持したまま集合化する。

lst_data_a = list(set_a)
lst_data_b = list(set_b)


#####################
#  以下検索処理
#####################
print(readfile_a + '  側にあるが ' + readfile_b + ' 側に無いものを検索する')
fw.write(readfile_a + '  側にあるが ' + readfile_b + ' 側に無いものを検索する\n' )

# まず左側のファイルを基準に要素の有無を検索
for i in range(len(lst_data_a)):
	rst_flg = 0
	for j in range(len(lst_data_b)):		
		if str(lst_data_a[i]) == str(lst_data_b[j]):
			rst_flg = 1

	if rst_flg == 0:
		print(str(lst_data_a[i]) + ' は無い')
		fw.write(str(lst_data_a[i]) + ' は無い \n')

print(readfile_b + '  側にあるが ' + readfile_a + ' 側に無いものを検索する')
fw.write(readfile_b + '  側にあるが ' + readfile_a + ' 側に無いものを検索する\n' )

# 次に右側のファイルを基準に要素の有無を検索
for j in range(len(lst_data_b)):
	rst_flg = 0
	for i in range(len(lst_data_a)):
		if str(lst_data_b[j]) == str(lst_data_a[i]):
			rst_flg = 1
			break
	if rst_flg == 0:
		print(str(lst_data_b[j]) + ' は無い')
		fw.write(str(lst_data_b[j]) + ' は無い \n')
fr_a.close()
fr_b.close()
fw.close()
		



















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
set_diff = set()
lst_output = list()

#検索元記載の比較要素が重複している可能性を考慮して一度集合にする
for line in range(num_line_a):
	str_line = fr_a.readline()
	str_line = str_line.replace('\n','').replace('\r','')
	#print(str(line) + '行目　' + str_line)
	set_diff.add(str_line)

# 一度集合にした重複していない要素を取り出したい
lst_output = list(set_diff)

str_all = fr_b.read()

#for i in range(len(lst_output)):
for i in lst_output:
	# True or False
	rst = str(i) in str_all
	if rst == False:
		print(str(i) + 'は無い')
		fw.write(str(i) + 'は無い' + '\n')
	if rst == True:
		print(str(i) + 'は有る')
		fw.write(str(i) + 'は有る' + '\n')
fr_a.close()
fr_b.close()
fw.close()		

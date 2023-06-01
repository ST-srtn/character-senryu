import numpy as np
import random

#予めキャラクター名一覧.txtにキャラクター名を用意しておく（ここは手作業）
#ファイルオープン
f = open('キャラクター名一覧.txt', 'r', encoding="utf-8")
#listにキャラ名一覧を格納
list = f.readlines()
f.close()

k5 = 0 
k7 = 0

#テキストファイルに書き込み
f5 = open('5文字名前.txt', 'w', encoding="utf-8")
f7 = open('7文字名前.txt', 'w', encoding="utf-8")
for i in  list :
    if len(i.rstrip('\n')) == 5 :
        k5 += 1
        f5.write(i)
    if len(i.rstrip('\n')) == 7 :
        k7 += 1
        f7.write(i)
f5.close()
f7.close()
#再び5文字の名前を読み込み、list5に格納
f5 = open('5文字名前.txt', 'r', encoding="utf-8")
list5 = f5.readlines()
f5.close()
#再び7文字の名前を読み込み、list7に格納
f7 = open('7文字名前.txt', 'r', encoding="utf-8")
list7 = f7.readlines()
f7.close()

#list5からランダムに名前を出力(1回目)
name5 = random.choice(list5).rstrip('\n')
print(name5)
#list7からランダムに名前を出力
print(random.choice(list7).rstrip('\n'))
#list5からランダムに名前を出力(1回目とは被らないようにする)
while True :
    name5_2 = random.choice(list5).rstrip('\n')
    if name5 != name5_2 :
        print(name5_2)
        break
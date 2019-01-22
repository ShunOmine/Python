import random

sayings = ['今頑張れない奴は一生頑張れない',
'学力＝勉強時間＋勉強の質', 
'努力の前に成功がくるのは辞書だけである',
'現状維持では成長してない',
'あきらめなければ道は開ける',
'やらないで後悔するな！やってから後悔しろ',
'夢は逃げない。逃げるのいつも自分']

#出力したリストを保持するリスト
str = []

for count in range(5):
    temp = random.choice(sayings)
    #出力済みの名言を重複して表示しないようにする
    while temp in str:
        temp = random.choice(sayings)
    #選択された名言をリストstrに追加
    str.append(temp)
    #出力
    print(temp)
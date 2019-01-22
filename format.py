top = '現在'
day = '10日'
am = '午前'
pm = '午後'
sentence = '{first}, {second}の{third}です'.format(first = top, second = day,
                                                third = am)
print(sentence)

cm = float(input('cmを入力して下さい'))
print('{:.3f}は{:.3f}インチです'.format(cm, cm/2.54))

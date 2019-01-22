import random

saying1 = '模試のA判定より合格通知'
saying2 = 'いつやるの？いまでしょ！'
saying3 = '体力の限界はあるが頭の限界はない'
saying4 = '夢は逃げない。逃げるのはいつも自分'

for count in range(5):
    x = random.randint(1, 10)
    if x <= 3:
        print(saying1)
    elif x >= 4 and x <= 5:
        print(saying2)
    elif x >= 6 and x <= 7:
        print(saying3)
    else:
        print(saying4)
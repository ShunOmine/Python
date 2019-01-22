import random

#主語
s = ['I', 'You', 'He', 'She', 'We', 'They']

#第１文型用の動詞
snt1_v = ['walk', 'run', 'work']

#第２文型用の動詞、補語
snt2_v = ['am', 'are', 'is', 'become', 'come']
snt2_c = ['a student', 'hungry', 'happy']

#第３文型用の動詞、目的語
snt3_v = ['play', 'love']
snt3_o = ['tennis', 'basketball', 'listening to music']

#第４文型用の動詞、間接目的語、直接目的語
snt4_v = ['give', 'buy', 'make']
snt4_io = ['me', 'us','him', 'her', 'them', 'Rei', 'Terasu', 'my sister']
snt4_do = ['a watch', 'a ring', 'character figure']

#第５文型用の動詞、目的語、補語
snt5_v = ['think', 'find', 'consider', 'make']
snt5_o = ['me', 'us', 'him', 'her', 'them', 'Rei', 'Terasu', 'my sister']
snt5_c = ['happy', 'angry', 'good singer', 'good character']

def first_pattern():
    choice_s = random.choice(s)
    choice_v = random.choice(snt1_v)
    if choice_s == 'He' or choice_s == 'She':
        choice_v = choice_v + 's'
    print('第１文型---> {0} {1}.'.format(choice_s, choice_v))
def second_pattern():
    choice_s = random.choice(s)
    choice_v = ''
    choice_c = random.choice(snt2_c)
    if choice_s == 'I':
        choice_v = snt2_v[0]
    elif choice_s == 'You' or choice_s == 'We' or choice_s == 'They':
        choice_v = snt2_v[1]
    elif choice_s == 'He' or choice_s == 'She':
        tmp_v = snt2_v[2:]
        choice_v = random.choice(tmp_v)
        if choice_v != 'is':
            choice_v = choice_v + 's'
    print('第２文型---> {0} {1} {2}.'.format(choice_s, choice_v, choice_c))
def third_pattern():
    choice_s = random.choice(s)
    choice_v = random.choice(snt3_v)
    choice_o = random.choice(snt3_o)
    if choice_s == 'He' or choice_s == 'She':
        choice_v = choice_v + 's'
    print('第３文型---> {0} {1} {2}.'.format(choice_s, choice_v, choice_o))
def fourth_pattern():
    choice_s = random.choice(s)
    choice_v = random.choice(snt4_v)
    choice_io = random.choice(snt4_io)
    choice_do = random.choice(snt4_do)
    if choice_s == 'He' or choice_s == 'She':
        choice_v = choice_v + 's'
    if choice_s == 'I':
        if choice_io == 'me' or choice_io == 'us':
            tmp_1 = snt4_io[2:]
            choice_io = random.choice(tmp_1)
    print('第４文型---> {0} {1} {2} {3}.'.format(choice_s, choice_v, choice_io, choice_do))
def fifth_pattern():
    choice_s = random.choice(s)
    choice_v = random.choice(snt5_v)
    choice_o = random.choice(snt5_o)
    choice_c = random.choice(snt5_c)
    if choice_s == 'He' or choice_s == 'She':
        choice_v = choice_v + 's'
    print('第５文型---> {0} {1} {2} {3}.'.format(choice_s, choice_v, choice_o, choice_c))
        
print('基本５文型を使って英作文するね！')
print('1 = 第１文型')
print('2 = 第２文型')
print('3 = 第３文型')
print('4 = 第４文型')
print('5 = 第５文型')
while True:
    pattern = input('どの文型にする？ 数字を入力してね！')
    if pattern == 'OK':
        print('またねー')
        break
    elif pattern == '1':
        first_pattern()
    elif pattern == '2':
        second_pattern()
    elif pattern == '3':
        third_pattern()
    elif pattern == '4':
        fourth_pattern()
    elif pattern == '5':
        fifth_pattern()
    else:
        print('なにそれ？')
            
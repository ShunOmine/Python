import time

words = {
    'crucial' : '極めて重要な',
    'cubsequent' : 'その後の',
    'devise' : '考案する',
    'strain' : '負担、重圧',
    'distinct' : '明確な、独特な',
    'incorporate' : '取り入れる',
    'eliminate' : 'なくす、排除する',
    'privilege' : '特権、特典',
    'retain' : '記憶する、維持する',
    'seize' : 'つかむ、つかみ取る',
    'perceive' : '知覚する',
    'variation' : '変化、変動',
    'persuade' : '説得する、促す',
    'prominent' : '著名な、顕著な',
    'integrate' : '一体化する、組み入れる',
    'anticipate' : '予想する、予期する',
    'disturb' : '邪魔する、不安にさせる',
    'respectively' : 'それぞれ、おのおの',
    'perspective' : '展望、観点',
    'magnificent' : '壮麗な、壮大な'
}
print('単語の意味を答えるね')
while True:
    word = input('>>>')
    if word == 'OK':
        print('バイバーイ')
        break
    elif word in words:
        print('「' + words[word] + '」って意味だよ')
    else:
        print('わかんないよー')
        meaning = input('意味を教えて>')
        while not meaning:
            meaning = input('意味を教えて>')
        words[word] = meaning
        print('記憶中......')
        time.sleep(3)
        
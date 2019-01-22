import time
while True:
    time.sleep(1)
    present = input('動詞を入力してね>')
    if (present == 'OK'):
        print('またねー')
        break
    
    # 例外的に扱う動詞
    prog = ''
    if present == 'visit' or\
       present == 'limit' or\
       present == 'play' or\
       present == 'enjoy' or\
       present == 'listen' or\
       present == 'see' or\
       present == 'dye' or\
       present == 'enter':
        prog = present + 'ing'
    # ieで終わる語はieを取ってyingにする 
    elif present[-2] == 'ie':
        prog = present.replace(present[-2:], 'ying')

    # eで終わる語はeを取ってingを付ける
    elif present[-1] == 'e':
        prog = present.replace(present[-1], 'ing')

    # c で終わる語はkingを付ける
    elif present[-1] == 'c':
        prog = present + 'king'

    # 「長母音＋子音」は原形にingを付ける　先に書かないといけない
    elif (present[-3] == 'a' or \
          present[-3] == 'i' or \
          present[-3] == 'u' or \
          present[-3] == 'e' or \
          present[-3] == 'o') and\
         (present[-2] == 'a' or \
          present[-2] == 'i' or \
          present[-2] == 'u' or \
          present[-2] == 'e' or \
          present[-2] == 'o'):
        prog = present + 'ing'

    #「短母音＋子音」は子音字を重ねてingを付ける
    elif present[-2] == 'a' or \
         present[-2] == 'i' or \
         present[-2] == 'u' or \
         present[-2] == 'e' or \
         present[-2] == 'o':
        prog = present + present[-1] + 'ing'

    #どれも一致しない
    else:
        prog = present + 'ing'
    print('現在分詞はこれ ->' + prog)

    past = ''
    #例外的に扱う動詞
    if present == 'visit' or\
       present == 'limit' or\
       present == 'play' or\
       present == 'enjoy' or\
       present == 'listen' or\
       present == 'enter':
        past = present + 'ed'
        
    #例外的に扱う動詞
    elif present == 'dye':
        past = present + 'd'
    
    #不規則動詞
    elif present == 'get':
        past = 'got-got'

    #不規則動詞
    elif present == 'run':
        past = 'ran-run'

    #不規則動詞
    elif present == 'swim':
        past = 'swam-swmut'

    #不規則動詞
    elif present == 'begin':
        past = 'began-begun'

    #不規則動詞
    elif present == 'read':
        past = 'read-read'

    elif present == 'eat':
        past = 'ate-eaten'

    elif present == 'take':
        past = 'took-taken'

    #eで終わる語はdを付ける
    elif present[-1] == 'e':
        past = present + 'd'

    #語尾がpで終わる動詞
    elif present[-1:] == 'p':
        # 語尾が「母音＋ｐ」で終わる場合はｐを加えてからedを付ける
        if present[-2] == 'a' or \
           present[-2] == 'i' or \
           present[-2] == 'u' or \
           present[-2] == 'e' or \
           present[-2] == 'o':
            past = present + 'ped'
        #それ以外はedのみを付ける
        else:
            past = present + 'ed'

    #語尾がyで終わる動詞
    elif present[-1:] == 'y':
        #語尾が「母音 + y」で終わる場合はedのみを付ける
        if present[-2] == 'a' or \
           present[-2] == 'i' or \
           present[-2] == 'u' or \
           present[-2] == 'e' or \
           present[-2] == 'o':
            past = present + 'ed'
        #それ以外はyをiに変えてedを付ける
        else:
            past = present.replace(present[-1], 'ied')

    #cで終わる動詞はkを加えてからedを付ける
    elif present[-1] == 'c':
        past = present + 'ked'

    #ir,er,urで終わる動詞は最後に子音を加えてからedを付ける
    elif present[-2:] == 'ir' or \
         present[-2:] == 'er' or \
         present[-2:] == 'ur':
        past = present + present[-1] + 'ed'

    #「長母音+子音」はedを付ける
    elif (present[-3] == 'a' or \
          present[-3] == 'i' or \
          present[-3] == 'u' or \
          present[-3] == 'e' or \
          present[-3] == 'o') and\
         (present[-2] == 'a' or \
          present[-2] == 'i' or \
          present[-2] == 'u' or \
          present[-2] == 'e' or \
          present[-2] == 'o'):
        past = present + 'ed'
          

    #「母音+ 子音」は子音字を重ねてedを付ける
    elif present[-2] == 'a' or \
         present[-2] == 'i' or \
         present[-2] == 'u' or \
         present[-2] == 'e' or \
         present[-2] == 'o':
        past = present + present[-1] + 'ed'

    #どれにも当てはまらない場合はedを付ける
    else:
        past = present + 'ed'
    print('過去形はこれ ->' + past)


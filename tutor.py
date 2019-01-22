class Tutor:
    count = 0
    max = 4
    @classmethod
    def teach(cls):
        if cls.count < cls.max:
            print('いつやるの？今でしょ！')
        else:
            print('よーし続きは明日だ！')
        cls.count += 1

#==================================
#プログラムの起点
#==================================
if __name__ == '__main__':
    
    for i in range(3):
        print('この単語も覚えなきゃダメ？')
        Tutor.teach()

    for i in range(2):
        print('もう覚えらんないよー')
        Tutor.teach()

    Tutor.count = 0

    for i in range(2):
        print('やっぱりもう一つ覚えるかな')
        Tutor.teach()

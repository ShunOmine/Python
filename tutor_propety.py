class Tutor:
    def __init__(self, max=5, count=0):
        self.__max = max
        self.__count = count

    #__maxのゲッター
    def get_max(self):
        return self.__max

    #__countのゲッター
    def get_count(self):
        return self.__count

    #__maxのセッター
    def set_max(self, max):
        self.__max = max
    #_countのセッター
    def set_count(self, count):
        self.__count = count

    #maxプロパティの定義
    max = property(get_max, set_max)
    #countプロパティの定義
    count = property(get_count, set_count)

    def teach(self):
        if self.count < self.max:
            print('いつやるの？今でしょ！')
        else:
            print('よーし続きは明日だ')
        self.count += 1

#=============================
#プログラムの起点
#=============================
if __name__ == '__main__':
    tu = Tutor()
    tu.max = 2
    for i in range(3):
        print('この単語も覚えなきゃダメ？')
        tu.teach()
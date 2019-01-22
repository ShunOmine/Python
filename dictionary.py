class Dictionary:
    def __init__(self):
        
        """辞書オブジェクトを作成"""
        self.__load_history = __load_history

    def __load_history(self):
        
        """ファイルを読み込み、世界史の辞書オブジェクトを作成"""
        with open('world_history.txt', 'r', encoding = 'utf_8') as file:
            lines = file.readlines()
        new_lines = []
        for line in lines:
            line = line.rstrip('\n')
            if(line != ''):
                new_lines.append(line)

        separate = []
        for line in new_lines:
            sp = line.split('\t')
            separate.append(sp)
        self.__history = dict(separate)

    def save(self):
        """self.historyの内容を加工してファイルに書き込む"""
        write_lines = []
        for key, val in self.history.items():
            write_lines.append(key + '\t' + val + '\n')
        with open('world_history.txt', 'w', encoding = 'utf_8') as f:
            f.writelines(write_lines)

    def get_history(self):
        return self.__history
    def set_history(self):
        self.__history = history()
    history = property(get_history, set_history)

#==============================================
#プログラムの実行ブロック
#==============================================
if __name__ == '__main__':

    dictionary = Dictionary()
    print(dictionary.history)
    dictionary.save()

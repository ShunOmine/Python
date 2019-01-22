class WordsDictionary:
    def __init__(self):
        self.__load_words = __load_words

    words = {}
    def __load_words(self):
        with open('English_words.txt', 'r', ebcoding='utf_8')as file:
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
        self.__words = dict(separate)

    def save(self):
        write_lines = []
        for key, val in self.words.items():
            write_lines.append(key + '\t' + val + '\n')
        write_lines.sort()
        with open('English_words.txt', 'w', encoding='utf_8')as f:
            f.writelines(write_lines)

    def get_words(self):
        return self.__words
    def set_wordst(self,words):
        self.__words = words

    words = property(get_words, set_wordst)

#==================================
#プログラムの起点
#==================================
if __name__ == '__main__':
    w_dictionary = WordsDictionary()
    print(w_dictionary.words)
    w_dictionary.save()
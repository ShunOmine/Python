from dictionary import *
from English_words_dictionary import *

class Responder:
    def __init__(self, dictionary):
        self.__dictionary = dictionary
        self.__dictionary_words = dictionary

    def response(self, input, what):
        return ''

    def get_dictionary(self):
        return self.__dictionary
    def set_dictionary(self, dictionary):
        self.__history = history()
    dictionary = property(get_dictionary, set_dictionary)
    
    def get_dictionary_words(self):
        return self.__dictionary_words
    def set_dictionary_words(self):
        self.__words = words()
    dictionary = property(get_dictionary_words, set_dictionary_words)

class HistoryResponder(Responder):
    def response(self, input, what):
        if input in self.dictionary.history:
            return '「' + self.dictionary.history[input] + '」だよ'
        else:
            return('わかんないよ～答えを教えて！')

class StudyHistoryResponder(Responder):
    def response(self, input, what):
        self.dictionary.history[what] = input
        return '学習したよ～'

class WordResponder(Responder):
    def response(self, input, what):
        if input in self.dictionary.words:
            return '「' + self.dictionary.words[input] + '」だよ'
        else:
            return('わかんないよ～答えを教えて！')

class StudyWordResponder(Responder):
    def response(self, input, what):
        self.dictionary.words[what] = input
        return '学習したよ～'

#========================================
#プログラムの実行ブロック
#========================================
if __name__ == '__main__':
    
    dictionary = Dictionary()
    history_resp = HistoryResponder()
    ans = history_resp.response('世界四大文明', '')
    print(ans)

    study_resp = StudyHistoryResponder(dictionary)
    ans = study_resp.response('ディアドコイ', 'アレクサンドロス大王の後継者')
    print(dictonary.history)

    dictionary = WordsDictionary()
    word_resp = WordResponder(dictionary)
    ans = word_resp.response('anticipate', '')
    print(ans)
    study_word = StudyWordResponder(dictionary)
    ans = study_word.response('variation', '変化、変動')
    print(dictionary.words)
from wordle import LetterVerdict

class WordleSolver:
    def __init__(self, word_list):
        self.word_list = word_list

    def filter_words(self, guess, verdict, words=None):
        if words is None:
            words = self.word_list
        filtered_words = []
        for word in words:
            if self.__matches_constraints(word, guess, verdict):
                filtered_words.append(word)
        return filtered_words

    def __matches_constraints(self, word, guess, verdict):
        for i, (letter, v) in enumerate(zip(guess, verdict)):
            if v == LetterVerdict.GREEN and word[i] != letter:
                return False
            if v == LetterVerdict.YELLOW and (word[i] == letter or letter not in word):
                return False
            if v == LetterVerdict.GRAY and letter in word:
                return False
        return True
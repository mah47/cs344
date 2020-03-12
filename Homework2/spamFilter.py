'''
Name: Marcos Hernandez (mah47)
CS 344
Homework 2
'''

class SpamFilter:

    def __init__(self, corpus1, corpus2, strings):
        self.spam_corpus = self.corpusWords(corpus1)
        self.spam2_corpus = self.corpusWords(corpus2)
        self.fusedCorpus = strings
        self.corpusLength = 0
        self.corpusAmount = self.corpusMix()
        self.corpusAlgo = {}

    def corpusWords(self, strings):
        corpus = []
        for words in strings:
            for corpWord in words:
                corpus.append(corpWord)
        return corpus

    def corpusMix(self):
        dictionary = {}
        for words in self.fusedCorpus:
            for corpWord in words:
                if corpWord not in dictionary.keys():
                    dictionary[corpWord] = 0
                self.corpusLength += 1
                dictionary[corpWord] += 1
        return dictionary

    def result(self):
        # print(self.corpusAmount)
        # print(self.spam_corpus)
        # print(self.fusedCorpus)
        # print(self.spam2_corpus)
        corps = 0
        for words in self.fusedCorpus:
            for corpWord in words:
                spam = 0
                filterCorps = 0
                if corpWord in self.spam2_corpus:
                    spam = 2 * self.corpusAmount[corpWord]
                if corpWord in self.spam_corpus:
                    filterCorps = self.corpusAmount[corpWord]

                if spam + filterCorps >= 1:
                    corpusCode = max(0.01, min(0.99, min(1.0, filterCorps / len(self.spam_corpus))
                                               / (min(1.0, spam / len(self.spam2_corpus)) +
                                                  min(1.0, filterCorps / len(self.spam_corpus)))))
                    corps += corpusCode
                    self.corpusAlgo[corpWord] = corpusCode
        return corps / self.corpusLength


if __name__ == '__main__':
    spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
    ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
    corpus_sample = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "green", "eggs", "and", "ham"]]
    filterCorpus = SpamFilter(spam_corpus, ham_corpus, corpus_sample)
    print("Spam Probability: ", filterCorpus.result())
    print("0 word probabilities: " + str(filterCorpus.corpusAlgo))

'''
It makes it Bayesian because it determines the probabilities of individual words and uses them
to determine the overall probability. If the program shows that the words spam then the email is spam because the
probability is conditional.
'''
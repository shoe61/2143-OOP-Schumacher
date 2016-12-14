"""
Given a list of words like so:
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]
Write a python snippet to find the words that occur most often. You output should look something like the following:
[('eyes', 8), ('the', 5), ('look', 4)]
"""

import operator

class WordCounter(object):

    def __init__(self, wordList):
        self.workList = sorted(wordList)
        self.wordLister()

    def wordLister(self):
        self.counted = {}
        for word in self.workList:
            if not word in self.counted:
                self.counted[word] = 0
            self.counted[word] += 1        
        self.summaryList = sorted(self.counted.items(), key = operator.itemgetter[1], reverse = True)

        print(self.summaryList)

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

rezo = WordCounter(words)


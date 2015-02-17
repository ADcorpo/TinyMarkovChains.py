#!/bin/env python3

"""This module contains an implementation of Markov Chains as a
class. It is used by instantiating a MarkovChain() object and calling
his train() method on a sentence represented by a string.

The talk() method generates a sentence and returns it as a string.
"""

from collections import defaultdict
# defaultdict is more appropriate than the standard dict for word
# counting.
from random import randint
# A random component is needed to avoid the creation of deterministic
# chains.

class MarkovChain(object):
    """Represents a Markov chain. It contains a word tree, populated by
    passing sentences to the train() method. The talk() method generates
    a sentence and returns it as a string.
    """

    def __init__(self):
        """MarkovChain constructor. Takes no argument, creates the attribute _word_tree,
        a dict() to store words using the following pattern:
        {word: {occurrence1: times_occured,
                occurrenceN: times_occured}}
        """

        self._word_tree = defaultdict(lambda: defaultdict(int))
        # Recursively declaring a defaultdict

    def _get_probable_word(self, word):
        """Internal method. Returns a probable word that could follow the word
        passed as a parameter (according the word tree). However, a
        pseudo-random component remains to ensure that the generated sentences are
        not always the same.
        """
        
        word_list = list(self._word_tree[word].keys())
        total_occurences = 0

        for word_ in word_list:
            total_occurences += self._word_tree[word][word_]

        index = randint(0, total_occurences)
        counter = 0
        for word_ in word_list:
            counter += self._word_tree[word][word_]
            if counter >= index:
                return word_
            
    def train(self, sentence):
        """Takes a sentence (string) and adds each word to the word_tree,
        following the pattern described in the constructor's
        docstring. NoneType is used as a key to represent the absence
        of words (For example, at the beginning/ending of the
        sentence).
        """
        
        words = sentence.split()

        self._word_tree[None][words[0]] += 1
        
        for i in range(0, len(words)):
            if i == len(words)-1:
                self._word_tree[words[i]][None] += 1
            else:
                self._word_tree[words[i]][words[i+1]] += 1
        # Using a defaultdict for counting occurences shows an interest
        # here: checking if the key exists before assigning a value is
        # not necessary.  The amount of code needed here is decreased.

    def talk(self):
        """Takes no parameter. Generates a sentence following the Markov
        chain algorithm and returns it as a string.
        """
        
        sentence = list()
        word = None
        sentence.append('')
        # This is a placeholder string. It allowr
        
        while sentence[-1] != None:
            # None is still used to represent the end of the sentence
            word = self._get_probable_word(word)
            sentence.append(word)

        # We get rid of the NoneType at the end of the sentence
        sentence.pop()
        # Adding each word of the sentence to a proper string
        sentence = " ".join(sentence)

        # Returns the sentence minus the withespace (caused by join())
        # at the beginning
        return sentence[1:]

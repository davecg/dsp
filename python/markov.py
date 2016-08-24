#!/usr/bin/env python
from __future__ import division, print_function
# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

from argparse import ArgumentParser,FileType
import re
from os.path import exists
import cPickle as pickle
from random import random
from operator import add
from collections import defaultdict,Counter

parser = ArgumentParser()
parser.add_argument('--text',default='hamlet.txt',type=FileType('r'))
parser.add_argument('--line',default=380,type=int,help='Starting line number.')
parser.add_argument('--words',default=40,type=int,help='Number of output words.')
parser.add_argument('--ngram',default=4,type=int)
parser.add_argument('--pickle',default='hamlet.pk',help='Save ngrams to save time.')
args = parser.parse_args()


sub_strings = [
    (r"[^\'?\w ]+",''), # remove other characters
    (r"'(?=\W)",''), # remove trailing apostrophes
    (r"(?<=\W)'",''), # remove beginning apostrophes
    (r'\s+',' '), # convert whitespace to single spaces
]

substitutions = [(re.compile(x),y) for x,y in sub_strings]


def clean(line,substitutions=substitutions):
    for regex,repl in substitutions:
        line = regex.sub(repl,line)
    return line.lower().strip().split()

if args.pickle is None or not exists(args.pickle):
    data = reduce(add,[clean(_) for _ in args.text.readlines()[args.line:] if re.search(r'\w',_)])

    print('Total words:',len(data))
    print('Unique words:',len(set(data)))

    ngrams = [defaultdict(Counter) for _ in xrange(args.ngram + 1)]

    # go through each word and count how many times words follow ngrams.
    for idx in xrange(len(data)):
        for n in xrange(args.ngram + 1):
            if n < idx:
                ngrams[n][tuple(data[idx-n:idx])][data[idx]] += 1

    # remove unique ngrams (n > 1) - otherwise might just repeat original document. keep all single word counts.
    for ngram in ngrams[2:]:
        for key in ngram.keys():
            if sum(ngram[key].values()) == 1:
                del ngram[key]

    if args.pickle:
        with open(args.pickle,'wb') as fh:
            pickle.dump(ngrams,fh,-1)
else:
    with open(args.pickle,'rb') as fh:
        ngrams = pickle.load(fh)

def weighted_choice(counter):
    total = sum(counter.values())
    cursor = random() * total
    for word in sorted(counter):
        cursor -= counter[word]
        if cursor <= 0:
            return word
    else:
        print(counter)


def next_word(seq,ngrams=ngrams):
    N = len(ngrams) - 1
    state = tuple(seq[-N:])
    for ngram in ngrams[len(state)::-1]:
        if state in ngram:
            return weighted_choice(ngram[state])
        else:
            state = state[1:]
    else:
        raise Exception('Something went wrong')
            

sequence = []

for _ in xrange(args.words):
    sequence.append(next_word(sequence))

print(' '.join(sequence))


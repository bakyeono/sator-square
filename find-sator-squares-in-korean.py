# 1. Fetch Korean word dictionary

# * Korean dictionary source: KoNLPy (http://konlpy-ko.readthedocs.io)

import urllib.request

url = 'https://raw.githubusercontent.com/konlpy/konlpy/master/konlpy/java/data/kE/dic_system.txt'
fp = urllib.request.urlopen(url)
words = [str(line, 'utf-8').rstrip() for line in fp]


# 2. Remove unnecessary information from dictionary

# 2.1 Filter out words start with other than Hangul character

def is_hangul(ch):
    return '가' <= ch <= '힣'

def starts_with_hangul(word):
    return is_hangul(word[0])

words = [word for word in words if starts_with_hangul(word)]


# 2.2 Remove tags from dictionary

def remove_tag(word):
    return word.split()[0]

words = [remove_tag(word) for word in words]


# 3. Group words by their length

import itertools

def group_by(seq, by):
    acc = {}
    for k, items in itertools.groupby(seq, by):
        acc.setdefault(k, []).extend(items)
    return acc

word_groups = group_by(words, len)



# 4. Find sator squares

def find_sator_3x3(words):
    words = set(words)
    rev = lambda w: "".join(reversed(list(w)))
    words = [w for w in words if rev(w) in words]

    squares = []
    for w1 in words:
        w2_match = lambda x: x[0] == w1[1] and x[-1] == w1[-2]
        for w2 in filter(w2_match, words):
            if w2 == rev(w2):
                square = [w1, w2, rev(w1)]
                squares.append(square)

    return squares

squares = find_sator_3x3(word_groups[3])


# 5. Print found sator squares

for x in squares:
    print("%s\n%s\n%s\n\n" % tuple(x))


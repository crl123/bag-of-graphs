import numpy as np

SEPARATION_CHARS = [",", ";", ".", " "]

def remove_extra_chars_str(text):
    ans = ""
    for ch in text.lower():
        if ch.isalpha() or ch == "'":
            ans += ch
        elif ch in SEPARATION_CHARS:
            ans += ' ' + ch
        else:
            ans += ' '
    ans = ' '.join([x for x in ans.split(' ') if len(x)>0])
    return ans

def remove_extra_chars_file(file_name):
    f = open(file_name, 'r')
    for line in f:


# Stop-words list extracted from http://dev.mysql.com/doc/refman/5.5/en/fulltext-stopwords.html
def load_stop_words(file_name = './stop-words.in'):
    f = open(file_name, 'r')
    stop_words = set()
    for word in f.read()[:-1].split(' '):
        stop_words.add(word)
    f.close()
    return stop_words

def remove_stop_words(file_name, stop_words):
    f = open(file_name, 'r')
    text = ''
    for word in f:


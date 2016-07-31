import numpy as np
import sys, os
import stemmer

SEPARATION_CHARS = [",", ";", ".", " "]
PATH_NEWS = os.environ['HOME'] + '/Documents/20newsgroup/original/'
PATH_NEWS_OUT = os.environ['HOME'] + '/Documents/20newsgroup/pre-processed/'
NEWS_INTERNAL_PATHS = dict(train='20news-bydate-train/', test='20news-bydate-test/')
NEWS_CLASSES = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']


stem = stemmer.PorterStemmer()
stop_words = None

def load_stop_words(file_name = './stop-words.in'):
    """
    Load the stop words in the global variable stop_words

    The list of stop-words was extracted from
    http://dev.mysql.com/doc/refman/5.5/en/fulltext-stopwords.html and saved into ./stop-words.in
    """
    global stop_words
    f = open(file_name, 'r')
    stop_words = set()
    for word in f.read()[:-1].split(' '):
        stop_words.add(word)
    f.close()

def remove_stop_words(text):
    """
    Remove stop words(previously load_stop_words) from a list of words
    text: list of words

    Returns: a list of words without those words belonging to
    stop words. SEPARATION_CHARS are not included as stop-words
    """
    global SEPARATION_CHARS
    clean_text = []
    for word in text:
        if word in SEPARATION_CHARS or word not in stop_words:
            clean_text.append(stem.stem(word, 0, len(word)-1))
    return clean_text

def remove_extra_chars_str(text):
    """
    Removes extra spaces for a text
    """
    global SEPARATION_CHARS
    ans = ""
    for ch in text.lower():
        if ch.isalpha() or ch == "'":
            ans += ch
        elif ch in SEPARATION_CHARS:
            ans += ' ' + ch + ' '
        else:
            ans += ' '
    ans = remove_stop_words([x for x in ans.split(' ') if len(x)>2 or x in SEPARATION_CHARS])
    ans = ' '.join(ans)
    return ans

def remove_extra_chars_file(file_name):
    """
    Removes extra spaces, numbers, and some punctuation
    characters that are not defined in SEPARATION_CHARS

    Returns: a string with words and punctuations one-
    space separated

    TODO: For the moment, it process the whole file, it
    does not differentiate among paragraphs
    """
    f = open(file_name, 'r')
    clean_text = remove_extra_chars_str(f.read())
    f.close()
    return clean_text

def run_preprocessing():
    """
    Run the pre-processing over all (train, test) files
    """
    global PATH_NEWS
    global PATH_NEWS_OUT
    global NEWS_INTERNAL_PATHS
    global NEWS_CLASSES

    load_stop_words()
    for news_class in NEWS_CLASSES:
        for level in ['train', 'test']:
            directory = '%s%s%s' % (PATH_NEWS, NEWS_INTERNAL_PATHS[level], news_class)
            for file_name in os.listdir(directory):
                print file_name
                text = remove_extra_chars_file('%s/%s' % (directory, file_name))
                f_out = open('%s%s%s/%s' % (PATH_NEWS_OUT, NEWS_INTERNAL_PATHS[level], news_class, file_name), 'w')
                f_out.write(text)
                f_out.close()
            #return None


"""
Scripts to create the directories:
cd $HOME/Documents/20newsgroup
mkdir pre-processed && cd pre-processed
mkdir 20news-bydate-train && mkdir 20news-bydate-test
for i in `ls ../original/20news-bydate-train/`; do mkdir 20news-bydate-train/$i; mkdir 20news-bydate-test/$i; done
"""



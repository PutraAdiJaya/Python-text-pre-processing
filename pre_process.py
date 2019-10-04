
import shutil
import re

import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
#STOPWORD LANG
stopWords = set(stopwords.words('indonesian'))
ps = PorterStemmer() 

# import nltk
# nltk.download('stopwords')


#CASE FOLDING
def CaseFolding(str):
    txt = str.lower()
    return txt

#REMOVE STOPWORD
def StopwordRemover(str):
    words = word_tokenize(str)
    wordsFiltered = []
    #CEK ALL STOPWORD
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)
    return wordsFiltered

#REMOVE SEMUA KAREKTER BUKAN A-Z
def Filtering(str):
    txt = str.replace("-", " ")
    return re.sub("[^a-z ]", "", txt)

#STEMMING
def Stemming(str):
    return ps.stem(str)

#TOKENIZING
def Tokenizing(str):
    return word_tokenize(str);

#STEMMING ALL
def StemmingAll(a_str):
    a_ret = []
    splitter = re.compile(r"[\s\.-]")
    #PECAH KATA DARI KALIMAT
    for word in splitter.split(a_str):
        if word == '':
            continue
        original = word.lower()
        a_ret.append(Stemming(original).strip())
    return a_ret;
 


class Preprosessing:
    #PROSES PREPROCESSING SEMUA
    def main(self, text):
        txt = CaseFolding(text);
        txt = Filtering(txt);
        txt = StemmingAll(txt);
        txt = " ".join(txt)
        txt = StopwordRemover(txt); 
        txt = " ".join(ts)
        print(txt)

        return txt

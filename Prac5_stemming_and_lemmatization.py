'''
import nltk

print("=====Porter Stemmer=====\n")
atext = "She was running towards the finish line and quickly completed the race."
stemmer = nltk.stem.PorterStemmer()
atextlist = atext.split()
n = len(atextlist)
c = 0
for word in atextlist:
    stemword = stemmer.stem(word)
    print(word, ":", stemword)
    if word != stemword:
        c += 1

print(n, ":", c)
print("stemming level(approx): ", (int)((c / n) * 100), "%")
'''
'''
print("=====Snowball Stemmer=====\n")

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

text = "The children are playing in the playground and enjoying their day."
stemmer = SnowballStemmer("english", True)
atextlist = text.split()
n=len(atextlist)
c=0
for word in atextlist:
    stemword = stemmer.stem(word)
    print(word, ":", stemword)
    if word != stemword:
        c += 1

print(n, ":", c)
print(f"Stemming level(approx): {(int)((c/n)*100)} %")
'''

print("=====Lemmatization=====\n")

from nltk.stem import WordNetLemmatizer

atext = "The birds were flying over the mountains and resting in the trees."
wordnet_lemma = WordNetLemmatizer()
atextlist = atext.split()
n = len(atextlist)
c = 0 
for word in atextlist:
    lemmaword = wordnet_lemma.lemmatize(word)
    print(word, ":", lemmaword)
    if word != lemmaword:
        c += 1
print(n, ":", c)
print(f"Lemmatization level(approx): {(int)((c/n)*100)} %")
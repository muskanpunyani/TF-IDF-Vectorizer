# MUSKAN PUNYANI

import pandas as pd
import math
import re


##FUNCTIONS

# TF function:
def computeTF(word_dict, doc):
    TFDict = {}
    docLength = len(doc)
    for word, count in word_dict.items():
        TFDict[word] = count / float(docLength)
    return TFDict

# IDF function
def computeIDF(docList):
    IDFDict = {}
    N = len(docList)

    IDFDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                IDFDict[word] += 1

    for word, val in IDFDict.items():
        IDFDict[word] = math.log10(N / float(val))

    return IDFDict

# TF*IDF FUNCTIONS
def computeTFIDF(TFDoc, Idfs):
    TFIDF = {}
    for word, val in TFDoc.items():
        TFIDF[word] = "{:.2f}".format(val * Idfs[word])
    return TFIDF


#TAKE 2 FILES AS INPUT
FILE1=input("Enter the first file")
FILE2=input("Enter the second file")

#NOW PERFORM PREPROCESSING

# 1] CONVERT TO LOWER CASE
FILE1 = FILE1.lower()
FILE2 = FILE2.lower()

#TAKING 2 EMPTY STRINGS TO STORE THE CHAR AFTER REMOVING SPECIAL CHAR
ONE = ''
TWO = ''

# 2] REMOVE SPECIAL CHARACTERS FROM BOTH THE FILES
for i in FILE1.split("\n"):
    ONE = re.sub(r"[^a-zA-Z0-9]+", ' ', i)
for j in FILE2.split("\n"):
    TWO = re.sub(r"[^a-zA-Z0-9]+", ' ', j)

# 3] SPLIT INTO DIFFERENT WORDS
ONE = ONE.split()
TWO = TWO.split()

# JOIN TWO LISTS OF WORDS
List_Of_Words = set(ONE).union(set(TWO))

#COUNT WORDS
COUNT_WORDS_1 = dict.fromkeys(List_Of_Words, 0)
COUNT_WORDS_2 = dict.fromkeys(List_Of_Words, 0)
for word in ONE:
    COUNT_WORDS_1[word] += 1

for word in TWO:
    COUNT_WORDS_2[word] += 1


# RUN TWO FILES THROUGH TF FUNCTIONS
TF_one = computeTF(COUNT_WORDS_1, ONE)
TF_two = computeTF(COUNT_WORDS_2, TWO)

# EVALUATING IDF
IDFS = computeIDF([COUNT_WORDS_1, COUNT_WORDS_2])


# RUNNING THROUGH TFIDF
idfFirst = computeTFIDF(TF_one, IDFS)
idfSecond = computeTFIDF(TF_two, IDFS)


pd.set_option('display.max_columns', None)  # to print all the columns
pd.set_option('display.width', None)  # to align all the columns on same line
output = pd.DataFrame([idfFirst, idfSecond])
print(output)


""""
OUTPUT

Enter the first file SACHIN PLAYS CRICKET
Enter the second file FEDERER PLAYS TENNIS
  cricket plays tennis federer sachin
0    0.10  0.00   0.00    0.00   0.10
1    0.00  0.00   0.10    0.10   0.00
"""""






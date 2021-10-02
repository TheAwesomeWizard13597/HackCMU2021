#import discord
#from discord.ext import commands

import csv
import os.path
import random

START_CONST = "((START))"
END_CONST = "((END))"

data = {}

def filterEmotes(string):
    filterIt = ["<:", "<@"]
    if filterIt in string:
        return false
    else:
        return true

def getCSVList(filename):
    rows = []
    with open(filename, 'r') as file:
        csvread = csv.reader(file)
        header = next(csvread)
        for row in csvread:
            #filterIt = ["<:", "<@"]
            if(len(row) >= 3):
                if ("<:" in row[2] or "<@" in row[2]):
                    continue
                else:
                    rows.append(row[2])

       # if rows.__len__() < n:
         #   rows = rows[:n]
   # print(header)
   # print(rows)
    return rows


#def readSentences(filename, n):
#    
#    with open(filename, "r") as file:
#        arr = file.read().splitlines()
#        arr = list(filter(lambda a: a.__len__() > 25, arr))
#        if arr.__len__() < n:
#            arr = arr[:n]

    #return arr

def readSentences(filename, n):
    with open(filename, "r") as file:
        arr = file.read().splitlines()
        arr = list(filter(lambda a: a.__len__() > 25, arr))
        if arr.__len__() < n:
            arr = arr[:n]
    print(arr)
    return arr

def decapFirstLet(str):
    if(str.__len__() > 1):
        return str[0].lower() + str[1:]
    else:
        return " "

def capFirstLet(str):
    return str[0].upper() + str[1:]



def add(sentence):
    data[START_CONST] = {}
    for word in sentence.split(" "):
        if word not in data:
            data[word] = {}

    last = START_CONST
    for word in sentence.split(" "):
        if word not in data[last]:
            data[last][word] = 0
        if last == START_CONST and word == END_CONST:
            pass
        elif word.__len__() < 1 or last.__len__() < 1:
            continue
        else:
            data[last][word] = data[last][word] + 1
        last = word
    
    if END_CONST not in data[last]:
        data[last][END_CONST] = 0
    data[last][END_CONST] = data[last][END_CONST] + 1


def generate():
    word = START_CONST
    words = []
    while word != END_CONST:
        weightArr = []
        for x in data[word]:
            for i in range(data[word][x]):
                weightArr.append(x)

        word = random.choice(weightArr)
        if word != END_CONST:
            words.append(word)
    
    return capFirstLet(" ".join(words))+"."

def genParagraph(num):
    final = ""
    for i in range(num):
        final += generate() + " "

    return final.strip()

def generateFromDataset(filename, num, numToGen):
    sentences = [decapFirstLet(s).replace(".", "").replace("& ", "").replace("?", "").
                replace("!", "").replace(";", "").replace(",", "").replace("\"", "").
                replace("'", "") for s in getCSVList(filename)]

    global data
    data = {}
    for i in sentences:
        add(i)

    return genParagraph(numToGen)

#getCSVList("messages.csv")
print(generateFromDataset("messages.csv", 1000, 10))

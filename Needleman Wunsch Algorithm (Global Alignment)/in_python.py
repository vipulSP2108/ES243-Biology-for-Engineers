import numpy as np

def formula(word1index, word2index, matx, error, match, mismatch):
    if(word1[word2index-1] == word2[word1index-1]):
        s = match
    else:
        s = mismatch
    digonal = matx[word1index-1][word2index-1] + s
    up = matx[word1index-1][word2index] + error
    left = matx[word1index][word2index-1] + error
    maximum = max(digonal, up, left)
    if maximum == digonal:
        tracematx[word1index][word2index] = tracematx[word1index][word2index] + "d"
    if maximum == up:
        tracematx[word1index][word2index] = tracematx[word1index][word2index] + " "
        tracematx[word1index][word2index] = tracematx[word1index][word2index] + "u"
    if maximum == left:
        tracematx[word1index][word2index] = tracematx[word1index][word2index] + " "
        tracematx[word1index][word2index] = tracematx[word1index][word2index] + "l"
    return maximum

def modify(words, madestr, i, j):
    if(madestr[len(madestr)-1] == "d"):
        i = i+1
        j = j+1
    elif(madestr[len(madestr)-1] == "u"):
        i = i+1
        j = j
    elif(madestr[len(madestr)-1] == "l"):
        i = i
        j = j+1
    madestr = madestr[:len(madestr)-1]
    words = words[:len(words)-1]
    return i,j,madestr,words

def tracebreak(madestr, words, i, j, trace):
        
    while trace!="0":                   #need to be edited for all case printing
        eliment = trace.split(" ")
        count = 0
        for elipos in range(len(eliment)):

            if(eliment[elipos]=="d"):
                if(count == 1):
                    prviousi,prviousj,prviousmadestr,prviouswords = modify(words,madestr, i, j)
                    tracebreak(prviousmadestr, prviouswords, prviousi, prviousj, eliment[elipos])
                    break
                else:
                    i = i-1
                    j = j-1
                    madestr = madestr + "d"
                    words = words + word2[i]
                    count += 1
                
            elif(eliment[elipos]=="u"):
                if(count == 1):
                    prviousi,prviousj,prviousmadestr,prviouswords = modify(words, madestr, i, j)
                    tracebreak(prviousmadestr, prviouswords, prviousi, prviousj, eliment[elipos])
                    break
                else:
                    i = i-1
                    j = j
                    madestr = madestr + "u"
                    words = words + "_"
                    count += 1
                
            elif(eliment[elipos]=="l"):
                if(count == 1):
                    prviousi,prviousj,prviousmadestr,prviouswords = modify(words, madestr, i, j)
                    tracebreak(prviousmadestr, prviouswords, prviousi, prviousj, eliment[elipos])
                    break
                else:
                    i = i
                    j = j-1
                    madestr = madestr + "l"
                    words = words +"_"
                    count += 1
                
        trace = tracematx[i][j]
    
    # print(madestr)
    # print(words.upper())
    print(words[::-1].upper())

word1 = str(input("word1 value: "))       # "agttgc" or  "sacn"
word2 = str(input("word2 value: "))       # "atgc"   or  "tcn"
match = int(input("match value: "))       # 10
mismatch = int(input("mismatch value: ")) # 5
error = int(input("error value: "))       # -10

if __name__ == '__main__' :
    rows = len(word2)+1
    cols = len(word1)+1

    scorematx = np.zeros((rows,cols))
    tracematx = [["" for i in range(cols)] for i in range(rows)]

    for i in range(len(word1) + 1):
        tracematx[0][i] = "l"
        scorematx[0][i] = 0 + i*error

    for i in range(len(word2) + 1):
        tracematx[i][0] = "u"
        scorematx[i][0] = 0 + i*error

    # print(scorematx)

    for i in range(1,len(word2)+1):
        for j in range(1,len(word1)+1):
            scorematx[i][j] = formula(i, j, scorematx, error, match, mismatch)

    # print(scorematx)

    tracematx[0][0] = "0"
    last = tracematx[len(word2)][len(word1)]

    # print(tracematx)

    madestr = ""
    words = ""
    i = len(word2)
    j = len(word1)
    trace = tracematx[i][j]
    tracebreak(madestr, words, i, j, trace)

def wordGame(sent):

    # Splits sentence into words
    wordsList = sent.split(" ")

    # function call to return middle word/words
    middleWords = getMiddleWord(wordsList)

    # function call to return longest word
    longestWord = getLongestWord(wordsList)

    # function call to return list with each word reversed
    revWords = reverseWords(wordsList)

    senWithRevWords = ""

    # revWords items appened to form sentence
    for word in revWords:
        senWithRevWords = senWithRevWords + word+" "

    # print results
    print("Middle Words: "+middleWords)
    print("LongestWord: "+longestWord)
    print("Sentence with reverse words:\n"+senWithRevWords)



# fun to get middlewords
def getMiddleWord(list):
    words = "["
    val = list.__len__()
    if(val % 2 == 0):
        words = words + list[int((val-1)/2)] + ", "
        words = words + list[int(val / 2)]
    else:
        words = words + list[int(val/2)]

    return words + "]"

#fun to get longest word
def getLongestWord(list):
    max = list[0]
    for word in list:
        if(len(word)>len(max)):
            max = word
    return max

#reverse each word in list
def reverseWords(list):
    for i in range(0,list.__len__()):
        list[i] = list[i][::-1]
    return list

wordGame("My name is Chaitanya Kumar Peravalli")
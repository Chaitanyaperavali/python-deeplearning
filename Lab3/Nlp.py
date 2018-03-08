from nltk import WordNetLemmatizer, wordpunct_tokenize, pos_tag, ngrams


def lemma():
    file1 = open('inputtext.txt', 'r')
    text = file1.readline()
    lem = []
    tags = []
    data = ""
    while text != "":
        data = data + text
        tags = tags + pos_tag( wordpunct_tokenize(text))
        # lem = WordNetLemmatizer().lemmatize((word for word in tokens), (pos for word,pos in tags))
        for word,pos in tags:
            lem.append(WordNetLemmatizer.lemmatize(word,pos))
        text = file1.readline()

    # bi-gram
    bgram = {}
    ngram = ngrams(data.split(), 2)
    for item in ngram:
        if item in bgram:
            bgram[item] += 1
        else:
            bgram[item] = 1

    # top 10 bigrams

    for i in 10:
        print(bgram[i])

    while text != "":
        for word in bgram[:10]:
            if(text.__contains__(word)):
                print(text)
        text = file1.readline()

lemma()


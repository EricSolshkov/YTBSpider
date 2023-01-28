import string
from nltk.corpus import stopwords

def count(source):
    # 预处理评论列表，做成单词列表
    words = []
    ls = list(string.punctuation)
    for each in source:
        no_space = each
        for item in ls:
            no_space = no_space.replace(item, ' ')

        append_words = no_space.lower().split()
        for each in append_words:
            words.append(each)

    # 统计全局词频
    words_count = dict()
    for word in words:
        if len(word) > 1:
            words_count[word] = words_count.get(word, 0)+1

    # 去掉停用词
    stop_words = stopwords.words('english')
    for word in stop_words:
        words_count.pop(word, 0)

    for key in list(words_count.keys()):
        if words_count[key] <= 1:
            del words_count[key]


    #words_count = sorted(words_count, key=lambda x: x[1] , reverse=True)

    return words_count

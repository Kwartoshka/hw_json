import json

def read_file(file):
    with open(file, encoding='utf-8') as f:
        json_data = json.load(f)
        return json_data

def get_txt(file):
    all_txt = []
    data = read_file(file)
    for news in data['rss']['channel']['items']:
        description = news['description'].split(' ')
        all_txt += description
    return all_txt

def get_long_words(file):
    words_list = []
    txt = get_txt(file)
    for word in txt:
        if len(word) > 6:
            words_list.append(word)
    return words_list

def get_repeats_of_words(file):
    unique_words = {}
    long_words = get_long_words(file)
    for word in long_words:
        if word not in unique_words:
            unique_words[word] = 1
        else:
            unique_words[word] += 1
    return unique_words

def get_sorted_top(file):
    repeats = get_repeats_of_words(file)
    tuples_list = list(repeats.items())
    tuples_list.sort(key=lambda file: file[1], reverse=True)
    top = []
    for word in tuples_list[:10]:
        top.append(word[0])
    return top


top = get_sorted_top('newsafr.json')
print(top)



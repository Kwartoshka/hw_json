import json

with open('newsafr.json',encoding='utf-8') as f:
    json_data = json.load(f)

all_txt = []
for news in json_data['rss']['channel']['items']:
    description = news['description'].split(' ')
    all_txt += description

long_words = []
for word in all_txt:
    # print(word)
    if len(word) > 6:
        long_words.append(word)

set_long_words = set(long_words)

list = []
top = []

for word in set_long_words:
    number_of_repeats = long_words.count(word)
    list.append([word, number_of_repeats])

list.sort(key = lambda file: file[1], reverse=True)
for word in list[:10]:
    top.append(word[0])

print(top)



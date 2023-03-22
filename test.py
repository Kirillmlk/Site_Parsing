import json

with open("news_dict.json") as file:
    news_dict = json.load(file)

search_id = "537097"

if search_id in news_dict:
    print("пидор ебаный")
else:
    print('sdgfdsfgds')

import requests
import json
import pandas as pd
import csv
import tqdm


identity = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
top_story = requests.get(identity)
id_top_story = top_story.json()


url = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty"


def link_to_id():
    list_of_dictionaries = []
    for id_s in (id_top_story):
        dictionary_hn = downloading_an_article(url.format(id_s))
        list_of_dictionaries.append(dictionary_hn)
        return (list_of_dictionaries)



print(id_top_story)
def downloading_an_article(link):
     response_link = requests.get(link)
     if response_link.status_code == 200:
         return response_link.json()





#print(type(dictionary))

#print(dictionary)


def create_csv():
    to_csv =

    keys = to_csv[0].keys()

    with open('people.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)

list_of_dictionaries = link_to_id()
#create_csv()
#print()
#for info_dict in list_of_info_dict:
#keys |= list(info_dict.keys())


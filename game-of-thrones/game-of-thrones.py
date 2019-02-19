from characters import characters
from got_houses import houses
import requests
import time

# print(houses['https://www.anapioficeandfire.com/api/houses/1'])

# for i in characters:
#         print(i['allegiances'])


# print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# # for k in jon_snow:
# #     print(k)

# # print out just the values
# # for k in jon_snow:
# #     print(jon_snow[k])

# # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))


# how many characters names' begin with 'Z'?
a_chars = []

for person in characters:
    name = person['name']
    if name[0] == 'A':
        a_chars.append(name)
print(len(a_chars))


# how many characters names' begin with 'Z'?
z_chars = []

for person in characters:
    name = person['name']
    if name[0] == 'Z':
        z_chars.append(name)
print(len(z_chars))


# how many characters are dead?
dead_chars = []

for person in characters:
    dead = person['died']
    if len(dead) > 0:
        dead_chars.append(dead)
print(len(dead_chars))


# Who has the most titles
title_array = []
for char in characters:
    num_of_titles = len(char['titles'])
    title_array.append(num_of_titles)
    if len(char['titles']) == max(title_array):
        title_holder = (char['name'])
print("%s has the most titles of" % (title_holder, num_of_titles)
        # print(num_of_titles)

most_titles = 0
person_with_most_titles = ''

# visit each character to is if they have more than `most_titles`
# if so, save that new value to `most_titles`. if not, ignore them
for person in characters:
        num_titles = len(person['titles'])
        if num_titles > most_titles:
                most_titles = num_titles
                person_with_most_titles = person['name']
# print ou the name of each person with the same number of title as `most_titles`
for person in characters:
        num_titles = len(person['titles'])
        if num_titles == most_titles:
                print('%s has %d titles' % (person_with_most_titles, most_titles))

# print('%s has %d titles' % (person['name'], most_titles))


# how many characters are valyrian?
valyrian_array = []
for char in characters:
        valyrian_chars = char['culture']
        if valyrian_chars =="Valyrian":
                valyrian_array.append(valyrian_chars)

print(len(valyrian_array))


# What actor plays "Hot Pie?"
hot_pie = ''
for char in characters:
        alias = char['name']
        if alias == "Hot Pie":
                hot_pie = char['playedBy']
print (hot_pie)


# How many characters are *not* in the tv show?
no_tv = 0
for char in characters:
        tv_series = char['tvSeries']
        if "" in tv_series:
                no_tv += 1
print(no_tv)


# Produce a list of characters with the last name "Targaryen"
targaryens = []
for char in characters:
        last_names = char['name']
        if "Targaryen" in last_names:
                targaryens.append(last_names)
print (targaryens)


#######################

# Create a histogram of the houses('allegiances')
# count the number of people who are part of a house : ATTEMPT #1

# result = []
# for char in characters:
#         allegiances = char['allegiances']
#         for allegiances in houses:
#                 result.append(allegiances)
# print (result)

# for i in result:
#         print(houses[i])



# house_histogram = {}
# allegiances = []

# for char in characters:
#         if char['allegiances'] != "" and char['allegiances'] != []:
#                 allegiances.append(char['allegiances'])
#         # print(allegiances)
# for x in allegiances:
#         # print(x)
#         for key in houses:
#                 # print (key)
#                 if key == x:
                        
#                         if houses[key] not in house_histogram:
#                                 house_histogram[houses[key]] = 1
#                         elif houses[key] in house_histogram:
#                                 house_histogram[houses[key]] = house_histogram[houses[key]] + 1

# print(house_histogram)
# # # print (houses[allegiances])

# print(houses.keys())
# print(allegiances)

#######################


# count the number of people who are part of a house : ATTEMPT #2
def make_house_histogram(character_list):
        histogram= {}

        #do the thing!
        #loop through all the characters
        for person in character_list:
                # what do i check for each person?
                allegiances = person['allegiances']
                # allegiances is a list of URLs
                # they look like this:
                # ["https://anapioficeandfire.com/api/houses/15"]
                for house in allegiances:
                        # do something with that house
                        if house in histogram:
                                histogram[house] = histogram[house] + 1
                        else:
                                histogram[house] = 1

        return histogram


def pretty_print_histogram(histogram):
        for house in histogram:
                print('%s has %d members' % (house, histogram[house]))


def translate_address_to_house_name(URL):
        house_name = ''
        r = requests.get(URL)
        house_info = r.json()
        house_name = house_info['name']
        return house_name

def convert_to_nice_names(histogram):
        nice_histogram = {}
        for url in histogram:
                house_name = translate_address_to_house_name(url)
                nice_histogram[house_name] = histogram[url]
                time.sleep(0.1)
        
        return nice_histogram

ugly_histogram = make_house_histogram(characters)
pretty_histogram = convert_to_nice_names(ugly_histogram)
pretty_print_histogram(pretty_histogram)
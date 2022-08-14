import json
import re


with open('data.json', 'r') as json_file:
    movies = json.load(json_file)

starName = ''
movieCount = 0
movieRate = 0.0
stars = []
existStar = []

for i in range(0,len(movies)):
    stars = movies[i]['stars'].split(', ')
    for y in range(0,len(stars)):
        starName = stars[y]
        for j in range(0, len(movies)):
            pattern = re.compile(starName)
            search = pattern.search(movies[j]['stars'])
            if search != None: #that star is existed in stars
                movieCount +=1
                movieRate += float(movies[j]['rating'])
        if movieCount>=2:
            if not existStar.__contains__(starName):
                print("Star Name: ","{:20s} {:4.1s}".format(starName," || "),"Movies: ",movieCount," || ","Average Rate: ","{:.2f}".format(movieRate/movieCount))
                existStar.append(starName)
        movieCount = 0
        movieRate = 0




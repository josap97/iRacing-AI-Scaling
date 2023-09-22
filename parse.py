import json

import sys

print(sys.argv[1] + ".json")

if len(sys.argv) < 2:
        print("Please give the name of the json file as an argument.")
        exit()

file = sys.argv[1] + ".json"
file1 = open(sys.argv[1] + ".txt","w")#write mode

with open(file) as jsonData:
        data = json.load(jsonData)

results = data['session_results'][0]['results']

for r in results:
        print("{0},{1}".format(r['carNumber'], r['time']))
        file1.write("{0},{1}\n".format(r['carNumber'], r['time']))

file1.close()
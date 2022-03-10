import csv
import requests
import json

urls="http://api.coincap.io/v2/assets"

response=requests.get(urls)
my_json=response.json()
# print(type(my_json))
# print(my_json)

headers=['Id','Name','Symbol']

my_list=[]
for data in my_json['data']:
    listen=[data['id'],data['name'],data['symbol']]
    my_list.append(listen)
    # print(type(listen))
# print(my_list)

with open('test2.csv','w') as f:
    write=csv.writer(f,delimiter=',')
    write.writerow(headers)

    for ls in my_list:
        write.writerow(ls)

print('done')
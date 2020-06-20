import requests
import json

url = 'https://a.tiles.mapbox.com/v4/mopc.iobaeb6c/features.json?access_token=pk.eyJ1IjoibW9wYyIsImEiOiJKNFo3aktvIn0.tQGSxRugkpMUIcxUskZHgQ'
response = requests.get(url)
data = response.text
data_dic = json.loads(data)
#print(data_dic["type"])
#print(data_dic["features"])
data_obras = data_dic["features"]
csv = ""
for obra in data_obras :
    if obra["properties"]["title"] != '':
        csv += obra["properties"]["title"] + "," + obra["properties"]["description"].replace('\n','') + "\n"    

with open('mopc.csv', 'wb') as archivo:
    archivo.write(csv.encode())
    archivo.close()

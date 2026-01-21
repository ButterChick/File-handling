import json
import urllib.request
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())


file = open("iss.txt",'w')
file.write(
    "There are currently" + str(result["number"])
    + " /n Astraunts on ISS rn /n"
)
people = result["people"]
for p in people:
  file.write(p['name'] + ' - on board' + '\n')
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()

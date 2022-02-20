import json
import time
import urllib.request
from kafka import KafkaProducer



API_KEY = "ae45c82dddb41f3ad5e4c7f34783e7f2ac39b3ae" 
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())
    for station in stations:
        producer.send("velib-topic", json.dumps(station).encode())
        print(station)
        

    
    
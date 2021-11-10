import random
from kafka import KafkaProducer
import json
import time
DIRECTION = '20.120.14.159:9092'
TOPIC = '18188'
INTERVAL = 4

directions = ['N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE']

class Station:
    def getTemperature(self):
        return round(random.uniform(0,100), 2)

    def getHumidity(self):
        return int(random.uniform(0,100))

    def getWindDirection(self):
        return  directions[random.randint(0,len(directions)-1)]

    def getMeasurements(self):
        return '{}{}{}'.format(chr(int(self.getTemperature())), chr(self.getHumidity()), chr(self.getWindDirection()))

if __name__ == '__main__':
    producer = KafkaProducer(value_serializer = lambda v: json.dumps(v).encode('utf-8') ,bootstrap_servers=DIRECTION)
    station = Station()
    while True:
        measurements = station.getMeasurements()
        message = producer.send(TOPIC, measurements)
        result = message.get()
        print(result)
        time.sleep(INTERVAL)
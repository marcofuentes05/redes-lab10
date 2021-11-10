import random

from kafka import KafkaConsumer
import json
import time
from producer import TOPIC, DIRECTION, INTERVAL

import datetime as dt
# matplotlib.use('GTK3Agg')
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def animate(i, x, y, consumer):
    message = ''
    for msg in consumer:
        message = msg
        break
    x.append(dt.datetime.now().strftime('%H:%M:%S'))
    y.append(message.value['temperature'])

    x = x[-20:]
    y = y[-20:]

    ax.clear()
    ax.scatter(x, y)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperatura del sensor')
    plt.ylabel('Temperatura (C)')

consumer = KafkaConsumer(TOPIC, bootstrap_servers=DIRECTION, value_deserializer=lambda m: json.loads(m.decode('utf-8')))
timer = 0
x_data, y_data = [], []

animation = FuncAnimation(fig, animate, fargs=(x_data, y_data, consumer), interval=10)
plt.show()


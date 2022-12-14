#  🎄 🌊 🚁 🟩 🔥 🏥 💛 🪣 🏨 🔵 🔴 🏆 ⬛

import keyboard
from clouds import Clouds
from map import Map
import time
import os
from helicopter import Helicopter as Helico
import json

TICK_SLEEP = 0.5
TREE_UPDATE = 50
CLOUDS_UPDARE = 200
FIRE_UPDATE = 100
MAR_W, MAP_H = 20, 10

field = Map(MAR_W, MAP_H)
clouds = Clouds(MAR_W, MAP_H)
helico = Helico(MAR_W, MAP_H)
tick = 1


MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1), }
#  f - сохранение, g - востановление.


def process_key(key):
    global helico, tick, clouds, field
    c = key.name
    if key.event_type == 'up':
        if c in MOVES.keys():
            dx, dy = MOVES[c][0], MOVES[c][1]
            helico.move(dx, dy)
        elif c == 'f':
            data = {"helicopter": helico.export_data(),
                    "clouds": clouds.export_data(),
                    "field": field.export_data(),
                    "tick": tick}
            with open("level.json", "w") as lvl:
                json.dump(data, lvl)
        elif c == 'g': 
            with open("level.json", "r") as lvl:
                data = json.load(lvl) 
                tick = data["tick"] or 1
                helico.import_data(data["helicopter"])
                field.import_data(data["field"])
                clouds.import_data(data["clouds"])

keyboard.hook(process_key)

while True:
    os.system("clear || clr")  # cls
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print("TICK", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()    
    if (tick % CLOUDS_UPDARE == 0):
        clouds.update()
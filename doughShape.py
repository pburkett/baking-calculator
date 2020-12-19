import json
import os
import math
import random


class DoughShape:
    def __init__(self, id, name, doughWeight):
        self.id = id
        self.name = name
        self.doughWeight = doughWeight

    def __str__(self):
        return self.name

    def generateData(self):
        dataDict = {"type": 'doughShape', "id": self.id,
                    "name": self.name, "weight": self.doughWeight}

        f = open(self.id + ".json", "w+")
        dataString = str(dataDict)
        dataString = dataString.replace("'", '"')
        f.write(dataString)

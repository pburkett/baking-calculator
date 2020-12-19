import json
import os
import math
import random

from doughShape import *


class Formula:
    def __init__(self, id, name, flourList, ingredientList):
        self.name = name
        self.id = id
        self.flourList = flourList
        self.ingredientList = ingredientList

    def __str__(self):
        return self.name

    def displayFormula(self):
        try:
            formulaDisplay = f"{self.name} Formula\n\n"

            for flour in self.flourList:
                flourDisplayTemplate = flour['flourName'] + \
                    ': ' + str(flour['flourPercentage']) + '%\n'
                formulaDisplay += flourDisplayTemplate

            for ingredient in self.ingredientList:
                ingredientDisplayTemplate = ingredient['ingredientName'] + \
                    ': ' + str(ingredient['ingredientPercentage']) + '%\n'
                formulaDisplay += ingredientDisplayTemplate

            print(formulaDisplay)
        except:
            print("An error occured while displaying this formula.")

    def generateData(self):
        dataDict = {"type": 'formula', "id": self.id, "name": self.name,
                    "flourList": self.flourList,
                    "ingredientList": self.ingredientList}

        f = open(self.name + ".json", "w+")
        dataString = str(dataDict)
        dataString = dataString.replace("'", '"')
        f.write(dataString)

    def createRecipe(self, doughWeight):
        # takes in a dough weight, returns a list of ingredients and their respective weights using the data stored in the formula class
        createdRecipe = f"\n{self.name} Recipe\n\nDough Weight: {doughWeight}\n"

        # calculates the total percentage of the non-flour ingredients
        # total ingredient percentage is set to 100 to account for the flour percentage
        totalIngredientPercentage = 100
        for ingredient in self.ingredientList:
            totalIngredientPercentage += ingredient['ingredientPercentage']

        totalFlourWeight = doughWeight / totalIngredientPercentage * 100

        # the loop sets individual weights for each flour in the flour list
        for flour in self.flourList:
            flourWeight = round(
                (totalFlourWeight * flour['flourPercentage'] / 100), 2)
            flourTemplate = f'{flour["flourName"]} : {str(flourWeight)}\n'
            createdRecipe += flourTemplate

        for ingredient in self.ingredientList:
            ingredientWeight = round(
                (totalFlourWeight * ingredient['ingredientPercentage'] / 100), 2)
            ingredientTemplate = ingredient['ingredientName'] + \
                ': ' + str(ingredientWeight) + '\n'
            createdRecipe += ingredientTemplate

        print("_____________________________________________________________")
        print(createdRecipe)

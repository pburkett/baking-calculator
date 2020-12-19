import json
import os
import math
import random

from formula import *
from doughShape import *

formulaList = []
doughShapeList = []

if __name__ == "__main__":
    print("\nExecuting as __main__...")


def idGenerator():
    return str(random.randint(0, 100000))


def loadData():
    # searches for .json files and tries to open them, then creates a Formula or DoughShape class with the data
    print("\nloading available JSON files...\n")
    formulaFileCount = 0
    doughShapeFileCount = 0
    for filename in os.listdir():

        if filename.endswith(".json"):
            f = open(filename, "r")
            fileHeader = f.read(40)

            if 'formula' in fileHeader:

                formulaFileCount += 1
                f.seek(0)
                fileString = f.read()
                fileData = json.loads(fileString)

                fileData['id'] = Formula(
                    fileData['id'], fileData['name'], fileData['flourList'], fileData['ingredientList'])
                formulaList.append(fileData['id']
                                   )
                f.close()

            elif 'doughShape' in fileHeader:
                doughShapeFileCount += 1
                f.seek(0)
                fileString = f.read()
                fileData = json.loads(fileString)

                fileData['id'] = DoughShape(
                    fileData['id'], fileData['name'], fileData['weight']
                )
                doughShapeList.append(fileData['id'])
                f.close()

    print(f"{formulaFileCount} Formula files found \n{doughShapeFileCount} Dough weight files found.")


def createFormula():
    # asks for formula data from the user, then passes that data on to the Formula module.

    formulaId = idGenerator()
    formulaName = input("Please Enter New Formula Name: ")
    # variables for use in the flour loop
    flourCount = 0
    flourList = []
    totalFlourPercentage = 0
    # flour input loop
    while totalFlourPercentage != 100:
        flourName = input(
            f"Number of flour types: {flourCount}\nEnter flour type.\n>> ")
        flourPercentage = float(
            input(f"Enter baker's percentage (1-100) of {flourName}\n>> "))
        flourDict = {
            "flourName": flourName,
            "flourPercentage": flourPercentage
        }
        flourList.append(flourDict)
        flourCount += 1
        totalFlourPercentage += flourPercentage

    # variables for use in the ingredient loop
    ingredientCount = 0
    ingredientList = []
    # ingredient input loop
    while True:
        ingredientName = input(
            (f"\nNumber of ingredient types: {ingredientCount}\nType 'done' to finish entering formula.\nEnter ingredient type.\n>> "))
        if ingredientName == 'done':
            break
        ingredientPercentage = float(
            input(f"Enter baker's percentage(1-100) of {ingredientName}\n>> "))
        ingredientDict = {
            "ingredientName": ingredientName,
            "ingredientPercentage": ingredientPercentage
        }
        ingredientList.append(ingredientDict)
        ingredientCount += 1

    formulaId = Formula(formulaId, formulaName, flourList, ingredientList)
    formulaId.generateData()


def createDoughShape():
    doughShapeId = idGenerator()
    doughShapeName = input("Enter new dough shape name:\n>>  ")
    doughShapeWeight = float(input("Enter dough weight:\n>> "))

    doughShapeId = DoughShape(doughShapeId, doughShapeName, doughShapeWeight)
    doughShapeId.generateData()


def remWhiteSpace(x):
    # removes whitespace from the beggining and end of a string, and removes double whitespace throughout
    # courtesy of Farzi <3
    while x[0] == " ":
        x = x[1:]
    while x[-1] == " ":
        x = x[:-1]
    return x


def deleteFormula():
    # asks for a valid Formula name, then deletes that formula .json file
    userInput = input(
        "Enter the name of the formula you would like to delete:\nThis cannot be undone! Type 'exit' to cancel.\n>>")
    if userInput == 'exit':
        pass
    elif os.path.exists(userInput + '.json'):
        os.remove(userInput + '.json')
        print(f'File {userInput}.json will be deleted on startup.')
    else:
        print("Formula file can not be found.")


def returnFormulaName(userSelection):
    # takes in a string, and returns the formula class if the string matches the name
    for formula in formulaList:
        if userSelection == formula.name:
            return formula
    else:
        print("Formula file can not be found.")


def displayBook():
    print('\nFormulas:\n')
    for formula in formulaList:
        print('<' + formula.name + '>')
    print('\n\nShapes:\n')
    for shape in doughShapeList:
        print('<' + shape.name + '>')


loadData()
displayBook()
# main menu loop

while True:
    print("_____________________________________________________________")
    userSelection = input(
        "CalcuBaker V 1.0\n \nEnter a formula name to calculate a recipe.\n'formula' to create a new formula. \n'shape' to create a new dough shape. \n'edit' to make changes to existing formulas. \n'view book' to view all saved formulas.\n'delete' to remove a formula. \n'display' to display a formula. \n'exit' to close the application.\n>> ")
    if userSelection == 'formula':
        createFormula()
    if userSelection == 'shape':
        createDoughShape()
    elif userSelection == 'delete':
        deleteFormula()
    elif userSelection == 'edit':
        formula = returnFormulaName(
            input('Enter the name of the formula to be edited:\n>> '))
        formula.editFormula()
    elif userSelection == 'view book':
        displayBook()
    elif userSelection == 'exit':
        print("It's getting dark...")
        break
    elif userSelection == 'display':
        formula = returnFormulaName(
            input("Enter the name of the formula to be displayed:\n>> "))
        formula.displayFormula()
    else:
        formula = returnFormulaName(userSelection)
        doughWeight = int(input(
            "Please enter the desired total dough weight: "))
        formula.createRecipe(doughWeight)

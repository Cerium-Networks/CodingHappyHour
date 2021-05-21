from pathlib import Path
from collections import deque

def printHeader(Problem, Challenge=""):
    if(Challenge != ""):
        print("\n--- Problem {Problem}, Challenge {Challenge} ---\n")
    else:
        print("\n--- Problem {Problem} ---\n")

def Warmup():
    numbers = [1, 5, 2, 4, 7, 21, 6, 6, 15, 15, 42, 1, 2, 8, 12, 2]
    numbers = sorted(list(set(numbers)), reverse=True)
    
    removeCount = int(input("How many numbers should I remove? "))
    for _ in range(removeCount):
        if(len(numbers) > 0):
            print(numbers.pop())

def Solution1():
    lines = []
    with open(Path('Week-3/animals.txt')) as file:
        for line in file.readlines():
            lines.append(line.strip('\n'))
    
    printHeader(1,1)
    for i, line in enumerate(lines):
        print(f"{i} - {line}")
    
    printHeader(1,2)
    for i, line in enumerate(lines):
        if i % 2 == 0: 
            print(f"{i} - {line}")

    return lines

def Solution2(animalsList):
    printHeader(1)
    animalsList = list(set(animalsList))
    print(animalsList)

def Solution3():
    with open(Path("Week-3/animals.csv")) as file:
        animals = dict()
        for line in file.readlines():
            key,value = line.strip('\n').split(',')
            if(key in animals.keys()):
                animals[key].append(value)
            else:
                animals[key] = [value]

    return animals

def Solution4():
    wordsStack = []
    undoStack = []

    word = input("Enter a word(s): ")
    while(word != "PRINT"):
        if(word == "UNDO" and len(wordsStack) > 0):
            removed = wordsStack.pop()
            undoStack.append(removed)
        elif(word == "REDO" and len(undoStack) > 0):
            added = undoStack.pop()
            wordsStack.append(added)
        elif(word != "UNDO" and word != "REDO"):
            wordsStack.append(word)
        
        word = input("~ ")

    for line in wordsStack:
        print(line, end=" ")


if __name__ == "__main__":
    Warmup()
    
    animalsList = Solution1()
    Solution2(animalsList)
    Solution3()
    Solution4()
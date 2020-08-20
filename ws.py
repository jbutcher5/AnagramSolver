import random
import json
from threading import Thread as T_
from itertools import permutations

class jsonLoader:
    def __init__(self, writeList, jsonFile):
        self.writeList = writeList
        self.jsonFile = jsonFile

    # Threaded
    def load_data_threaded(self):
        with open(self.jsonFile) as jFile:
            data = json.load(jFile)

        for key, item in data.items():
            self.writeList.append(key)

    # Non Threaded
    def load_data(self):
        threadFunc = T_(target=self.load_data_threaded())
        threadFunc.start()
        threadFunc.join()

def randomLetters(size):
    nums = []
    for _ in range(size):
        rand = random.randint(97, 122)
        nums.append(rand)

    letters = [chr(_) for _ in nums]
    return ''.join(letters)

def split(word):
    return [char for char in word]

class wordBrute:
    def __init__(self, writeList, letters):
        self.writeList = writeList
        self.letters = letters

    def brute(self):

        for p in permutations(self.letters):
            self.writeList.append(''.join(p))

        newList = []

        for p in self.writeList:
            chars = split(p)

            while len(chars) > 1:

                newList.append("".join(chars))
                del chars[-1]

        newList = list(newList)

        for i in newList:
            self.writeList.append(i)

        del newList

    def solve(self,jsonData):
        self.writeList

        correctWord_ = list(set(jsonData) & set(self.writeList))

        return correctWord_
import random

zoznam = list()
options = [5, 3, 0, -3, -5]

numOfGirls = 13
numOfUsers = 8

UserList = ["Dano", "Martin", "Filip", "Aron", "Peťo", "Juro", "Bero", "Matej"]
GirlList = ["Janka", "Katka", "Nana", "Paula", "Mária", "Sára", "Klára", "Natália", "Kaja", "Simona", "Michaela", "Viktória", "Alexandra"]

TestUser = []

# VYTVORENIE ZOZNAMU
for i in range(numOfUsers):
    arr = list()
    for j in range(numOfGirls):
        arr.append(random.choice(options))
    zoznam.append(arr)

# ------------------------------------------------------------------------------------------


class Statistics:

    def bestWorstRating(array, hodnotenie):
        global resultArr
        resultArr = list()
        for iteracia in range(len(array[0])):
            sum = 0
            for i in range(len(array)):
                sum = sum + array[i][iteracia]
            resultArr.append(sum)
        print()
        if hodnotenie == "top":
            return resultArr.index(max(resultArr))
        else:
            return resultArr.index(min(resultArr))

    def mostUnknown(array):
        global resultArr
        resultArr = list()
        for iteracia in range(len(array[0])):
            sum = 0
            for i in range(len(array)):
                if array[i][iteracia] == 0:
                    sum = sum + 1
            resultArr.append(sum)
        return resultArr.index(max(resultArr))

    @staticmethod
    def statistics(self):
        print("***STATISTICS***", end="")
        print("Best rated:", GirlList[Statistics.bestWorstRating(zoznam, "top")], "(", ((max(resultArr)/numOfUsers)*10)+50, "% )", end="")
        print("Worst rated:", GirlList[Statistics.bestWorstRating(zoznam, "worst")], "(", ((min(resultArr)/numOfUsers)*10)+50, "% )")
        print("Most unknown:", GirlList[Statistics.mostUnknown(zoznam)])
        print("***STATISTICS***", end="\n")

# ------------------------------------------------------------------------------------------


class Core:

    def similarity(TestUser, User):
        s = 0
        float = random.uniform(0.0, 0.9)
        for i in range(numOfUsers):
            if TestUser[i] == User[i] and (TestUser[i] != 0 or User[i] != 0):
                s = s + pow(max(options), 2)
            s = s + TestUser[i] * User[i]
        return s + (float/10)
    '''
    # ***TROCHU SA NA TO POZRIET***
    def TestSimilarity(TestUser, User):
        result2 = 0
        float = random.uniform(0.0, 0.9)
        for i in range(numOfUsers):
            result = 10
            s = 0
            if TestUser[i] != 0 or User[i] != 0:
                if (TestUser[i] == User[i]):
                    result = result + 3
                else:
                    s = TestUser[i] - User[i]
                    s = abs(s)
                    result = result - (s)
                if s >= 8:
                    result = result - 3
            result2 = result2 + result
        return((result2+(float/10)))
    '''

    @staticmethod
    def main(self):
        global numOfUsers, zoznam, TestUser
        tempArr = list()
        for i in range(numOfUsers):
            tempArr.append(Core.similarity(zoznam[i], TestUser))
        # print(tempArr)

        for order in range(3):
            for i in range(numOfUsers):
                if tempArr[i] == Other.findKthElement(tempArr, order):  # najdem maximum v tempArray
                    newArr = list()
                    newArr.append(zoznam[i])
                    print("\n")
                    print(order + 1, "best similar user(", int(Other.findKthElement(tempArr, order)), "):",
                          UserList[Other.findKthElement(tempArr, order, True)].upper())
                    print("Similarity:", Other.levelOfSimilarity(Other.findKthElement(tempArr, order)), "\n")
                    print("---Results---")

            for i in range(numOfGirls):
                if TestUser[i] == 0:
                    girlIndex = i
                    if newArr[0][girlIndex] > 2:
                        print(GirlList[i], ":", newArr[0][girlIndex])
                    else:
                        if newArr[0][girlIndex] < 0:
                            print(GirlList[i], "not recommended.")

# ------------------------------------------------------------------------------------------


class Other:

    @staticmethod
    def enterData(self):
        global TestUser, name
        name = str(input("Okay, now type your name: "))
        print("Welcome,", name + "! Please, rate the following:\n")
        for i in range(len(GirlList)):
            print(GirlList[i])
            x = int(input("Your rating(-5, 5): "))
            if (x >= -5) and (x <= 5):
                TestUser.append(x)
            else:
                print("Invalid input")
        return TestUser

    def findKthElement(array, k, index=False):
        tempArr = []
        for i in range(len(array)):
            tempArr.append(array[i])
        tempArr.sort(reverse=True)
        wanted = tempArr[k]
        for i in range(len(array)):
            if array[i] == wanted:
                if index == False:
                    return array[i]
                else:
                    return i

    @staticmethod
    def printFakeData(self):
        global zoznam, TestUser, name
        for i in range(numOfGirls):
            print(GirlList[i], end="  ")
        print("\n")
        for i in range(numOfUsers):
            print(UserList[i], zoznam[i], end="\n")
        print()
        print(name + ":", TestUser, end="\n\n")

    def levelOfSimilarity(num):
        if num <= 30:
            return "Very weak"
        elif num > 30 and (num <= 60):
            return "Weak"
        elif num > 60 and (num <= 80):
            return "Good"
        elif num > 80 and (num <= 110):
            return "Strong"
        elif num > 110 and (num <= 140):
            return "Very Strong"
        elif num > 140:
            return "Ultra Strong"

# ------------------------------------------------------------------------------------------


data = str(input("Would you like random data or your own? Type 'rnd' or 'own':"))
if data == "rnd":
    name = str(input("Okay, now type your name: "))
    for i in range(numOfGirls):
        TestUser.append(random.choice(options))
elif data == "own":
    Other.enterData(True)
else:
    print("Type 'rnd' or 'own'.")

Other.printFakeData(True)
Statistics.statistics(True)

# Podmienky pre spustenie
if (numOfUsers >= 3 and numOfGirls >= 3) and (numOfGirls >= numOfUsers) and (len(TestUser) == numOfGirls):
    Core.main(True)
else:
    print("\n***ERROR***\nCannot count your similarity. Check the following:")
    print("1) More than 3 users.\n2) More than 3 products.\n3) Same amount or more products than users.\n"
          "4) Each rating corresponds to exactly one product.")

# lock = input()





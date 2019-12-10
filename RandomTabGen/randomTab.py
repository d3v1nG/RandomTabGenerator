import random as rand

# this is a project that i am going to use to help learn music theory
# also a way of pushing off studying during dead week
# i havent been playing guitar long so easy on the criticism / validity of the random computer generated tabs

#temp key, add more later
# string = [ 1 , 2 , 3 , 4 , 5 , 6 ]
stringList   = ["E | ","A | ","D | ","G | ","B | ","e | "]
# fret = [5,6,7,8]

length = 10
randomTab = []

def generateTab(length):
    while(len(randomTab) != length):
        string = rand.randrange(1,7)
        fret = rand.randrange(5,9)
        note = str(string) +"~"+ str(fret)
        # print(note)
        randomTab.append(note)

def formatTab(tablist):
    for n in tablist:
        temp = n.split("~")
        currentString = int(temp[0]) - 1
        stringList[currentString] += ("-"+str(temp[1])+"-")
        for idx, s in enumerate(stringList):
            if (idx != currentString):
                    stringList[idx] += ("---")

def saveToFile(tabList):
    # saves all tabs generated
    # probably a writeline
    line = open("GeneratedTabs.txt", "a")
    line.write(tabList[5] + "\n")
    line.write(tabList[4] + "\n")
    line.write(tabList[3] + "\n")
    line.write(tabList[2] + "\n")
    line.write(tabList[1] + "\n")
    line.write(tabList[0] + "\n\n")


def displayTab(tabList):
    # try for loop, quick and easy solution
    # tabList.reverse() and loop through that
    print(tabList[5])
    print(tabList[4])
    print(tabList[3])
    print(tabList[2])
    print(tabList[1])
    print(tabList[0])


generateTab(length)
formatTab(randomTab)
displayTab(stringList)
saveToFile(stringList)

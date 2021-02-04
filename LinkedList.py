from collections import defaultdict


class Node:

    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode

        else:
            lastNode = self.head

            while True:
                if lastNode.nextNode is None:
                    break
                else:
                    lastNode = lastNode.nextNode

            lastNode.nextNode = newNode

    def printList(self):
        startNode = self.head

        while True:
            print(startNode.data)
            if startNode.nextNode is None:
                break
            else:
                startNode = startNode.nextNode

    def getMiddle(self):
        startSlow = self.head
        startFast = self.head

        while True:
            if startFast.nextNode is None:
                break
            else:
                startSlow = startSlow.nextNode
                if startFast.nextNode.nextNode is None:
                    startFast = startFast.nextNode
                else:
                    startFast = startFast.nextNode.nextNode


        print(startSlow.data)

    def length(self):
        x = 0

        startNode = self.head

        while True:
            x = x + 1
            if startNode.nextNode is None:
                break
            else:
                startNode = startNode.nextNode

        print(x)

    def thirdNode(self):

        startNode = self.head

        while True:
            if startNode.nextNode.nextNode.nextNode is None:
                break

            else:

                startNode = startNode.nextNode


        print(startNode.data)


    def findDuplicate(self):

        letterDict = dict()
        startNode = self.head
        x = 0

        while True:
            if startNode is None:
                break

            if startNode.data in letterDict :
                print("Duplicate exists in ",letterDict[startNode.data],x)
                break

            letterDict[startNode.data] = x
            startNode = startNode.nextNode
            x = x + 1



node1 = Node("a")
node2 = Node("b")
node3 = Node("c")
node4 = Node("d")
node5 = Node("e")
node6 = Node("f")
node7 = Node("g")
node8 = Node("b")

linkedList = LinkedList()

linkedList.insert(node1)
linkedList.insert(node2)
linkedList.insert(node3)
linkedList.insert(node4)
linkedList.insert(node5)
linkedList.insert(node6)
linkedList.insert(node7)
linkedList.insert(node8)

linkedList.findDuplicate()












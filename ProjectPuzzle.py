import math

class node:
    def __init__(self) -> None:
        icost = 0
        heuristic = 0
        puz = []
    def getIcost(self):
        return self.icost
    def getHeuristic(self):
        return self.heuristic 
    def getPuzzle(self):
        return self.puz
    def setPuzzle(self, puz):
        self.puz = puz
    def setIcost(self, icost):
        self.icost = icost
    def setHeuristic(self, heuristic):
        self.heuristic = heuristic 
        
def defPuzzle():
    print('Welcome to Aramis\'s 8 puzzle solver!')
    puzzlechoice = int(input('Type "1" to use a default puzzle, or "2" to enter your own puzzle. '))
    if puzzlechoice == 1:
        puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    else:
        print('Enter your puzzle, use a zero to represent the blank')
        row1 = input('Enter the first row, use space or tabs between numbers ')
        row1 = row1.split(' ')
        for i in range(len(row1)):
            row1[i] = int(row1[i])
        row2 = input('Enter the second row, use space or tabs between numbers ')
        row2 = row2.split(' ')
        for j in range(len(row2)):
            row2[j] = int(row2[j])
        row3 = input('Enter the third row, use space or tabs between numbers ')
        row3 = row3.split(' ')
        for k in range(len(row3)):
            row3[k] = int(row3[k])
        puzzle = [row1, row2, row3]
    print(puzzle)
    return puzzle

def defAlgorithm():
    print('Enter your choice of algorithm')
    print('Uniform Cost Search')
    print('A* with the Misplaced Title heuristic')
    print('A* with the Eucledian distance heuristic')
    choice = int(input())
    return choice

def expandNodes(c1, alg, i, j, puzzle, frontier, goal, visited):
    didExpand = False
    if(i == 0 and j == 0):
        puz1 = [[puzzle[0][1], puzzle[0][0], puzzle[0][2]], [puzzle[1][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz2 = [[puzzle[1][0], puzzle[0][1], puzzle[0][2]], [puzzle[0][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        child1 = node()
        child1.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz1, goal)
        child1.setHeuristic(h1)
        child1.setPuzzle(puz1)
        child2 = node()
        child2.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz2, goal)
        child2.setHeuristic(h1)
        child2.setPuzzle(puz2)
        if child1.puz not in visited:
            frontier.append(child1)
            visited.append(child1.puz)
            didExpand = True
        if child2.puz not in visited:
            frontier.append(child2)
            visited.append(child2.puz)
            didExpand = True
    if(i == 0 and j == 1):
        puz1 = [[puzzle[0][1], puzzle[0][0], puzzle[0][2]], [puzzle[1][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz2 = [[puzzle[0][0], puzzle[0][2], puzzle[0][1]], [puzzle[1][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz3 = [[puzzle[0][0], puzzle[1][1], puzzle[0][2]], [puzzle[1][0], puzzle[0][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        child1 = node()
        child1.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz1, goal)
        child1.setHeuristic(h1)
        child1.setPuzzle(puz1)
        child2 = node()
        child2.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz2, goal)
        child2.setHeuristic(h1)
        child2.setPuzzle(puz2)
        child3 = node()
        child3.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz3, goal)
        child3.setHeuristic(h1)
        child3.setPuzzle(puz3)
        if child1.puz not in visited:
            frontier.append(child1)
            visited.append(child1.puz)
            didExpand = True
        if child2.puz not in visited:
            frontier.append(child2)
            visited.append(child2.puz)
            didExpand = True
        if child3.puz not in visited:
            frontier.append(child3)
            visited.append(child3.puz)
            didExpand = True
    if(i == 0 and j == 2):
        puz1 = [[puzzle[0][0], puzzle[0][2], puzzle[0][1]], [puzzle[1][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz2 = [[puzzle[0][0], puzzle[0][1], puzzle[1][2]], [puzzle[1][0], puzzle[1][1], puzzle[0][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        child1 = node()
        child1.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz1, goal)
        child1.setHeuristic(h1)
        child1.setPuzzle(puz1)
        child2 = node()
        child2.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz2, goal)
        child2.setHeuristic(h1)
        child2.setPuzzle(puz2)
        if child1.puz not in visited:
            frontier.append(child1)
            visited.append(child1.puz)
            didExpand = True
        if child2.puz not in visited:
            frontier.append(child2)
            visited.append(child2.puz)
            didExpand = True
    if(i == 1 and j == 0):
        puz1 = [[puzzle[1][0], puzzle[0][1], puzzle[0][2]], [puzzle[0][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz2 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][1], puzzle[1][0], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz3 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[2][0], puzzle[1][1], puzzle[1][2]], [puzzle[1][0], puzzle[2][1], puzzle[2][2]]]
        child1 = node()
        child1.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz1, goal)
        child1.setHeuristic(h1)
        child1.setPuzzle(puz1)
        child2 = node()
        child2.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz2, goal)
        child2.setHeuristic(h1)
        child2.setPuzzle(puz2)
        child3 = node()
        child3.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz3, goal)
        child3.setHeuristic(h1)
        child3.setPuzzle(puz3)
        if child1.puz not in visited:
            frontier.append(child1)
            visited.append(child1.puz)
            didExpand = True
        if child2.puz not in visited:
            frontier.append(child2)
            visited.append(child2.puz)
            didExpand = True
        if child3.puz not in visited:
            frontier.append(child3)
            visited.append(child3.puz)
            didExpand = True
    if(i == 1 and j == 1):
        puz1 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][1], puzzle[1][0], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz2 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[1][2], puzzle[1][1]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz3 = [[puzzle[0][0], puzzle[1][1], puzzle[0][2]], [puzzle[1][0], puzzle[0][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz4 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[2][1], puzzle[1][2]], [puzzle[2][0], puzzle[1][1], puzzle[2][2]]]
        child1 = node()
        child1.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz1, goal)
        child1.setHeuristic(h1)
        child1.setPuzzle(puz1)
        child2 = node()
        child2.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz2, goal)
        child2.setHeuristic(h1)
        child2.setPuzzle(puz2)
        child3 = node()
        child3.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz3, goal)
        child3.setHeuristic(h1)
        child3.setPuzzle(puz3)
        child4 = node()
        child4.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz4, goal)
        child4.setHeuristic(h1)
        child4.setPuzzle(puz4)
        if child1.puz not in visited:
            frontier.append(child1)
            visited.append(child1.puz)
            didExpand = True
        if child2.puz not in visited:
            frontier.append(child2)
            visited.append(child2.puz)
            didExpand = True
        if child3.puz not in visited:
            frontier.append(child3)
            visited.append(child3.puz)
            didExpand = True
        if child4.puz not in visited:
            frontier.append(child4)
            visited.append(child4.puz)
            didExpand = True
    if(i == 1 and j == 2):
        puz1 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[1][2], puzzle[1][1]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz2 = [[puzzle[0][0], puzzle[0][1], puzzle[1][2]], [puzzle[1][0], puzzle[1][1], puzzle[0][2]], [puzzle[2][0], puzzle[2][1], puzzle[2][2]]]
        puz3 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[1][1], puzzle[2][2]], [puzzle[2][0], puzzle[2][1], puzzle[1][2]]]
        child1 = node()
        child1.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz1, goal)
        child1.setHeuristic(h1)
        child1.setPuzzle(puz1)
        child2 = node()
        child2.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz2, goal)
        child2.setHeuristic(h1)
        child2.setPuzzle(puz2)
        child3 = node()
        child3.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz3, goal)
        child3.setHeuristic(h1)
        child3.setPuzzle(puz3)
        if child1.puz not in visited:
            frontier.append(child1)
            visited.append(child1.puz)
            didExpand = True
        if child2.puz not in visited:
            frontier.append(child2)
            visited.append(child2.puz)
            didExpand = True
        if child3.puz not in visited:
            frontier.append(child3)
            visited.append(child3.puz)
            didExpand = True
    if(i == 2 and j == 0):
        puz1 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][1], puzzle[2][0], puzzle[2][2]]]
        puz2 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[2][0], puzzle[1][1], puzzle[1][2]], [puzzle[1][0], puzzle[2][1], puzzle[2][2]]]
        child1 = node()
        child1.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz1, goal)
        child1.setHeuristic(h1)
        child1.setPuzzle(puz1)
        child2 = node()
        child2.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz2, goal)
        child2.setHeuristic(h1)
        child2.setPuzzle(puz2)
        if child1.puz not in visited:
            frontier.append(child1)
            visited.append(child1.puz)
            didExpand = True
        if child2.puz not in visited:
            frontier.append(child2)
            visited.append(child2.puz)
            didExpand = True
    if(i == 2 and j == 1):
        puz1 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][2], puzzle[2][1]]]
        puz2 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][1], puzzle[2][0], puzzle[2][2]]]
        puz3 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[2][1], puzzle[1][2]], [puzzle[2][0], puzzle[1][1], puzzle[2][2]]]
        child1 = node()
        child1.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz1, goal)
        child1.setHeuristic(h1)
        child1.setPuzzle(puz1)
        child2 = node()
        child2.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz2, goal)
        child2.setHeuristic(h1)
        child2.setPuzzle(puz2)
        child3 = node()
        child3.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz3, goal)
        child3.setHeuristic(h1)
        child3.setPuzzle(puz3)
        if child1.puz not in visited:
            frontier.append(child1)
            visited.append(child1.puz)
            didExpand = True
        if child2.puz not in visited:
            frontier.append(child2)
            visited.append(child2.puz)
            didExpand = True
        if child3.puz not in visited:
            frontier.append(child3)
            visited.append(child3.puz)
            didExpand = True
    if(i == 2 and j == 2):
        puz1 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[1][1], puzzle[1][2]], [puzzle[2][0], puzzle[2][2], puzzle[2][1]]]
        puz2 = [[puzzle[0][0], puzzle[0][1], puzzle[0][2]], [puzzle[1][0], puzzle[1][1], puzzle[2][2]], [puzzle[2][0], puzzle[2][1], puzzle[1][2]]]
        child1 = node()
        child1.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz1, goal)
        child1.setHeuristic(h1)
        child1.setPuzzle(puz1)
        child2 = node()
        child2.setIcost(c1 + 1)
        h1 = heuristicAlgo(alg, puz2, goal)
        child2.setHeuristic(h1)
        child2.setPuzzle(puz2)
        if child1.puz not in visited:
            frontier.append(child1)
            visited.append(child1.puz)
            didExpand = True
        if child2.puz not in visited:
            frontier.append(child2)
            visited.append(child2.puz)
            didExpand = True
    return didExpand
            

def heuristicAlgo(n, puzzle, goal):
    heuristic = 0
    if n == 1:
        heuristic = 0
    elif n == 2:
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if ((puzzle[i][j] != goal[i][j]) and (puzzle[i][j] != 0)) :
                    heuristic += 1
    elif n == 3:
        pri = 0
        pci = 0
        gri = 0
        gci = 0
        for j in range(9):
            for k in range(len(puzzle)):
                for l in range(len(puzzle[k])):
                    if ((puzzle[k][l] == j) and (puzzle[k][l] != 0)) :
                        pri = k
                        pci = l  
            for m in range(len(goal)):
                for n in range(len(goal[m])):
                    if ((goal[m][n] == j) and (goal[m][n] != 0)) :
                        gri = m
                        gci = n 
            heuristic += math.sqrt((gci - pci)**2 + (gri - pri)**2)
    return heuristic

def sortOrder(frontier):
    for i in range(len(frontier)):
        for j in range(len(frontier)):
            totalCost1 = frontier[i].getIcost() + frontier[i].getHeuristic()
            totalCost2 = frontier[j].getIcost() + frontier[j].getHeuristic()
            if totalCost2 < totalCost1:
                tempVal = frontier[i] 
                frontier[i] = frontier[j]
                frontier[j] = tempVal
    return frontier

def matchGoal(currentNode, goal):
    puzzle = currentNode.puz
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if (puzzle[i][j] != goal[i][j]):
                return False
    return True

def main():
    goalFound = False
    nodesExpanded = 0
    maxSize = 0
    currentSize = 0
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    puzzle = defPuzzle()
    algorithm = defAlgorithm()
    visited = []
    frontier = []
    firstNode = node()
    firstNode.setIcost(0)
    h1 = heuristicAlgo(algorithm, puzzle, goal)
    firstNode.setHeuristic(h1)
    firstNode.setPuzzle(puzzle)
    frontier.append(firstNode)
    currentSize = len(frontier)
    maxSize = currentSize
    while (len(frontier) != 0):
        currentNode = frontier.pop()
        currentSize -= 1
        rindex = 0
        cindex = 0
        for i in range(3):
            for j in range(3):
                if (currentNode.puz[i][j] == 0):
                    rindex = i 
                    cindex = j
        if (nodesExpanded == 0):
            print("Expanding state\n")
            print(currentNode.puz, "\n")
        else:
            print("The best state to expand with g(n) = ", currentNode.getIcost(), " and h(n) = ", currentNode.getHeuristic(), " is...\n")
            print(currentNode.puz)
            print("\t Expanding this node...\n \n")
        if (matchGoal(currentNode, goal)):
            goalFound = True
            print("GOAL!!!\n")
            print(currentNode.puz, "\n")
            print("To solve this problem the search algorithm expanded a total of ", nodesExpanded, " nodes.\n")
            print("The maximum number of nodes in the queue at any one time: ", maxSize, ".\n")
            print("The depth of the goal node was ", currentNode.icost, ".")
            break
        expandInc = expandNodes(currentNode.getIcost(), algorithm, rindex, cindex, currentNode.getPuzzle(), frontier, goal, visited)
        if (expandInc):
            nodesExpanded += 1
        currentSize = len(frontier)
        if (currentSize > maxSize):
            maxSize = currentSize
        frontier = sortOrder(frontier)
    if ((len(frontier) == 0) and (not goalFound)):
        print("No Solution Found.\n")

main()
    

# Least Moves Knight Chess 

# Description:
# On  a (0-8)*(0-8) chess board, a starting and ending position for a knight is given, this program returns the least 
# number of moves required for it to get from the start to the end position.

def leastMovesKnight():

    # Get start position inputs and validate them
    posVals = []
    for i in range(4):
        invalid = True
        while invalid:
            try:
                if i == 0:
                    msg = "Start Row (0-8): "
                elif i == 1:
                    msg = "Start Col (0-8): "
                elif i == 2:
                    msg = "End Row (0-8): "
                else:
                    msg = "End Col (0-8): "
                posInp = input(msg)
                posInp = int(posInp)
                if posInp <= 8 and posInp >= 0:
                    invalid = False
                else:
                    print("Invalid input. Please enter a value in range 0-8 so it fits on the chess board.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        posVals.append(posInp)
    startPos = (posVals[0], posVals[1], 0)
    endPos = (posVals[2], posVals[3])

    if startPos[0] == endPos[0] and startPos[1] == endPos[1]:
        return(0)

    # Uses Breadth First Search to reach the end position, and when it has, it returns the 3rd element of the position
    # tuple (the least number of moves at which that position was found), as the least number of moves required to 
    # reach it.
    visited = [startPos]
    queue = [startPos]

    while queue:
        currentNode = queue.pop(0)
        childNodes = movesPossible(currentNode[0], currentNode[1], currentNode[2])
        print("-------NEXT NODE-------")
        for node in childNodes:
            if isNodeVisited(node, visited) == False:
                print(node)
                visited.append(node)
                queue.append(node)
                if node[0] == endPos[0] and node[1] == endPos[1]:
                    return(node[2])
    return(-1)

# Generates an array of all valid positions (not off grid) that a knight can move to given its current position.
def movesPossible(r, c, layer):

    allMoves = [(r+2, c+1, layer+1), (r+2, c-1, layer+1), (r+1, c+2, layer+1), (r+1, c-2, layer+1), 
                (r-2, c+1, layer+1), (r-2, c-1, layer+1), (r-1, c+2, layer+1), (r-1, c-2, layer+1)]
    validMoves = []
    for m in allMoves:
        if m[0] >= 0 and m[0] <= 8 and m[1] >= 0 and m[1] <= 8:
            validMoves.append(m)
    return validMoves

# Checks if a node has been visited already, in order for the leastMovesKnight() function to not add it into the queue
# again. Each position is stored as its row, column numebrs and which number of move it was reached in, therefore,
# all positions that are found repeatedly, should not be added to the queue again since it was previously already found 
# at the same or fewer number of moves.
def isNodeVisited(node, visited):
    nodeVisited = False
    for v in visited:
        if node[0] == v[0] and node[1] == v[1]:
            nodeVisited = True
    return nodeVisited 

result = "\n\nThe least number of moves required to get to the end position is:\n" + str(leastMovesKnight())
print(result)
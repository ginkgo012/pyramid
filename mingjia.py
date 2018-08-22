import math

#input = [2,8,9,1,12,9,1,4,3,6]
# Read data from text file
inputString = []
with open('pyramidData.txt', 'r') as f:
    for line in f:
        inputString.extend(line.split())

input = list(map(int,inputString))
rootValue = input[0]

tempSolution = []
finalSolution = []
sumOfTempSolution = 0
sumOfFinalSolution = 0

# Define a function which calculates the number of the rows in the pyramid
# Length of input == 1 + 2 + 3 + ... + rowNum
# Length of input == (1 + rowNum) * rowNum / 2
# According to the quadratic formula: rowNum == ( math.sqrt( 8 * length + 1 ) - 1 ) / 2
def CalculateRowNum(length):
    return (math.sqrt(8*length+1)-1)/2

rowNum = int(CalculateRowNum(len(input)))
print rowNum

# Define a function which finds next child node to go and store the successful path into a solution list
def GoToNext(row, column):
    nodeIndex = row*(row-1)/2 + column
    nodeValue = input[nodeIndex-1]

# If root node is odd, then current node should has the same parity with its row number;
# If root node is even, then current node should has the opposite parity with its row number. 
    if (rootValue%2 != 0 and row%2 == nodeValue%2) or (rootValue%2 == 0 and row%2 != nodeValue%2) :
        tempSolution.append(nodeValue)
        print tempSolution
        if row == rowNum:
            print 'One successful path: ', tempSolution
            CompareSolution(tempSolution)
            tempSolution.pop()
        else:
            GoToNext(row+1, column)
            GoToNext(row+1, column+1)
            tempSolution.pop()
    else:
        print 'Fail at the coordinate: ', row, column

# Define a variable 'sumOfFinalSolution' to store the maximum sum.
# Define a variable 'finalSolution' to store the maximum path.
# Compare sum of a successful solution with stored sum.
def CompareSolution(tempSolution):
    sumOfTempSolution = sum(tempSolution)
    global sumOfFinalSolution
    global finalSolution
    if sumOfTempSolution > sumOfFinalSolution:
        sumOfFinalSolution = sumOfTempSolution
        finalSolution = tempSolution[:]

# Start from root node
GoToNext(1,1)
print 'Final valid path is:', finalSolution, ' The max sum is: ', sumOfFinalSolution
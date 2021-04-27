import numpy as np
import sys

# Program prompts user out of the console for vector 0 and the array
# Prints out the current x vector, Ax matrix, and mu value for each iteration

# class constants for the methods
SPACING = 10
ROUNDTO = 4

# matrix is the matrix/vector
# spaces is the number of digits per entry
# roundedTo is what the decimal is rounded to
def printMatrix(matrix, spaces = SPACING, roundedTo = ROUNDTO):
    for rows in matrix:
        print("|", end = " ")
        for value in rows:
            formattedVal = ("%" + str(spaces) + "." + str(roundedTo) + "f") % (value)
            print(formattedVal, end = " ")
        print("|", end = "")
        print()

# xk is the current vector
# A is the matrix
# mu is the max(abs(value in Ax))
# n is the number of iterations
# k is the current iteration starting from 0
def powerMethod(xk, A, n, k, spaces = SPACING, roundTo = ROUNDTO):
    while (k <= n):
        Axk = np.dot(A, xk)
        mu = max(Axk.min(), Axk.max(), key = abs)
        invMu = 1 / mu
        print("Iteration:", k)
        print("vector x" + str(k))
        printMatrix(xk, spaces, roundTo)
        print("Ax" + str(k))
        printMatrix(Axk, spaces, roundTo)
        print("Mu" + str(k) + ": " + (("%" + str(spaces) + "." + str(roundTo) + "f") % mu))
        xk = (np.dot(invMu, Axk))
        k += 1
        print()

def getMatrix():
    print("Enter your dimensions: ", end = " ")
    dimensions = int(sys.stdin.readline())
    vector = np.zeros((dimensions, 1))
    print()

    print("Enter your vertical matrix (type values in as a row): ", end = " ")
    vectorVals = sys.stdin.readline().split()
    for idx in range(len(vectorVals)):
        vector[idx][0] = vectorVals[idx]
    printMatrix(vector)

    A = np.zeros((dimensions, dimensions))
    print("Enter your matrix (go row by row):")
    for rowIdx in range(dimensions):
        currRow = sys.stdin.readline().split()
        for colIdx in range(len(currRow)):
            A[rowIdx][colIdx] = currRow[colIdx]
    printMatrix(A)
    print()

    return vector, A


# Here just in case you don't want to run the program out of stdin
'''   
x0 = np.array([[1], 
               [0], 
               [0], 
               [0]])

A = np.array([[1, -7, -4, -4],
             [-1, 2, -1, 4],
             [-6, 2, 7, -4],
             [-6, 3, 3, 2]])
'''

vals = getMatrix()
x0 = vals[0]
A = vals[1]

powerMethod(x0, A, 6, 0)


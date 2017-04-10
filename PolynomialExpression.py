import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

####################################################################
# Program: Given a sequence of integers that fit a polynomial
# expression of nth degree, determine the the coefficients of the
# the nth  degree polynomial.
#
# Author: Anirudh Kothapalli
# Year: Summer 2016
####################################################################

def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.show()

def buildMatrix( n=int ):
    theta = np.zeros((n, n))
    for row in range(0, n):
        for col in range(0, n):
            theta[row, col] = (row + 1) ** (n - col - 1)

    return theta

def computeCoefficients(n=int, data=list):
    Y = np.matrix(data).transpose()

    theta = buildMatrix(n+1)

    return inv(theta) * Y

def printPolynomialSeq(poly, n=int):
    print "f(1) = " + np.polyval(poly, 1)

def preparePolynomial(data):
    nterms = data.__len__()
    degree = nterms - 1
    coefficients = computeCoefficients(degree, data)
    poly = ''
    for i in range(nterms-1, 0, -1):
        poly += '(' + str(coefficients[nterms-i-1, 0]) + '*x**' + str(i) + ') + '

    poly += '(' + str(coefficients[-1, 0]) + ')'

    Y = []
    for i in range(0, nterms):
        Y.append(int(round(np.polyval(np.array(coefficients.T)[0], i+1))))

    print
    print "degree     = ", degree
    print "f(x)       = ", poly
    print "f(1)..f(n) = ", Y
    print "Given data = ", data

    return (poly, Y)

def plotData(data, poly):
    n = data.__len__()
    X = [i for i in range(1,n+1)]
    # print "X = ", X

    # fig = plt.figure()
    # points = fig.add_subplot(1,1,1)
    # points.scatter(X, data)
    # graph(poly, range(1,n+1))
    # plt.show()


######################################################################
# This is the main program to find the polynomial expression of a
# a given integer sequence
######################################################################
data = [1, 8, 27, 64]
poly, seq = preparePolynomial(data)
plotData(data, poly)

data = [2, 9, 28, 65]
poly, seq = preparePolynomial(data)
plotData(data, poly)

data = [0, 1, 8, 27]
poly, seq = preparePolynomial(data)
plotData(data, poly)

data = [20, 77, 212, 467]
poly, seq = preparePolynomial(data)
plotData(data, poly)

data = [1, 2, 3, 6, 11, 23, 47, 106, 235]
poly, seq = preparePolynomial(data)
plotData(data, poly)

data = [1, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741]
poly, seq = preparePolynomial(data)
plotData(data, poly)

data = [1, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741, 19320, 48629, 123867, 317955, 823065, 2144505, 5623756, 14828074, 39299897, 104636890, 279793450, 751065460, 2023443032, 5469566585, 14830871802, 40330829030, 109972410221, 300628862480, 823779631721, 2262366343746, 6226306037178]
poly, seq = preparePolynomial(data)
plotData(data, poly)
# print the given list
def printData( theList ):
    print "n = " + str( len(theList) )
    for item in theList:
        print item + " "

# add the numbers in the given array
def sum( theList ):
    result = 0
    for item in theList:
        result += int(item)
    print("Sum: " + str(result))

# This function deteremines if the given list is linear
# or not by computing the first order differences. If the first
# order differences are all same it would be classified as
# a linear list
def isLinear( theList ):
    result = True
    n = len(theList)
    difference = float(theList[1]) - float(theList[0])
    for i in range(1,n):
        if (float(theList[i]) - float(theList[i-1])) != difference:
            result = False
            break
    return result


############################################################
# Main Program
############################################################

# read data from the user
text = raw_input("Enter data: ")

# split the user input (text) into a data array
data = text.split()

printData(data)
sum(data)

if ( isLinear(data) == True):
    print "The data is Linear"
else:
    print "The data not linear"













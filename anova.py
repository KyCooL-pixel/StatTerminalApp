import math

def calculateTotal(list):
    total = 0
    for item in list:
        total += item
    return total

def calculateSSB(totalOfColumns, countOfColumns, intermediateValue):
    return intermediateValue - math.pow(calculateTotal(totalOfColumns),2) / calculateTotal(countOfColumns)

def calculateIntermediateValue(totalOfColumns, countOfColumns):
    answer = 0
    for total,count in zip(totalOfColumns,countOfColumns):
        answer += math.pow(total,2)/count

    return answer

def calculateSSW(matrix, intermediateValue):

    answer = 0

    for column in matrix:
        for row in column:
            answer += math.pow(row, 2)
    
    return answer - intermediateValue

def calculateSST(SSB,SSW):
    return SSB+SSW

def calculateMSB(SSB, k):
    return SSB / (k-1)

def calculateMSW(SSW, n, k):
    return SSW / (n-k)

numberOfColumns = int(input("How many columns are there?"))
numberOfReocrds = 0
matrix = []

for i in range(numberOfColumns):
    temp = []
    numberOfRows = input("How many records (rows) for this column?")
    numberOfRows = int(numberOfRows)
    numberOfReocrds+=numberOfRows
    for j in range(numberOfRows):
        record = int(input("Add a record (row)"))
        temp.append(record)
        
    
    matrix.append(temp)

totalOfColumns = [calculateTotal(item) for item in matrix]
countOfColumns = [len(item) for item in matrix]
intermediateValue = calculateIntermediateValue(totalOfColumns,countOfColumns)

SSB = calculateSSB(totalOfColumns,countOfColumns, intermediateValue)
SSW = calculateSSW(matrix, intermediateValue)
SST = calculateSST(SSB,SSW)
MSB = calculateMSB(SSB, numberOfColumns)
MSW = calculateMSW(SSW, numberOfReocrds, numberOfColumns)
F = MSB / MSW

# print original matrix
for i in matrix:
    line=""
    for j in i:
        line+=f'{j}\t'
    
    print(line)

#print squared matrix
for i in matrix:
    line=""
    for j in i:
        line+=f'{math.pow(j,2)}\t'
    
    print(line)

print(f'SSB= {SSB:.2f}')
print(f'SSW= {SSW:.2f}')
print(f'SST= {SST:.2f}')
print(f'd.f. = ({numberOfColumns-1}, {numberOfReocrds-numberOfColumns})')
print(f'MSB= {MSB:.2f}')
print(f'MSW= {MSW:.2f}')
print(f'F= {F:.2f}')



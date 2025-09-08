#e1

for i in range(1, 11):
    print(i**2)

#e2

myMatrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]

    #prints squared values
for i in myMatrix:
    for x in i:
        print(x**2)


    # prints coords of values
for i in range(3):
    for j in range(3):
        print(i,j)
print(myMatrix)

    #prints coords and squared values
for i in range(3):
    for j in range(3):
        print(f"({i},{j}), {myMatrix[i][j]**2}")
print(myMatrix)

    #squares values inside list (myMatrix) itself
for i in range(3): #bc there are 3 lists in the list
    for j in range(3): # bc there are 3 values in the list
        myMatrix[i][j] **= 2
print(myMatrix)

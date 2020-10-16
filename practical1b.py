X = [[4,7],[8,4],[9,5]]
Y = [[5,3],[8,7],[1,1]]
result = [[0,0],[0,0],[0,0]]
for row in range(len(X)):
   for column in range(len(X[0])):
       result[row][column] = X[row][column] + Y[row][column]
for addition in result:
   print("addition matrix:",addition)


X = [[7,1],[8,4],[9,7]]
Y = [[5,5],[8,7],[1,2]]
result = [[0,0],[0,0],[0,0]]
for row in range(len(X)):
   for column in range(len(X[0])):
       result[row][column] = X[row][column] * Y[row][column]
for addition in result:
   print("maltiplication matrix:",addition)


X = [[3,3],[0 ,7]]
result = [[0,0],[0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for transpose in result:
   print("transpose operration",transpose)

X = [[7],[8],[9]]
Y = [[5],[8],[1]]
result = [[0],[0],[0]]
for row in range(len(X)):
   for column in range(len(X[0])):
       result[row][column] = X[row][column] + Y[row][column]
for addition in result:
   print("addition matrix:",addition)


X = [[7],[8],[9]]
Y = [[5],[8],[1]]
result = [[0],[0],[0]]
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

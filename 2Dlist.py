matrix=[[1,2],[3,4]]
print (matrix[1][0])
print (matrix[0][1])
row=len(matrix)
column=len(matrix[0])
for i in range (row):
    for j in range (column):
        print (matrix[i][j])

matrixA=[[2,4],[10,20]]
matrixB=[[3,6],[20,30]]
Add=[[0,0],[0,0]]
Subtract=[[0,0],[0,0]]
Multiply=[[0,0],[0,0]]
for i in range (row):
    for j in range (column):
        Add[i][j]=matrixA[i][j]+matrixB[i][j]
        Subtract[i][j]=matrixA[i][j]-matrixB[i][j]
        Multiply[i][j]=matrixA[i][j]*matrixB[i][j]
        print (Multiply)
        print (Add)
        print (Subtract)
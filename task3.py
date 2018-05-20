#HardCode Given Matrix ...
Matrix = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
print(Matrix)

print('Given Matrix of 5x5')
for i in range(0,5):
    #for j in range(0,5):
    print(Matrix[i])

# Taking Input ...
rows = int(raw_input('Enter the Number of Rows : '))
cols = int(raw_input('Enter the Number of Columns : '))

matrix_to_be_Search = []
for i in range(0,cols):
    matrix_to_be_Search.append([])

for i in range(0,rows):
    for j in range(0,cols):
        matrix_to_be_Search[i].append(j)
        matrix_to_be_Search[i][j] = 0
print('Enter the Values in (Row x Columns) Sequence : ')
for i in range(0,rows):
    for j in range(0,cols):
        matrix_to_be_Search[i][j] = int(raw_input())

#Displaying the Entered Matrix
print('Your Matrix to be Searched : ')
for i in range(0,2):
    #for j in range(0,5):
    print(matrix_to_be_Search[i])

# Checking for Matrix to be Existed ...
l=0
k=0
rnge = 4

flag = 'false'
for i in range(0,rnge):
    for j in range(0,rnge):
        if matrix_to_be_Search[k][l] == Matrix[i][j]:
            if matrix_to_be_Search[k+1][l] == Matrix[i+1][j]:
                if matrix_to_be_Search[k][l+1] == Matrix[i][j+1]:
                    if matrix_to_be_Search[k+1][l+1] == Matrix[i+1][j+1]:
                        flag = 'true'
if flag == 'true':
    print('YES ! Matrix Exists!')
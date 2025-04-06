def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    else:
        rows = len(a)
        cols = len(b[0])
        c = [[0] * cols for _ in range(rows)]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    
print(matrixmul([[1,2],[2,4]],[[2,1],[3,4]]))
print(matrixmul([[1,2], [2,4]], [[2,1], [3,4], [4,5]]))
print(matrixmul([[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]]))
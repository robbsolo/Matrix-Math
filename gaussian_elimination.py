a = [[3,-2,5,0,2],
     [4,5,8,1,4],
     [1,1,2,1,5],
     [2,7,6,5,7]]

def removeCol(m, nr):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j == nr:
                del m[i][j]

def removeRow(m, nr):
    for i in range(len(m)):
        if i == nr:
            del m[i]

def matrixTranspose(m):
    new = [0] * len(m)
    for i in range(len(m)):
        new[i] = [0] * len(m[0])
    for i in range(len(m)):
        for j in range(len(m[0])):
            new[j][i] = m[i][j]
    return new

def det(m):
    n = len(m)
    if n > 2:
        sum = 0
        for i in range(n):
            temp = [0] * (n-1)
            if i == 0:
                for j in range(1, n):
                    temp[j-1] = []
                    for k in range(1, n):
                        temp[j-1].append(m[j][k])
            elif i == n:
                for j in range(0, n-1):
                    temp[j] = []
                    for k in range(0, n-1):
                        temp[j].append(m[j][k])
            else:
                for j in range(1, n):
                    temp[j-1] = []
                    for k in range(0, n):
                        if k != i:
                            temp[j-1].append(m[j][k])
            #print(temp)
            sum += pow(-1, i) * m[0][i] * det(temp)
        return sum
    else:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def adjMatrix(m):
    t = matrixTranspose(m)
    adj = [0] * len(m)
    for i in range(len(adj)):
        adj[i] = [0] * len(m)
    for i in range(len(t)):
        for j in range(len(t[0])):
            #m2 = t    # This doesn't work... we have to init element by element
            m2 = [0] * len(t)
            for k in range(len(m2)):
                m2[k] = [0] * len(t)
            for k in range(len(t)):
                for z in range(len(t[0])):
                    m2[k][z] = t[k][z]
            removeRow(m2, i)
            removeCol(m2, j)
            c = det(m2) * pow(-1, i + 1 + j + 1)
            adj[i][j] = c
    return adj

def invMatrix(m):
    a = adjMatrix(m)
    inv = [0] * len(m)
    for i in range(len(m)):
        inv[i] = [0] * len(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            inv[i][j] = 1/det(m) * a[i][j]
    return inv

def dot(a, b):
    if isinstance(a, list):
        error = "Matrix multiplication is undefined when number of columns of the first matrix != number of rows of the second matrix."
        result = [0] * len(a)
        for i in range(len(result)):
            if isinstance(b[0], list):
                result[i] = [0] * len(b[0])
            else:
                break
        if len(a[0]) == len(b):
            for i in range(len(a)):
                if isinstance(b[0], list):
                    for j in range(len(b[0])):
                        sum = 0
                        for k in range(len(a[0])):
                            sum += a[i][k] * b[k][j]
                        result[i][j] = sum
                else:
                    sum = 0
                    for k in range(len(a[0])):
                        sum += a[i][k] * b[k]
                    result[i] = sum
            return result
        else:
            return error

def gaussel(a):
    #Elimination
    for k in range(len(a)-1):
        for i in range(k+1, len(a)):
            notZero = True
            for j in range(len(a[0])):
                if a[i][j] != 0:
                    if notZero:
                        temp = a[i][k]
                    a[i][j] = round(a[k][j] - a[i][j] * a[k][k] / temp, 5)
                    notZero = False
    #Back substitution
    b = [0] * len(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j == len(a[i]) - 1:
                b[i] = a[i][j]
                del a[i][j]
    result = dot(invMatrix(a), b)
    print(result)
                
gaussel(a)
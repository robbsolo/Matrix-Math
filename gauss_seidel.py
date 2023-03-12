def tril(m):
    m2 = [0] * len(m)
    for i in range(len(m2)):
        m2[i] = [0] * len(m[0])
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == j:
                m2[i][j] = m[i][j]
            elif j < i:
                m2[i][j] = m[i][j]
    return m2

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

def subtract(A, B):
    a = [0] * len(A)
    for i in range(len(A[0])):
        a[i] = [0] * len(A[0])
    for i in range(len(A)):
        for j in range(len(A[0])):
            a[i][j] = A[i][j] - B[i][j]
    return a

def addVectors(A, B):
    a = [0] * len(A)
    for i in range(len(A)):
        a[i] = A[i] + B[i]
    return a

def add(A, B):
    a = [0] * len(A)
    for i in range(len(A[0])):
        a[i] = [0] * len(A[0])
    if isinstance(B[0], list) == False:
        for i in range(len(A)):
            a[i][0] = A[i][0] + B[i]
            for j in range(1, len(A[0])):
                a[i][j] = A[i][j]
        return a
    else:
        for i in range(len(A)):
            for j in range(len(A[0])):
                a[i][j] = A[i][j] + B[i][j]
        return a

def pieceMult(a, A):
    m = [0] * len(A)
    for i in range(len(A[0])):
        m[i] = [0] * len(A[0])
    for i in range(len(A)):
        for j in range(len(A[0])):
            m[i][j] = a * A[i][j]
    return m

def GaussSeidel(A, B, n):
    L = tril(A)
    U = subtract(A, L)
    
    # First guess
    x = [0,0,0]
    
    for i in range(n):
        print("Iteration", format(i+1))
        x = dot(invMatrix(L), addVectors(dot(pieceMult(-1, U), x), B))
        print(x)

# Example
A = [[3,-1,1],
     [-1,3,-1],
     [1,-1,3]]
B = [-1,7,-7]

# Nr of iterations
n = 3

GaussSeidel(A, B, n)

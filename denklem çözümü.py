def matris(m):
    n=len(m)-1
    x=len(m[0])
    k=0
    a=0
    for i in range(n,-1,-1):
        k=(-m[i][a]/m[a][a])
        for j in range(0,x):
            m[i][j]=k*m[a][j]+m[i][j]
        a+=1

    for i in range(n+1):
        for j in range(x-1,-1,-1):
            m[i][j]=m[i][j]/m[i][i]

    print("cözüm kümesi:")
    for i in range(n+1):
        print(m[i][x-1],end=" ")

denk=[[1,2,1],[3,4,-2]]
matris(denk)
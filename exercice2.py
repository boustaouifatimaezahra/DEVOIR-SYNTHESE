n=int(input('taper le nombre de colone: '))
l=[]
for j in range(1,n):
    ch=' '.join(map(str, str(11 ** j)))
    l.append(ch)
l.reverse()
for i in l:
    print(i)
Mat=[[0]*n for i in range(n)]
for x in range(len(Mat)):
    for i in range(len(Mat[0])):
        Mat[x][i]=1
        break
for x in range(1,len(Mat)):
    for i in range(len(Mat[0])):
        Mat[x][i] = Mat[x-1][i] + Mat[x-1][i-1]
for x in range(len(Mat)):
        for j in range(x+1):
            print(Mat[x][j],end=' ')
        print()
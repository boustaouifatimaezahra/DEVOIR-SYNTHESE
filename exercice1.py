n=int(input("taper le nombre des lettres: "))
while n>20 or n<5:
    n=int(input("taper le nombre des lettres: "))
T1=[]
for i in range(n):
    ch=input(f"taper la lettre {i+1} : ")
    T1.append(ch.upper())
T2=[]
for i in range(n):
    Min=min(T1) 
    for x in range(n):
        if T1[x]==Min:
            Min=T1[x]
            T2.append(Min)
            T1[T1.index(Min)]='_'
            break
for j in range(n):
    T1[j]="*"
print(T1)
print(T2)
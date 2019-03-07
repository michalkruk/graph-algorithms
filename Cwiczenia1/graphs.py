lines = [line.rstrip('\n') for line in open('graph.txt')]
levels = []
matrix = []
edges = []
temp = []
consequent = []
counter = 0
thisdict={}

for i in lines:
    levels.append(i.count('1'))
    matrix.append(i.split(' '))

# Zadanie 1
print("Stopnie kolejnych wiercholkow: ")
for idx, i in enumerate(levels):
    print(idx, i)

# Zadanie 2
print("Wierzcholki o przylegajace do wierzcholka o najwyzszym stopniu: ")
for idx, i in enumerate(max(matrix)):
    if i == '1':
        print(idx)

# Zadanie 3
print("Wypisuje, miedzy jakimi wierzcholkami sa krawedzie: ")
for idx, s in enumerate(matrix):
    for inx, n in enumerate(s):
        if (int(idx) <= int(inx)):
            if (n == '1'):
                edges.append((idx, inx))
print(edges)

# Zadanie 4
w, h = len(matrix), len(edges)
incidentMatrix = [[0 for x in range(w)] for y in range(h)]

print("Wypisuje macierz incydencji: ")
for i in enumerate(edges):
    incidentMatrix[i[0]][i[1][0]]=1
    incidentMatrix[i[0]][i[1][1]]=1
print(incidentMatrix)

# Zadanie 5

print("Wypisuje liste nastepnikow: ")
for idx, i in enumerate(matrix):
    del temp[:]
    for inx, n in enumerate(i):
        if n == '1':
            temp.append(inx)
    thisdict[idx] = temp[:]


print thisdict
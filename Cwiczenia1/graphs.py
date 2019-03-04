

lines = [line.rstrip('\n') for line in open('graph.txt')]
levels = []
matrix = []
counter = 0

for i in lines:
    levels.append(i.count('1'))
    matrix.append(i.split(' '))

print ("Stopnie kolejnych wiercholkow: ")
for idx,i in enumerate(levels):
    print (idx, i)



print ("Wierzcholki o przylegajace do wierzcholka o najwyzszym stopniu: ")
for idx,i in enumerate(max(matrix)):
    if i == '1':
        print (idx)
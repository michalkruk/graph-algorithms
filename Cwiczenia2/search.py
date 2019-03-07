lines = [line.rstrip('\n') for line in open('matrixDFS.txt')]
matrix = []
temp = []
thisdict={}




def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        print vertex
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

for i in lines:
    matrix.append(i.split(' '))

print("Wypisuje liste nastepnikow: ")
for idx, i in enumerate(matrix):
    del temp[:]
    for inx, n in enumerate(i):
        if n == '1':
            temp.append(inx)
    thisdict[idx] = temp[:]



print dfs_iterative(thisdict, 0)

print thisdict
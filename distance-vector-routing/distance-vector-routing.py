number_of_nodes=int(input('enter the number of nodes: '))
nodes=[]
for _ in range(number_of_nodes):
    nodes.append(input('enter name of node: '))
dist_matrix=[]
print('enter -1 if theres no connection')
for i in range(number_of_nodes):
    l=[]
    for j in range(number_of_nodes):
        if i==j:
            l.append(0)
        else:
            val=int(input('enter the cost from '+nodes[i]+' to '+nodes[j]+': '))
            if val==-1:
                l.append('inf')
                continue
            l.append(val)
    dist_matrix.append(l)


print("the current distance matrix is :")

for i in dist_matrix:
    print(i)
    
    
d={}
for start_node in range(len(nodes)):
    for neighbour_node in range(len(nodes)):
        for destination_node in range(len(nodes)):
            if dist_matrix[start_node][neighbour_node]!='inf' and dist_matrix[neighbour_node][destination_node]!='inf':
                if (dist_matrix[start_node][destination_node]=='inf') or (dist_matrix[start_node][neighbour_node]+dist_matrix[neighbour_node][destination_node]<dist_matrix[start_node][destination_node]):
                    dist_matrix[start_node][destination_node]=dist_matrix[start_node][neighbour_node]+dist_matrix[neighbour_node][destination_node]
                    print('updating '+nodes[start_node]+' -> '+nodes[destination_node])
                    print("the current distance matrix is :")
                    for i in dist_matrix:
                        print(i)
print("the new distance matrix is :")

for i in dist_matrix:
    print(i)
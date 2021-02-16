from heapq import heappush, heappop, heapify
import matplotlib as plt
import pylab as p
import networkx as nx
from datetime import datetime

def Adj(i , size):
    adj = []
    for j in range(1,size):
        if (j != i and abs(i - j) <= 3):
            adj.append(j)
    return adj

def Weight(u,v):
    if(u!=v and abs(u-v)<=3):
        return u+v
    return 9999

def dijkstra( N,src , des):

    size = N+1
    G = nx.Graph()
    src = src
    des = des
    Q=[]
    S=[]
    path=[]
    distance=[]
    for i in range (1,size+1):
        distance.insert(i,9999)
        path.append(-1)
        heappush(Q,i)
    distance[src] = 0
    for i in range (1,N):
        G.add_node(i)
    # print(G.nodes())
    while len(Q) != 0:
        u=heappop(Q)
        adjacent=Adj(u,size)
        for v in adjacent:
            if(u<size):
                G.add_edge(u, v,color='black',weight=Weight(u,v))
                alt = distance[u] + Weight(u,v)
                if(alt < distance[v] ):
                    distance[v]=alt
                    path[v]=u
        print("Dis calculation: ",distance)
    x=des
    while x != -1 :
        S.append(x)
        x=path[x]
    distance.pop(0)
    print("Calculated Distance: ", distance)
    for i in range(len(S) - 1):
        if S[+1] is not None:
            G.add_edge(S[i], S[i + 1],color='r')
    pos = nx.shell_layout(G)
    colors = nx.get_edge_attributes(G, 'color').values()
    nx.draw(G, pos, edge_color=colors, with_labels=True)
    p.show()

    return distance,path,S


if __name__ == "__main__":
    N=int(input("How many nodes do you have: "))
    # if(N>20):
    #     print("Too much nodes please enter lower than 20")
    #     N=int(input("How many nodes do you have: "))
    src=int(input("Where is your source destination:"))
    des=int(input("Where is your target destination: "))
    startTime=datetime.now()
    distances, path,S =dijkstra(N,src,des)
    print("Distances are: ", distances)
    print("Path distance is: ", distances[des-1])
    print("Path is",S)
    finishTime=datetime.now()
    print("N= " ,N )
    print('Duration: ', format(finishTime-startTime))





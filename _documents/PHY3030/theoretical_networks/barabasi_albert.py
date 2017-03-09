# -*- coding: utf-8 -*-
"""
PHY3030 - Projet de fin d etudes

Modele de Barabasi-Albert

Patrice Bechard

Hiver 2017
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import time

start=time.time()

G=nx.Graph()

N0=2

N=10000               #final number of nodes

G.add_nodes_from([i for i in range(N0)])
G.add_edge(0,1)                         #we create the starting nodes

for i in range(N0,N):
    node_deg=[G.degree(j)for j in range(i)]
    sum_deg=sum(node_deg)
    G.add_node(i)
    for j in range(i):
        prob=node_deg[j]/sum_deg
        if random.random()<prob:
            G.add_edge(i,j)

print("Number of nodes",G.number_of_nodes())
print("Number of edges",G.number_of_edges())

nx.write_gexf(G,'/users/user/network/barabasi_albert_%d.gexf'%N)

print("elapsed : ",time.time()-start)
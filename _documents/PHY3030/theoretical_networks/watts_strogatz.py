# -*- coding: utf-8 -*-
"""
PHY3030 - Projet de fin d etudes

Modele de Watts-Strogatz

Patrice Bechard

Hiver 2017
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import time

start=time.time()

G=nx.Graph()                        #initialization of graph

N=10000                                #number of nodes
p=np.linspace(0,1,10)               #prob of re-wiring
for prob in p:
    
    G.add_nodes_from([i for i in range(N)])

    for i in range(G.number_of_nodes()):        #initialization of links
        if i==0:
            G.add_edge(G.number_of_nodes()-1,0)
            G.add_edge(G.number_of_nodes()-2,0)
        elif i==1:
            G.add_edge(0,1)
            G.add_edge(G.number_of_nodes()-1,1)
        else:
            G.add_edge(i-1,i)
            G.add_edge(i-2,i)

    for i in range(G.number_of_nodes()):        #re-wiring
        if random.random()<prob:
            if i==0:
                G.remove_edge(G.number_of_nodes()-1,0)
            else:
                G.remove_edge(i-1,i)
            G.add_edge(i,random.randrange(G.number_of_nodes()))
        if random.random()<prob:
            if i==0:
                G.remove_edge(G.number_of_nodes()-2,0)
            elif i==1:
                G.remove_edge(G.number_of_nodes()-1,1)
            else:
                G.remove_edge(i-2,i)
            G.add_edge(i,random.randrange(G.number_of_nodes()))
    
    print("Number of nodes",G.number_of_nodes())
    print("Number of edges",G.number_of_edges())

    nx.write_gexf(G,'/users/user/network/watts_strogatz_%d_%d.gexf'%(N,prob*100))
    G.clear()

print("elapsed : ",time.time()-start)
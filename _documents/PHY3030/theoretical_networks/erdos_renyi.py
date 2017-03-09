# -*- coding: utf-8 -*-
"""
PHY3030 - Projet de fin d etudes

Modele de Erdos-Renyi

Patrice Bechard

Hiver 2017
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import numpy as np

start=time.time()

G=nx.Graph()        #initialize graph

N=10000               #number of nodes
p=np.linspace(0.05,0.5,10)
for prob in p:
    G.add_nodes_from([i for i in range(N)])

    for i in range(G.number_of_nodes()):        #if random number < threshold, new link
        for j in range(i,G.number_of_nodes()):
            if random.random()<prob:
                G.add_edge(i,j)
            
    print("Number of nodes",G.number_of_nodes())
    print("Number of edges",G.number_of_edges())

    nx.write_gexf(G,'/users/user/network/erdos_renyi_%d_%d.gexf'%(N,prob*100))
    
    G.clear()

print("elapsed : ",time.time()-start)
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:32:21 2017

@author: Patrice
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

'''
G=nx.Graph()
G.add_nodes_from([x for x in range(100)])
for i in range(0,100,8):
    G.add_edges_from([(i,x) for x in range(0,100,7)])
nx.draw_spectral(G)
plt.show()
'''


def g(t0,u):
    A,B=1.,3.
    gX=A-(B+1.0)*u[0]+u[0]**2*u[1]      #eq 1.39 RHS
    gY=B*u[0]-u[0]**2*u[1]              #eq 1.40 rhs
    eval=np.array([gX,gY])              #vecteurs rhs pentes
    return eval
    
def rk(h,t0,uu):
    g1=g(t0,uu)     #1.15
    g2=g(t0+h/2.,uu+h*g1/2.)    #1.16
    g3=g(t0+h/2.,uu+h*g2/2.)    #1.17
    g4=g(t0+h,uu+h*g3)          #1.18
    unew=uu+h/6.*(g1+2.*g2+2.*g3+g4)    #1.19
    return unew

nMax=1000           #nbre pas de temps max
eps=1.e-5           #tolerance
tfin=10.            #duree de l'integration
t=np.zeros(nMax)    #pour le temps
u=np.zeros([nMax,2])#tab solutions
u[0,:]=np.array([3.,3.])   #conditions initiales ??
nn=0                    #compteur d'iterations temporelles set a 0
h=0.1                   #pas initial
while(t[nn]<tfin)and(nn<nMax):
    u1=rk(h,t[nn],u[nn,:])  #pas pleine longueur
    u2a=rk(h/2., t[nn],u[nn,:]) #demi pas
    u2=rk(h/2.,t[nn],u[nn,:])   #deuxieme
    delta=max(abs(u2[0]-u1[0]),abs(u2[1]-u1[1]))   #eqn 1.42
    if delta>eps:
        h/=1.5          #on rejette et reduction de pas
    else:
        nn+=1
        t[nn]=t[nn-1]+h
        u[nn,:]=u2[:]
        if delta<=eps/2.:
            h*=1.5
    print("{0},t {1}, X {2}, Y {3}".format(nn,t[nn],u[nn,0],u[nn,1]))
    
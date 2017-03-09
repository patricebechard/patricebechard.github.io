'''
Visualizes and analyzes social networks
Takes input data from Lost Circles for Facebook networks
'''
import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.misc import factorial
plt.style.use('patrice')

"""
Types :

    0 : with main hub
    1 : without main hub
    2 : physics cluster
    3 : gatineau cluster
"""
type=0

def new_network():
    g = nx.Graph()
    return g

def build_facebook_net():
    fbg = new_network()

    file_path = '/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/facebook_friends/patrice_bechard.json'

    #Read data as dict and drop unnecessary elements
    with open(file_path) as json_data:
        data = json.load(json_data)
    data.pop('userName')
    data.pop('userId')

    fromList = []
    toList = []

    #Add connections between your friends
    for i in data['links']:
        fromList.append(i['source'])
        toList.append(i['target'])
    if type == 0:
        #Add connections between you and your friends
        for i in range(0, len(data['nodes'])):
            fromList.append(0)  #Let 0 be your node Id
            toList.append(i+1)
        
        #Populate nodes for everyone in your network plus yourself
        for i in range(0, len(data['nodes'])+1):
            fbg.add_node(i, label=i)
    else:
        #Populate nodes for everyone in your network plus yourself
        for i in range(0, len(data['nodes'])):
            fbg.add_node(i, label=i)        
        
    #Populate edges for all connections in your network
    for i in range(0, len(fromList)):
        fbg.add_edge(fromList[i], toList[i], key=i)

    return fbg
    
def degree_distribution(G,degree):
    degree_distr=np.zeros((max(degree)//5)+1)
    for i in degree:
        degree_distr[i//5]+=1
    for i in range(len(degree_distr)):
        degree_distr[i]=degree_distr[i]/len(degree)
    if round(max(degree),-1)<round(max(degree)):
        upper=round(max(degree),-1)+2.5
    else:
        upper=round(max(degree),-1)-2.5
    domain=np.linspace(2.5,upper,(max(degree)//5)+1)    #each point is for 5 degrees
    
    plt.loglog(domain,degree_distr,'.')
    
    meandeg=2*G.size()/G.order()
    
    plt.xlabel(r'k')
    plt.ylabel(r'$p_k$')
    if type==0:
        plt.savefig('with/with_degree.png')
    elif type==1:
        plt.savefig('without/without_degree.png')
    plt.show()

def distance(G):
    """Barabasi eq. 2.14"""
    sum=0
    numNoPath=0
    dist_distr=[]
    for i in range(G.order()):
        if i%100==0:print(i)
        for j in range(G.order()):
            if i!=j:
                try:
                    short_path=nx.shortest_path_length(G,source=i,target=j)
                    sum+=short_path
                    dist_distr+=[short_path]
                except nx.NetworkXNoPath:
                    numNoPath+=1
                    pass
    denom=G.order()*(G.order()-1)-numNoPath
    meandist=(1/denom)*sum
    diameter=max(dist_distr)
    weights=np.ones(len(dist_distr))/len(dist_distr)
    n,bins,patches=plt.hist(dist_distr,weights=weights)
    plt.xlabel(r'$d_{ij}$')
    plt.ylabel(r'$p_{d}$')
    plt.text(1, max(n)*0.9, r'$\langle d \rangle = %.2f$'%meandist,fontsize=15)
    plt.text(1, max(n)*0.8, r'$d_{max} = %d$'%diameter, fontsize=15)
    
    if type==0:
        plt.savefig('with/with_distance.png')
    elif type==1:
        plt.savefig('without/without_distance.png')

    else:
        raise Exception('Type is invalid')
    plt.show()
    return
    
#--------------------------Main------------------------------
for type in range(2):
    facebook_net = build_facebook_net()

    degree=[]
    for i in range(facebook_net.number_of_nodes()):
        degree.append(facebook_net.degree(i))

    degree_distribution(G,degree)

    distance(facebook_net)
    #Export data for use in Gephi
    if type==0:
        nx.write_gexf(facebook_net, "with/facebook_network_with.gexf")
    elif type==1:
        nx.write_gexf(facebook_net, "without/facebook_network_without.gexf")

"""
#Degree centrality top 10
deg = nx.degree(facebook_net)
deg_sorted = sorted(deg.items(), key=operator.itemgetter(1), reverse=True)
print("Top 10 degree centrality (node, centrality): ", deg_sorted[0:9])
#Closeness centrality top 10
clo = nx.closeness_centrality(facebook_net)
clo_sorted = sorted(clo.items(), key=operator.itemgetter(1), reverse=True)
print("Top 10 closeness centrality (node, centrality): ", clo_sorted[0:9])
#Betweenness centrality top 10
bet = nx.betweenness_centrality(facebook_net)
bet_sorted = sorted(bet.items(), key=operator.itemgetter(1), reverse=True)
print("Top 10 betweenness centrality (node, centrality): ", bet_sorted[0:9])
#Eigenvector centrality top 10
eig = nx.eigenvector_centrality(facebook_net)
eig_sorted = sorted(eig.items(), key=operator.itemgetter(1), reverse=True)
print("Top 10 eigenvector centrality (node, centrality): ", eig_sorted[0:9])
#Pagerank centrality top 10
pag = nx.pagerank(facebook_net)
pag_sorted = sorted(pag.items(), key=operator.itemgetter(1), reverse=True)
print("Top 10 pagerank centrality (node, centrality): ", pag_sorted[0:9])

#Trim network to only show nodes with more than 1 connection
facebook_net_trimmed = facebook_net.copy()
for n in facebook_net_trimmed.nodes():
    if deg[n] < 2:
        facebook_net_trimmed.remove_node(n)

#View all cliques
cliques = list(nx.find_cliques(facebook_net_trimmed))
print("Cliques:")
for c in cliques:
    print(c)
"""
"""
#Plot Facebook network
nx.draw_random(facebook_net)
plt.show()

"""

# -*- coding: utf-8 -*-
"""
Network Mapping

Patrice Bechard

jan 21 2017
"""
#--------------------------Modules---------------------------
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time
plt.style.use('patrice')

print("Execution Start Time :",time.asctime())
global start
start=time.time()            #time starts at beginning of execution
#-------------------------Header-----------------------------
"""
types
0: all (phys, lps and exoplanetes)
1: phys.umontreal.ca
2: exoplanetes.umontreal.ca
3: lps.umontreal.ca
4: craq-astro.ca

"""
type=2                  

#---------------------------Functions------------------------
def look_for_duplicates():
    if type==0:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/all/list_of_urls_all.txt')
    elif type ==1:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/phys/list_of_urls_phys.txt')
    elif type==2:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/exoplanetes/list_of_urls_exoplanetes.txt')
    elif type==3:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/lps/list_of_urls_lps.txt')
    elif type==4:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/craq/list_of_urls_craq.txt')
    else:
        raise Exception('Type is invalid')

    allURL=[]

    for lines in f:    
        x=lines[0]
        while x != 'h':
            lines=lines[1:]
            x=lines[0]
        allURL.append(lines)

    for i in range(len(allURL)):
        for j in range(i+1,len(allURL)):
            if allURL[i]==allURL[j]:
                print(allURL[i])
                print('ERROR')
                raise Exception('Duplicates in links file')

def map_network():
    
    if type==0:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/all/fileLinks_all.txt')
        numNodes=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/all/numberNodes_all.txt','r')
    elif type ==1:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/phys/fileLinks_phys.txt')
        numNodes=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/phys/numberNodes_phys.txt','r')
    elif type==2:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/exoplanetes/fileLinks_exoplanetes.txt')
        numNodes=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/exoplanetes/numberNodes_exoplanetes.txt','r')
    elif type==3:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/lps/fileLinks_lps.txt')
        numNodes=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/lps/numberNodes_lps.txt','r')
    elif type==4:
        f=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/craq/fileLinks_craq.txt')
        numNodes=open('/Users/user/Desktop/Ecole/Hiver_2017_PHY/PHY3030-Projet_de_fin_d_etudes/04_Codes/map_the_web/craq/numberNodes_craq.txt','r')

    else:
        raise Exception('Type is invalid')
        
    numNodes=numNodes.readline()           #number of nodes in network
    numNodes=int(numNodes)

    G=nx.DiGraph()
    G.add_nodes_from([x for x in range(numNodes)])
    degree=[]

    for i in range(numNodes):
        Links=f.readline()
        #if count >4:
        #    sys.exit()
        Links=Links[1:-2]                       #get rid of [ at beginning and ]\n at the end
        Links=Links.split(", ")                 #split into list of int  
        try:
            if Links[0]=='':
                degree.append(0)
                continue
            for j in range(len(Links)):
                Links[j]=int(Links[j])         
            degree.append(len(Links))
        except:
            print('FUCK')
            print(len(Links))
            print(Links)
            raise Exception
            pass
        for j in range(len(Links)):
            G.add_edge(i,j)   
    return G,degree

def degree_distribution(degree):
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
    plt.xlabel(r'k')
    plt.ylabel(r'$p_k$')
    if type==0:
        plt.savefig('all/degree_distribution_all.png')
    elif type==1:
        plt.savefig('phys/degree_distribution_phys.png')
    elif type==2:
        plt.savefig('exoplanetes/degree_distribution_exoplanetes.png')
    elif type==3:
        plt.savefig('lps/degree_distribution_lps.png')
    elif type==4:
        plt.savefig('craq/degree_distribution_craq.png')
    else:
        raise Exception("Type is invalid")
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
    norm=G.order()*(G.order()-1)-numNoPath
    meandist=(1/norm)*sum
    diameter=max(dist_distr)
    weights=np.ones(len(dist_distr))/len(dist_distr)
    n,bins,patches=plt.hist(dist_distr,weights=weights)
    plt.xlabel(r'$d_{ij}$')
    plt.ylabel(r'Count')
    plt.text(1, max(n)*0.9, r'$\langle d \rangle = %.2f$'%meandist,fontsize=15)
    plt.text(1, max(n)*0.8, r'$d_{max} = %d$'%diameter, fontsize=15)
    
    if type==0:
        plt.savefig('all/all_distance.png')
    elif type==1:
        plt.savefig('phys/phys_distance.png')
    elif type==2:
        plt.savefig('exoplanetes/exoplanetes_distance.png')
    elif type==3:
        plt.savefig('lps/lps_distance.png')
    elif type==4:
        plt.savefig('craq/craq_distance.png')
    else:
        raise Exception('Type is invalid')
    plt.show()
    return

def save_gexf(G):
    if type==0:
        nx.write_gexf(G,'all/all.gexf')
    elif type==1:
        nx.write_gexf(G,'phys/phys.gexf')
    elif type==2:
        nx.write_gexf(G,'exoplanetes/exoplanetes.gexf')
    elif type==3:
        nx.write_gexf(G,'lps/lps.gexf')
    elif type==4:
        nx.write_gexf(G,'craq/craq.gexf')
    else:
        raise Exception('Type is invalid')

#----------------------Main----------------------------------

for type in range(5):
    type=4
    look_for_duplicates()
    G,degree=map_network()

    distance(G)
    degree_distribution(degree)    
#save_gexf(G)

totaltime=time.time()-start
print("Total time : %d h %d m %d s"%(totaltime//3600,(totaltime//60)%60,totaltime%60))
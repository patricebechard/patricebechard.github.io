# -*- coding: utf-8 -*-
"""
Crawler

PHY3030 - Projet de fin d'études
Network Science

Patrice Béchard
janvier 2017


CODE EDITED FROM : http://www.netinstructions.com/how-to-make-a-web-crawler-in-under-50-lines-of-python-code/
"""

#----------------------------------MODULES-----------------------------
from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
from retrying import retry

#-------------------------CLASSES-----------------------------------

class TimeError(Exception):
    """Algorithm has stalled"""
    pass

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):
    
    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        # We are looking for the begining of a link. Links normally look
        # like <a href="www.someurl.com"></a>
        if tag == 'base':
            for (key,value) in attrs:
                if key == 'href':
                    self.baseUrl=value
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # We are grabbing the new URL. We are also adding the
                    # base URL to it. For example:
                    # www.netinstructions.com is the base and
                    # somepage.html is the new URL (a relative URL)
                    #
                    # We combine a relative URL with the base URL to create
                    # an absolute URL like:
                    # www.netinstructions.com/somepage.html
                    for i in range(len(value)-6):
                        if value[i:i+6]=='mailto':
                           value=''
                    newUrl = parse.urljoin(self.baseUrl, value)
                    if umontreal(newUrl)==True:
                    # And add it to our colection of links:
                        self.links = self.links + [newUrl]

    # This is a new function that we are creating to get links
    # that our spider() function will call
    def getLinks(self, url):
        self.links = []
        # Remember the base URL which will be important when creating
        # absolute URLs
        self.baseUrl=url
        # Use the urlopen function from the standard Python 3 library
        
        response=try_reading_response(url)

        # Make sure that we are looking at HTML and not other things that
        # are floating around on the internet (such as
        # JavaScript files, CSS, or .PDFs for example)
        #if response.getheader('Content-Type')=='text/html':
        try:
            htmlBytes = response.read()
            # Note that feed() handles Strings well, but not bytes
            # (A change from Python 2.x to Python 3.x)
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        #else:
        except:
            return "",[]

#------------------------------FUNCTIONS---------------------------------
def umontreal(url):
    """We limit our search to this domain only"""
    for i in range(len(url)):   
        if url[i:i+13]=='craq-astro.ca':
            return True
    return False         
    
def delete_duplicates(links,reference,addindex=0):
    """We make sure we delete as much junk as possible from the link list"""
    indexLinks=0
    listPointing=[]
    for i in links:
        indexRef=0
        try:
            for j in reference:
                if i==j:            #if link is in reference
                    listPointing+=[indexRef+addindex]   #page points to referenced item      
                    links=links[:indexLinks]+links[indexLinks+1:]   #delete referenced item from links
                    raise Exception
                else:
                    indexRef+=1
            indexLinks+=1
        except:
            pass
    return listPointing,links

                    
    
@retry(stop_max_delay=010)            #wait max 10 seconds
def try_reading_response(url):
    """"""
    response = urlopen(url)
    return response       
    raise TimeError("Error, time is too long")

# And finally here is our spider. It takes in an URL, a word to find,
# and the number of pages to search through before giving up
def crawler(url, maxPages):  
    f=open('list_of_urls.txt','w')
    fileLinks=open('fileLinks.txt','w') 
    numberNodes=open('numberNodes.txt','w') #total number of nodes (easier for plotting)
    maxNodes=1                  #node for url
    pagesToVisit = [url]        #in queue to be visited
    pagesVisited=[]             #we already visited them
    
    # The main loop. Create a LinkParser and get all the links on the page.
    # Also search the page for the word or string
    # In our getLinks function we return the web page
    # (this is useful for searching for the word)
    # and we return a set of links from that web page
    # (this is useful for where to go next)
    while (len(pagesVisited)+1) < maxPages and pagesToVisit != []:  #still things to visit and under the limit
        print("maxNodes : ",maxNodes)
        pointingTo=[]         #pages where the current node points
        # Start from the beginning of our collection of pages to visit:
        while url in pagesVisited:          #making sure we haven't went to this page
            if pagesToVisit==[]: break
            url=pagesToVisit[0]
            pagesToVisit=pagesToVisit[1:]
        f.write('{0}{1}{2}'.format(len(pagesVisited)+1,url,'\n')) #writing the list of site we've already visited
        try:
#        if True:    
            print(len(pagesVisited)+1, url)
            parser = LinkParser()
            data, links = parser.getLinks(url)
            links=list(set(links))      #removing duplicates 
            
            newPointing,links=delete_duplicates(links,pagesVisited) 
            pointingTo+=newPointing
            newPointing,links=delete_duplicates(links,pagesToVisit,len(pagesVisited))
            pointingTo+=newPointing
            
            #at this point, elems in links are only new links

            #add the remaining links to the list of items where the node points

            pointingTo+=[x for x in range(maxNodes,maxNodes+len(links))]
            maxNodes+=len(links)            #update maxNodes

            # Add the pages that we visited to the end of our collection
            # of pages to visit:
            pagesToVisit = pagesToVisit + links
            fileLinks.write(str(pointingTo)) 
            fileLinks.write('\n')
            pagesVisited+=[url]
            print(maxNodes,len(pagesVisited)+len(pagesToVisit))
            #print('***',len(pagesToVisit),len(list(set(pagesToVisit))))

        except :
            print(" **Failed!**")
            if pagesToVisit==[]: break
            url=pagesToVisit[0]
            pagesToVisit=pagesToVisit[1:]
            
            
    if pagesToVisit==[]:
        print('pagesToVisit is empty!')        
    print('Nombre de pages visitées : %d'%(len(pagesVisited)))
    print('Nombre de pages toujours en file : %d'%len(pagesToVisit))  
    numberNodes.write(str(maxNodes))
    return 

#---------------------------------MAIN----------------------------------
crawler('http://craq-astro.ca/',100000)

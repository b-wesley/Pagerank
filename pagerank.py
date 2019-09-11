class Graph:
    def __init__(self, nodes, df):
        self.nodes = nodes #list of nodes in the graph
        self.df = df #damping factor
        self.numNodes = len(self.nodes)
        self.initialRank = 1/self.numNodes

    #update the pagerank of a single node
    def updateRank(self, node):
        linkerList = [] * self.numNodes
        for n in self.nodes: #create a list of nodes that link to the node being calculated
                if n.linksTo(node):
                        linkerList.append(n)
        #calculate page rank formula for the node
        return ((1 - self.df) / float(self.numNodes)) + (self.df * self.sumPR(linkerList))

    #return sum of the nlist's pageranks divided by # of the given node's out-links    
    def sumPR(self, nodelist):
        total = 0
        for n in nodelist:
            total += (n.pageRank / float(n.numLinks))
        return total

    #update each node's rank
    def updateAllRanks(self):
        newRanks = []*self.numNodes
        for n in self.nodes:
                newRanks.append(self.updateRank(n))
        self.setRanks(newRanks)

    #set the new rank of each node
    def setRanks(self, newRanks):
        i = 0
        for n in self.nodes:
            n.pageRank = newRanks[i]
            i+=1
            
    #print each node's rank        
    def printRanks(self):
        tot = 0
        for n in self.nodes:
            print(n.pageRank)
            tot += n.pageRank
        print('total: '+ str(tot))
        
        
class Node:
    def __init__(self, graph):
        self.graph = graph #the graph containing the node
        
        self.links = None #outgoing edges, expressed as destination node
        self.pageRank = graph.initialRank
        self.numLinks = None

    #check if this node links to the other node
    def linksTo(self, other):
        return other in self.links

    #set the page rank to the new rank
    def setRank(newRank):
        self.pageRank = newRank

    #set the list of nodes this node links to, update the number of links
    def setLinks(self,newLinks):
        self.links = newLinks
        self.numLinks = len(self.links)

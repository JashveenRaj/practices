import operator
import networkx as nx
import random
import matplotlib.pyplot as plt

G=nx.gnp_random_graph(10,0.5,directed=True) # produced random graph and every node is "directed" randomly
nx.draw(G,with_labels=True) # draws graph(G) and gives label(num)
plt.show()

#for page ranking method we choose a random node and do drunkards walk
#if the node reached and it doesn't have other node director then we choose random node again.

#to pick random node
x=random.choice([i for i in range (G.number_of_nodes)])

#to store the no of count of node visits we create an dictionary
dict_counter={}
#initialising no of count to zero in dictionary
for i in range (G.number_of_nodes()):
    dict_counter[i]=0

#count of source node
dict_counter[x]=dict_counter[x]+1

#iterating transverse from node to node
for i in range(10000000):  #use large iterations for accurate results  
    list_n=list(G.neighbours(x)) # to take a list of neighbouring nodes
    if(len(list_n==0)):    #if the node we ended up is an sink(no more nodes to go to)
      x=random.choice([i for i in range (G.number_of_nodes)]) #new node is chosen
      dict_counter[x]=dict_counter[x]+1 
    else:
       x=random.choice(list_n)
       dict_counter[x]=dict_counter[x]+1

#to verify the result we use builtin 'pagerank' function to check our result
p=nx.pagerank
#to sort dictionary
sorted_p= sorted(p.items, key=operator.itemgetter(1))  #here to sort on basis of values-1 // for basis of keys=0
sorted_rw = sorted(dict_counter.items(),key=operator.itemgetter(1))
print(sorted_p)
print(sorted_rw)




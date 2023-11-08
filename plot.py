import networkx as nx
import matplotlib.pyplot as plt


G=nx.barbell_graph(4,2)
nx.draw(G)

plt.show()

#there are several types : wheel complete path cycle etc,....
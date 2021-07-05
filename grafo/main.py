import pandas as pd

def isNaN(num):
    return num != num

#------------------------------------------------
#------------------------------------------------

df = pd.read_csv("./data/matriz_distancia.csv", sep=";", skip_blank_lines=False)

data = []

val_map = {}

cont_fila = 0
for fila, columna in df.iterrows():
    cont_columna = 0
    if cont_fila>0:
        for i in range(len(columna)):
            if cont_columna>0 and cont_fila>0:
                if columna[i]!=-1 and columna[i]!=0 and (cont_columna-1)>0:
                    data.append(tuple([str(cont_fila), str((cont_columna-1))]))
                    if ((cont_columna-1)%2) == 0:
                        val_map[str((cont_columna-1))] = 100;

            cont_columna = cont_columna + 1

    cont_fila = cont_fila + 1

print(data)
print(val_map)

#------------------------------------------------
#------------------------------------------------


import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import show

G = nx.DiGraph()
G.add_edges_from(data)


values = [val_map.get(node, 0.5) for node in G.nodes()]

# marcar camino optimo
red_edges = []

edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)

# plt.show()
show()















#------------------------------------------------
#------------------------------------------------

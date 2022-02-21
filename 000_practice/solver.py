from copy import deepcopy

from dataparser import Data
import numpy as np
import networkx as nx

def solve(data: Data):
    G = deepcopy(data.graph)
    degress = [v[1] for v in list(G.degree([i for i in range(data.num_customers)]))]
    degress_index = np.argsort(degress)
    max_clique = []
    for curr_index in range(len(degress_index)):
        d_index = degress_index[curr_index]
        if d_index in max_clique:
            continue
        if not G.has_node(d_index):
            continue
        max_clique.append(d_index)
        neighbour_list = list(G.neighbors(d_index))
        for n in neighbour_list:
            if G.has_node(n):
                G.remove_node(n)

        for el in list(G.degree([i for i in range(data.num_customers)])):
            degress[el[0]] = el[1]
        degress_index = np.argsort(degress)
        curr_index == 0

    print(f'Len Max Set: {len(max_clique)}')
    max_ind = nx.algorithms.mis.maximal_independent_set(data.graph, max_clique)
    print(f'Len Max Ind: {len(max_ind)}')
    best_indexes = list(max_ind)
    on_pizza = []
    for i in best_indexes:
        on_pizza += data.likes[i]
    on_pizza = list(set(on_pizza))
    data.on_pizza = on_pizza
    data.generate_current_customers()

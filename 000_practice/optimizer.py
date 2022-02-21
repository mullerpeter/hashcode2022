from dataparser import Data
import networkx as nx
from tqdm import tqdm
import random


def run_optimisation(data: Data, num_steps=10):
    pbar = tqdm(range(num_steps))
    for i in pbar:
        new_ind = random.choices(data.current_customers, k=100)
        new_customers = list(data.current_customers)
        for ind in new_ind:
            if ind in new_customers:
                new_customers.remove(ind)
        new_max_ind = nx.algorithms.mis.maximal_independent_set(data.graph, new_customers)
        pbar.set_postfix(score=len(new_max_ind))
        if len(new_max_ind) >= len(data.current_customers):
            best_indexes = list(new_max_ind)
            on_pizza = []
            for i in best_indexes:
                on_pizza += data.likes[i]
            on_pizza = list(set(on_pizza))
            data.on_pizza = on_pizza
            data.generate_current_customers()
            data.write_if_best(score=len(new_max_ind))

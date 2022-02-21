import networkx as nx
import json
import os


def check_create_directory(path):
    # Check whether the specified path exists or not
    exists = os.path.exists(path)
    if not exists:
        # Create a new directory because it does not exist
        os.makedirs(path)

def read_input_file(filename):
    file1 = open(filename, 'r')
    likes = []
    hates = []
    c = int(file1.readline())
    for _ in range(c):
        line = file1.readline().split()
        likes.append(line[1:])
        line = file1.readline().split()
        hates.append(line[1:])

    return likes, hates


def read_output_file(filename):
    file1 = open(filename, 'r')
    return file1.readline().split()[1:]


class Data:
    def __init__(self, task_name):
        super(Data, self).__init__()
        self.task_name = task_name

        self.likes, self.hates = read_input_file(f'input_data/{task_name}.in.txt')
        self.on_pizza = []
        self.current_customers = []
        self.num_customers = len(self.likes)
        self.graph = self.create_graph()

    def generate_current_customers(self):
        self.current_customers = []
        for i in range(self.num_customers):
            if all(x in self.on_pizza for x in self.likes[i]) and all(x not in self.on_pizza for x in self.hates[i]):
                self.current_customers.append(i)

    def load_best_solution(self):
        self.on_pizza = read_output_file(f'submission/{self.task_name}.out.txt')
        self.generate_current_customers()

    def get_best_score(self):
        with open("best_scores.json") as json_file:
            json_object = json.load(json_file)
            json_file.close()

        if self.task_name in json_object:
            return json_object[self.task_name]

        return 0

    def create_graph(self):
        G = nx.Graph()
        G.add_nodes_from([i for i in range(self.num_customers)])
        for i1 in range(self.num_customers):
            for i2 in range(i1 + 1, self.num_customers):
                all_good = True
                for hate_i in self.hates[i1]:
                    if hate_i in self.likes[i2]:
                        all_good = False
                        break
                for hate_i in self.hates[i2]:
                    if hate_i in self.likes[i1]:
                        all_good = False
                        break
                if not all_good:
                    G.add_edge(i1, i2)
        return G

    def write_if_best(self, score):
        current_best = self.get_best_score()
        if score > current_best:
            print(f'Improved Score on {self.task_name}: {score} - (Prev.: {current_best})')
            self.write_solution()
            with open("best_scores.json", "r+") as json_file:
                data = json.load(json_file)

                data[self.task_name] = score

                json_file.seek(0)  # rewind
                json.dump(data, json_file)
                json_file.truncate()

        check_create_directory(f'runs/{self.task_name}')
        self.write_solution(path=f'runs/{self.task_name}/{score}.out.txt')

    def write_solution(self, path=None):
        if path is None:
            path = f'submission/{self.task_name}.out.txt'
        out_file = open(path, "w")
        out_file.write(str(len(self.on_pizza)))
        for element in self.on_pizza:
            out_file.write(" " + element)
        out_file.close()

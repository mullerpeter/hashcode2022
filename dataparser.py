import json
import os


def check_create_directory(path):
    # Check whether the specified path exists or not
    exists = os.path.exists(path)
    if not exists:
        # Create a new directory because it does not exist
        os.makedirs(path)

def read_input_file(filename):
    # TODO: Implement Input File Parsing
    file1 = open(filename, 'r')
    something = []
    c = int(file1.readline())
    for _ in range(c):
        line = file1.readline().split()
        something.append(line)

    return something


def read_output_file(filename):
    # TODO: Implement Output File Parsing
    file1 = open(filename, 'r')
    return file1.readline().split()[1:]


class Data:
    def __init__(self, task_name):
        super(Data, self).__init__()
        self.task_name = task_name

        self.something = read_input_file(f'input_data/{task_name}.in.txt')

    def load_best_solution(self):
        self.something = read_output_file(f'submission/{self.task_name}.out.txt')

    def get_best_score(self):
        with open("best_scores.json") as json_file:
            json_object = json.load(json_file)
            json_file.close()

        if self.task_name in json_object:
            return json_object[self.task_name]

        return 0

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
        # TODO: Implement Output File Writing
        if path is None:
            path = f'submission/{self.task_name}.out.txt'
        out_file = open(path, "w")
        out_file.write("Something")
        out_file.close()

import json
import os
import numpy as np


class Skill:
    def __init__(self, name, level):
        super(Skill, self).__init__()
        self.name = name
        self.level = level


class Role:
    def __init__(self, name, level):
        super(Role, self).__init__()
        self.name = name
        self.skill_index = None
        self.level = level
        self.assigned = None


class Contributor:
    def __init__(self, name, N):
        super(Contributor, self).__init__()
        self.name = name
        self.N = N
        self.skills = []


class Project:
    def __init__(self, name, D, S, B, R):
        super(Project, self).__init__()
        self.name = name
        self.D = D
        self.S = S
        self.B = B
        self.R = R
        self.roles = []

def check_create_directory(path):
    # Check whether the specified path exists or not
    exists = os.path.exists(path)
    if not exists:
        # Create a new directory because it does not exist
        os.makedirs(path)

def read_input_file(filename):
    file1 = open(filename, 'r')
    cp_line = file1.readline().split()
    C = int(cp_line[0])
    P = int(cp_line[1])
    contributors = []
    all_skills = []
    for i in range(C):
        contributor_line = file1.readline().split()
        contributor_name = contributor_line[0]
        N = int(contributor_line[1])
        contributor = Contributor(contributor_name, N)
        for j in range(N):
            skill_line = file1.readline().split()
            skill_name = skill_line[0]
            all_skills.append(skill_name)
            skill_level = int(skill_line[1])
            contributor.skills.append(Skill(skill_name, skill_level))
        contributors.append(contributor)
    projects = []
    for i in range(P):
        project_line = file1.readline().split()
        project_name = project_line[0]
        D, S, B, R = int(project_line[1]), int(project_line[2]), int(project_line[3]), int(project_line[4])
        project = Project(project_name, D, S, B, R)
        for j in range(R):
            skill_line = file1.readline().split()
            skill_name = skill_line[0]
            all_skills.append(skill_name)
            skill_level = int(skill_line[1])
            project.roles.append(Role(skill_name, skill_level))
        projects.append(project)

    all_skills = list(set(all_skills))
    for contributor in contributors:
        all_skill_levels = np.zeros(len(all_skills))
        for skill in contributor.skills:
            all_skill_levels[all_skills.index(skill.name)] = skill.level
        contributor.skills = all_skill_levels

    for project in projects:
        for role in project.roles:
            role.skill_index = all_skills.index(role.name)

    return C, P, contributors, projects, all_skills


def read_output_file(filename):
    # TODO: Implement Output File Parsing
    file1 = open(filename, 'r')
    return file1.readline().split()[1:]

class Data:
    def __init__(self, task_name):
        super(Data, self).__init__()
        self.task_name = task_name

        self.C, self.P, self.contributors, self.projects, self.all_skills = read_input_file(f'input_data/{task_name}.in.txt')

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

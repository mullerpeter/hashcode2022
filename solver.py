from dataparser import Data, Role
import random
import numpy as np
from tqdm import tqdm


def solve(data: Data):
    # TODO: Implement Greedy Solver
    return


def get_compatible_contributor(data: Data, role: Role, current_people, current_skills):
    if current_skills[role.skill_index] >= role.level:
        possible_candidates = []
        for con in data.contributors:
            if con.skills[role.skill_index] == role.level - 1 and con.name not in current_people:
                possible_candidates.append(con)
        if len(possible_candidates) > 0:
            canditate_scores = [con.get_score() for con in possible_candidates]
            sorted_scores_index = np.argsort(canditate_scores)
            possible_candidates[sorted_scores_index[0]].temp_skill_increase = role.skill_index
            return possible_candidates[sorted_scores_index[0]]
    possible_candidates = []
    possible_level_candidates = []
    for con in data.contributors:
        if con.skills[role.skill_index] == role.level and con.name not in current_people:
            possible_level_candidates.append(con)
        if con.skills[role.skill_index] >= role.level and con.name not in current_people:
            possible_candidates.append(con)

    if len(possible_level_candidates) > 0:
        canditate_scores = [con.get_score() for con in possible_level_candidates]
        sorted_scores_index = np.argsort(canditate_scores)
        possible_level_candidates[sorted_scores_index[0]].temp_skill_increase = role.skill_index
        return possible_level_candidates[sorted_scores_index[0]]
    if len(possible_candidates) > 0:
        canditate_scores = [con.get_score() for con in possible_candidates]
        sorted_scores_index = np.argsort(canditate_scores)
        return possible_candidates[sorted_scores_index[0]]

    return None

def solve_peter(data: Data):
    project_scores = [project.get_score() for project in data.projects]
    sorted_scores_index = np.argsort(project_scores)[::-1]
    solution = []
    second_try = []
    for project_index in tqdm(sorted_scores_index):
        all_good = True
        current_people = []
        current_skills = np.zeros(len(data.all_skills))
        for role in data.projects[project_index].roles:
            role.assigned = get_compatible_contributor(data, role, current_people, current_skills)
            if role.assigned is None:
                all_good = False
            else:
                current_skills = np.maximum(current_skills, role.assigned.skills)
                current_people.append(role.assigned.name)
        if all_good:
            for con in [role.assigned for role in data.projects[project_index].roles]:
                con.work_time += data.projects[project_index].D
                if con.temp_skill_increase is not None:
                    con.skills[con.temp_skill_increase] += 1
                    con.temp_skill_increase = None
            solution.append(data.projects[project_index])
        else:
            for con in [role.assigned for role in data.projects[project_index].roles]:
                if con is not None:
                    con.temp_skill_increase = None
            second_try.append(project_index)
    while True:
        original_second_try = list(second_try)
        second_try = []
        for project_index in tqdm(original_second_try):
            all_good = True
            current_people = []
            current_skills = np.zeros(len(data.all_skills))
            for role in data.projects[project_index].roles:
                role.assigned = get_compatible_contributor(data, role, current_people, current_skills)
                if role.assigned is None:
                    all_good = False
                else:
                    current_skills = np.maximum(current_skills, role.assigned.skills)
                    current_people.append(role.assigned.name)
            if all_good:
                for con in [role.assigned for role in data.projects[project_index].roles]:
                    con.work_time += data.projects[project_index].D
                    if con.temp_skill_increase is not None:
                        con.skills[con.temp_skill_increase] += 1
                        con.temp_skill_increase = None
                solution.append(data.projects[project_index])
            else:
                for con in [role.assigned for role in data.projects[project_index].roles]:
                    if con is not None:
                        con.temp_skill_increase = None
                second_try.append(project_index)
        if len(original_second_try) == len(second_try):
            break
    return solution



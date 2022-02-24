from dataparser import Data
from optimizer import run_optimisation
from score import score
from solver import solve, solve_peter
from zip_code import zip_code

if __name__ == '__main__':

    task_name = 'a_an_example'
    print(task_name)
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'b_better_start_small'
    print(task_name)
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'c_collaboration'
    print(task_name)
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'd_dense_schedule'
    print(task_name)
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'e_exceptional_skills'
    print(task_name)
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'f_find_great_mentors'
    print(task_name)
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()

    zip_code()




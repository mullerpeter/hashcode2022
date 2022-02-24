from dataparser import Data
from optimizer import run_optimisation
from score import score
from solver import solve, solve_peter
from zip_code import zip_code

if __name__ == '__main__':

    task_name = 'a_an_example'
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'b_better_start_small'
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'c_collaboration'
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'd_dense_schedule'
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'e_exceptional_skills'
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()
    task_name = 'f_find_great_mentors'
    data = Data(task_name)
    data.solution = solve_peter(data)
    data.write_solution()

    zip_code()




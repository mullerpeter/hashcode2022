from dataparser import Data
from optimizer import run_optimisation
from score import score
from solver import solve
from zip_code import zip_code

if __name__ == '__main__':

    # task_name = 'a_an_example'
    # task_name = 'b_basic'
    # task_name = 'c_coarse'
    task_name = 'd_difficult'
    # task_name = 'e_elaborate'

    load_best = True

    data = Data(task_name)
    if load_best:
        data.load_best_solution()
    else:
        solve(data)
    task_score = score(data)
    data.write_if_best(task_score)

    run_optimisation(data, num_steps=10)

    zip_code()


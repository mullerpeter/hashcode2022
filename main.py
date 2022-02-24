from dataparser import Data
from optimizer import run_optimisation
from score import score
from solver import solve
from zip_code import zip_code

if __name__ == '__main__':

    task_name = 'a_an_example'
    # task_name = 'b_better_start_small'
    # task_name = 'c_coarse'
    # task_name = 'd_difficult'
    # task_name = 'e_elaborate'

    load_best = False

    data = Data(task_name)


    zip_code()


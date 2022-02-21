from dataparser import Data


def score(data: Data):
    task_score = 0
    for i in range(data.num_customers):
        if all(x in data.on_pizza for x in data.likes[i]) and all(x not in data.on_pizza for x in data.hates[i]):
            task_score += 1
    return task_score

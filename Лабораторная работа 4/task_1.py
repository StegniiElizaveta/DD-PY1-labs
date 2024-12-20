# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as file:
        data = json.load(file)
        #data - список словарей
    list_score = [item['score'] for item in data]
    list_weight = [item['weight'] for item in data]
    #list_mult = [list_score*list_weight]
    list_mult = []
    for i in range(len(list_weight)):
        list_mult[i] = list_score[i]*list_weight[i]
    return round(sum(list_mult), 3)


print(task())

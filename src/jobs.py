from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        data = csv.DictReader(file)
        list = []
        for row in data:
            list.append(row)
        return list

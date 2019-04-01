import json


file_dao_test = "Graf.txt"


def create_graf():

    g = {
        1: {2: 7, 3: 9, 6: 14},
        2: {1: 7, 3: 10, 4: 15},
        3: {1: 9, 2: 10, 4: 11, 6: 2},
        4: {2: 15, 3: 11, 5: 6},
        5: {4: 6, 6: 9},
        6: {1: 14, 3: 2, 5: 9}
    }

    way = file_dao_test
    myfile = open(way, mode='w')
    json.dump(g, myfile)


def read_graf():
    way = file_dao_test
    myfile =open(way, mode='r')
    g = json.load(myfile)
    return g

create_graf()
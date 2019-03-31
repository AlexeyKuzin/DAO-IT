import json


file_Dao_test = r"C:\Users\Aleks\PycharmProjects\DAO-IT\Graf.txt"

def create_Graf():

    G = {
        1: {2: 7, 3: 9, 6: 14},
        2: {1: 7, 3: 10, 4: 15},
        3: {1: 9, 2: 10, 4: 11, 6: 2},
        4: {2: 15, 3: 11, 5: 6},
        5: {4: 6, 6: 9},
        6: {1: 14, 3: 2, 5: 9}
    }

    Way = file_Dao_test
    myfile = open(file_Dao_test, mode='w')
    json.dump(G, myfile)


def read_Graf():
    Way = file_Dao_test
    myfile =open(file_Dao_test, mode='r')
    G = json.load(myfile)
    return G
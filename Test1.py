# -*- coding utf-8 -*-
from Dijc import *
from Create_And_Read_graf import *

create_graf()

g = read_graf()
print(str(type(g)))
print("Граф успешно загружен")
print("Всего точек " + (str(len(g))))

dejc = Dejcstra(g)
dejc.set_point()
dejc.dijkstra()



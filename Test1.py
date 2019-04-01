# -*- coding utf-8 -*-
from Dejc import *
from Create_And_Read_graf import *

g = read_graf()
print(str(type(g)))
print("Граф успешно загружен")
print("Всего точек " + (str(len(g))))

dejc = Dejcstra(g)
dejc.set_points()
dejc.dijkstra()



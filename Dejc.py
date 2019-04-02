# -*- cofing utf-8 -*-


class Dejcstra:
    def __init__(self, g):
        self.g = g
        self.N = len(self.g)

    def set_points(self):
        global sp, fp

        while True:
            print("Пожайлуста Введите начальную точку маршрута")
            sp = input()
            if sp in self.g.keys():
                break
        print("Начальная точка маршрута назначена")

        while True:
            print("Пожайлуста Введите конечную точку маршрута:")
            fp = input()
            if fp in self.g.keys():
                break
        print("Конечная точка маршрута назначена")
        print('\nНачальная точка маршрута: ' + str(sp) + ' конечная точка маршрута: ' + str(fp))

    def dijkstra(self):
        v = sp # - текущая метка
        e = fp # - конечная метка
        g = self.g # - граф
        N = len(g) #-количество вершин графа

        def yes_sir(v, p, t, b, e):
            for x in g[v]:  # для каждого соседа (х) текущей вершины (v)
                xm = p[v] + g[v][x]  # новая метка соседа (xm) =
                # метка текущей вершины (p[v]) +
                # значение ребра vx (g[v][x])

                if not x in p:  # если соседа (x) нет в словаре (p)
                    p[x] = xm  # записываем новую метку (xm) в словарь с ключем (x)
                    b[x] = v  # как только метка пересчитывается, запоминаем
                    # (следующая вершина: предыдущая вершина) в словаре (b)
                elif not x in t:  # иначе если (x) не в (t)
                    if p[x] > xm:  # если старая метка соседа больше новой метки
                        p[x] = xm  # новую метку записываем на место старой
                        b[x] = v  # как только метка пересчитывается, запоминаем
                        # (следующая вершина: предыдущая вершина) в словаре (b)

            t.append(v)

            if N <= len(t):  # Условие выхода из функции

                s = []  # кратчайший путь
                s.insert(0, e)  # вставляем (е) в список (s) по индексу (0)

                while True:
                    if b[e] == -1:  # значение ключа (-1) имеет начальная вершина
                        # вот её и ищем в словаре (b)
                        print('Кратчайший путь от начальной до конечной вершины =', s)
                        print("Общий вес маршрута составил: " + str(p[fp]))
                        break  # выходим из цикла
                    e = b[e]  # теперь последней вершиной будет предыдущая
                    s.insert(0, e)  # вставляем (е) в список (s) по индексу (0)1

                return s

            for d in p:  # вершина (d) с минимальной меткой из словаря (p)
                if d not in t:
                    dm = p[d]
                    break  # пусть это будет первая вершина из словаря (p)

            for y in p:  # для каждой вершины (y) из словаря (p)
                if p[y] < dm and not y in t:
                    dm = p[y]
                    d = y  #

            v = d  # теперь текущей вершиной v будет вершина d

            yes_sir(v, p, t, b, e)

        t = [] #спиок посещенных точек
        p = {} #открытая вершина и ее метка
        p[sp] = 0
        b = {} #короткий путь
        b[sp] = -1
        y = yes_sir(v, p, t, b, e)

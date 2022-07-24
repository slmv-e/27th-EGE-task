def main():  # эффективный алгоритм
    k = 251  # координаты могут принимать значения от 0 до 250 включительно, 250 - 0 + 1 = 251
    kit_cnt = 0  # количество наборов по четыре пары
    mas = []  # массив с парами
    graph = []  # график с координатами graph[x][y]

    for _ in range(k):  # заполняю график
        graph.append([0] * k)

    with open("27-B.txt") as f:
        n = int(f.readline())
        for _ in range(n):
            pair = tuple(map(int, f.readline().split()))  # точка
            mas.append(pair)  # добавляю точку в массив
            graph[pair[0]][pair[1]] = 1  # помечаю точку на графике

    mas.sort(key=lambda x: (x[0], x[1]))  # сортирую массив по двум условиям: x по возрастанию, y по возрастанию

    for elem in mas:  # перебераю точки в отсортированном массиве
        for i in range(max(elem) + 1, k):  # перебираю всевозможные варианты длины стороны квадрата
            side_length = i - max(elem)  # длина стороны
            B = (elem[0], elem[1] + side_length)  # точка A - elem
            C = (elem[0] + side_length, elem[1] + side_length)  # A, B, C, D - это точки, которые образуют квадрат
            D = (elem[0] + side_length, elem[1])
            if graph[B[0]][B[1]] == 1 and graph[C[0]][C[1]] == 1 and graph[D[0]][D[1]] == 1:  # проверяю наличие точек
                kit_cnt += 1

    print(kit_cnt)


if __name__ == '__main__':
    main()

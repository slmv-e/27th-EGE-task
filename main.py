# переборный алгоритм
mas = []
with open("27-A.txt") as f:
    n = int(f.readline())
    for _ in range(n):
        pair = tuple(map(int, f.readline().split()))
        mas.append(pair)

kit_cnt = 0

for a in range(n - 3):  # перебираю первую точку
    for b in range(a + 1, n - 2):  # перебираю вторую точку
        for c in range(b + 1, n - 1):  # перебираю третью точку
            for d in range(c + 1, n):  # перебираю четвертую точку
                pairs_kit = [mas[a], mas[b], mas[c], mas[d]]  # набор пар
                pairs_kit.sort(key=lambda x: (x[0], x[1]))  # сортирую пары (подробное объяснение работы lambda
                # выражения есть в файле effective.py)
                side_length_x = pairs_kit[3][0] - pairs_kit[0][0]
                side_length_y = pairs_kit[3][1] - pairs_kit[0][1]
                if side_length_x == side_length_y and pairs_kit[3][0] == pairs_kit[2][0] and \
                        pairs_kit[3][1] == pairs_kit[1][1] and pairs_kit[3][1] - pairs_kit[2][1] == side_length_y \
                        and pairs_kit[3][0] - pairs_kit[1][0] == side_length_x:  # условие квадрата
                    kit_cnt += 1
print(kit_cnt)

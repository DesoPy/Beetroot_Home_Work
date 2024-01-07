import math


"""
В класі ми майже не реалізовували задачу. Зробив задачу зі Slak, яку ти давав в якості проработки.

Дано граф, що представляє маршрути між містами України, з вагами – відстанями між містами.
Знайти найкоротший шлях від одного міста до іншого. Між містами може не бути зв'язків, а може, в теорії, бути декілька,
можете подивитися на карті. :)
Для вирішення цієї задачі пропоную використати алгоритм Дейкстри.

Матриця з містами:
https://docs.google.com/spreadsheets/d/1IBHc1qoYW-kSxg3pSfon2dHfzNzVqHb7ZcWHuWjYdgo/edit#gid=0
"""


def arg_min(t, s):
    amin = -1
    m = math.inf
    for i, t in enumerate(t):
        if t < m and i not in s:
            m = t
            amin = i

    return amin


matrix = ((0, 5, math.inf, math.inf, 4, math.inf, math.inf, math.inf, math.inf),
          (5, 0, 4, 4, math.inf, math.inf, math.inf, math.inf, math.inf),
          (math.inf, 4, 0, 6, math.inf, math.inf, math.inf, 6, math.inf),
          (math.inf, 4, 6, 0, 7, math.inf, math.inf, 7, math.inf),
          (4, math.inf, math.inf, 7, 0, 7, math.inf, math.inf, math.inf),
          (math.inf, math.inf, math.inf, math.inf, 7, 0, 3, math.inf, math.inf),
          (math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 3, math.inf),
          (math.inf, math.inf, 7, 7, math.inf, math.inf, 3, 0, 5),
          (math.inf, math.inf, math.inf, math.inf, 4, math.inf, math.inf, 5, 0))

len_matrix = len(matrix)
tran = [math.inf] * len_matrix

v = 0
s = {v}
tran[v] = 0
m = [0] * len_matrix

while v != -1:
    for j, dw in enumerate(matrix[v]):
        if j not in s:
            w = tran[v] + dw
            if w < tran[j]:
                tran[j] = w
                m[j] = v

    v = arg_min(tran, s)
    if v >= 0:
        s.add(v)


start = 0
end = 8
final = [end]
while end != start:
    end = m[final[-1]]
    final.append(end)

print(final)

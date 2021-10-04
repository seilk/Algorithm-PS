def solution(brown, yellow):
    area = brown + yellow

    lst = []
    for i in range(1, area):  # area = 4
        if i * i > area:  # i = 1, 2
            break
        elif area % i == 0:  # 공약수 (x, y)
            j = area // i  # (1, ) (2, ) (3, ) ... (sqrt(area), sqrt(area))
            lst.append((j, i))
    for i in lst:
        # 가로길이 - 2 * 세로길이 - 2 = yellow
        if (i[0] - 2) * (i[1] - 2) == yellow:
            return [i[0], i[1]]


def solution(places):
    answer = []
    for place in places:
        place = [list(place[i]) for i in range(5)]
        personPositions = findPerson(place)
        answer.append(check(place, personPositions))
    return answer


def findPerson(place):
    positions = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                positions.append([i, j])
    return positions


def check(place, personPositions):
    dx = [0, 0, 1, -1, -1, 1, 1, -1, 2, -2, 0, 0]
    dy = [1, -1, 0, 0, -1, 1, -1, 1, 0, 0, 2, -2]
    for position in personPositions:
        y, x = position[0], position[1]
        for i in range(12):
            if 0 <= y + dy[i] < 5 and 0 <= x + dx[i] < 5:
                if place[y + dy[i]][x + dx[i]] == 'P':
                    if 0 <= i < 4:
                        return 0
                    if i == 4 and (place[y][x - 1] != 'X' or place[y - 1][x] != 'X'):
                        return 0
                    if i == 5 and (place[y][x + 1] != 'X' or place[y + 1][x] != 'X'):
                        return 0
                    if i == 6 and (place[y][x + 1] != 'X' or place[y - 1][x] != 'X'):
                        return 0
                    if i == 7 and (place[y][x - 1] != 'X' or place[y + 1][x] != 'X'):
                        return 0
                    if i == 8 and place[y][x + 1] != 'X':
                        return 0
                    if i == 9 and place[y][x - 1] != 'X':
                        return 0
                    if i == 10 and place[y + 1][x] != 'X':
                        return 0
                    if i == 11 and place[y - 1][x] != 'X':
                        return 0
    return 1


#
#
#
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                               "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

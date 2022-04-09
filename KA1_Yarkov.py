lookup_path = []
history_path = []
maze = []


def read_input():
    file = open("input.txt", "r")
    string = []
    points_list = []
    n = int(file.readline())
    m = int(file.readline())
    for i in range(0, n):
        w = file.readline().split(" ")
        for j in range(0, m):
            string.append(int(w[j]))
        maze.append(string.copy())
        string.clear()
    start_pos = get_point(file.readline())
    end_pos = get_point(file.readline())
    file.close()
    points_list.append(start_pos)
    points_list.append(end_pos)
    return points_list


def get_point(str_point):
    coordinate = str_point.split(" ")
    out_coordinate = []
    x = int(coordinate[0]) - 1
    y = int(coordinate[1]) - 1
    out_coordinate.append(x)
    out_coordinate.append(y)
    return out_coordinate


def write_output():
    file = open("output.txt", "w+")
    file.write("Y" + '\n')
    for point in lookup_path:
        file.write(str(point[0] + 1) + ' ' + str(point[1] + 1) + '\n')
    file.close()


def left(location):
    if location[1] == 0:
        return False
    else:
        new_location = [location[0], location[1] - 1]
        if new_location in history_path:
            return False
        elif maze[new_location[0]][new_location[1]] == 0:
            history_path.append(new_location)
            lookup_path.append(new_location)
            return True
        else:
            return False


def right(location):
    if location[1] == len(maze[0]) - 1:
        return False
    else:
        new_location = [location[0], location[1] + 1]
    if new_location in history_path:
        return False
    elif maze[new_location[0]][new_location[1]] == 0:
        history_path.append(new_location)
        lookup_path.append(new_location)
        return True
    else:
        return False


def up(location):
    if location[0] == 0:
        return False
    else:
        new_location = [location[0] - 1, location[1]]
        if new_location in history_path:
            return False
        elif maze[new_location[0]][new_location[1]] == 0:
            history_path.append(new_location)
            lookup_path.append(new_location)
            return True
        else:
            return False


def down(location):
    if location[0] == len(maze) - 1:
        return False
    else:
        new_location = [location[0] + 1, location[1]]
    if new_location in history_path:
        return False
    elif maze[new_location[0]][new_location[1]] == 0:
        history_path.append(new_location)
        lookup_path.append(new_location)
        return True
    else:
        return False


if __name__ == '__main__':
    points_list = read_input()
    start = points_list[0]
    end = points_list[1]
    lookup_path.append(start)
    history_path.append(start)
try:
    while lookup_path[-1] != end:
        now = lookup_path[-1]
        if left(now) or right(now) or up(now) or down(now):
            continue
        lookup_path.pop()

    write_output()
except:
    file = open("output.txt", "w+")
    file.write("N" + '\n')


class Line:
    def __init__(self, string):
        tokens = string.split(' -> ')
        self.p1 = list(map(int, tokens[0].split(',')))
        self.p2 = list(map(int, tokens[1].split(',')))

    def is_diagonal(self):
        return self.p1[0] != self.p2[0] and self.p1[1] != self.p2[1]

    def is_angle_45(self):
        return abs(self.p1[0] - self.p2[0]) == abs(self.p1[1] - self.p2[1])

    def iterate(self):
        direction = [self.p2[0] - self.p1[0], self.p2[1] - self.p1[1]]
        direction_length = (direction[0]**2 + direction[1]**2)**0.5
        direction = [int(round(direction[0] / direction_length)), int(round(direction[1] / direction_length))]

        curr_pos = self.p1
        yield curr_pos
        while curr_pos != self.p2:
            curr_pos = [curr_pos[0] + direction[0], curr_pos[1] + direction[1]]
            yield curr_pos


def hydrothermal_venture():
    with open('Day5/input.txt', 'r') as file:
        overlapping_points = 0
        terrain = {}
        overlapping_points_diagonal = 0
        terrain_diagonal = {}
        for line in file.readlines():
            curr_line = Line(line)
            if not curr_line.is_diagonal():
                for point in curr_line.iterate():
                    point_tuple = tuple(point)
                    terrain[point_tuple] = terrain.get(point_tuple, 0) + 1
                    if terrain[point_tuple] == 2:
                        overlapping_points += 1

            if not curr_line.is_diagonal() or curr_line.is_angle_45():
                for point in curr_line.iterate():
                    point_tuple = tuple(point)
                    terrain_diagonal[point_tuple] = terrain_diagonal.get(point_tuple, 0) + 1
                    if terrain_diagonal[point_tuple] == 2:
                        overlapping_points_diagonal += 1

        return overlapping_points, overlapping_points_diagonal

class IO:
    def getStr(self):
        return input().strip()

    def getInt(self):
        return int(input().strip())

    def getStrList(self):
        return self.getStr().split(" ")

    def getIntList(self):
        return [int(x) for x in self.getStrList()]

    def strTuple(self, tuple):
        return "%s %s" % tuple

    def strList(self, li):
        return " ".join(map(str, li))


io = IO()

"""
The children's game Hotter Colder is played as follows. 
Player A leaves the room while player B hides an object somewhere
in the room. 
Player A re-enters at position (0,0) and then visits
various other positions about the room. 
When player A visits a new position, player B announces "Hotter" if this position is closer to the object than the previous position; player B announces "Colder" if it is farther and "Same" if it is the same distance.

Your task is to calculate the area of the region in which the object may have been placed.

Input
The first line of input will consist of a single integer n, the number of positions (1 ≤ n
≤ 50).
The following n lines each contain an x,y coordinate pair and one of the words
"Hotter", "Colder", or "Same". Each pair represents a position within the room, which
is a square with opposite corners at (0,0) and (10,10).
Output
For each line of input print a line giving the total area of the region in which the object
may have been placed based on the information in the lines processed so far, to 2
decimal places. If there is no such region, output 0.00."""


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __eq__(self, that: object) -> bool:
        return self.x == that.x and self.y == that.y

    def __repr__(self) -> str:
        return str((self.x, self.y))


# Get input
n = io.getInt()  # number of positions (1 ≤ n ≤ 50).


"""
Shoelace formula
https://en.wikipedia.org/wiki/Shoelace_formula
"""


class polygon:
    def __init__(self, vertices: list[Point]) -> None:
        self.vertices = vertices

    def area(self) -> float:
        sum = 0
        for i in range(len(self.vertices)):
            sum += (
                self.vertices[i].x * self.vertices[i - 1].y
                - self.vertices[i - 1].x * self.vertices[i].y
            )
        return 0.5 * abs(sum)

    def update_vertices(self, pA: Point, pB: Point, near: str) -> None:
        # if area already is 0
        if self.area() == 0:
            return
        if pA == pB:
            return
        if near == "Same":
            # if two positions are not same, then possible area must be 0
            self.vertices = [Point(0, 0)]
            return

        # make point pA the nearer one
        if near == "Hotter":
            pA, pB = pB, pA

        dist_diff_list = [self.dist_diff(pA, pB, v) for v in self.vertices]

        # Calculate new vertices if needed
        # Case 1.1, no intersects, keep all the vertices
        # Case 1.2, no intersects, remove all the vertices

        # Case 2.1, intersected one line, keep all
        # Case 2.2, intersected one line, remove all except two vertices
        # Case 3, intersects with vertices, just keep and remove
        # Case 4, intersects with non vertices, calculate new vertices
        new_vertices = []

        for i in range(len(dist_diff_list)):
            # append the vertices that are "near pA"
            if dist_diff_list[i - 1] <= 0:
                new_vertices.append(self.vertices[i - 1])

            # check if need to calculate new vertices (intersections)
            if dist_diff_list[i - 1] * dist_diff_list[i] < 0:
                new_v = self.intersect(self.vertices[i - 1], self.vertices[i], pA, pB)
                new_vertices.append(new_v)

        self.vertices = new_vertices

    """
    Find the point on the line defined by v1 and v2 and the distances to pA and pB are same
    """

    def intersect(self, v1, v2, pA, pB) -> Point:
        # Desired point:
        # (v1.x + t(v2.x - v1.x), v1.y + t(v2.y - v1.y))
        # distance(new_p, pA) == distance(new_p, pB)
        # (x - pA.x)**2 + (y - pA.y)**2 == (x - pB.x)**2 + (y - pB.y)**2
        # substitute and simplify
        #
        # Coefficients for the linear equation in t
        numerator = (
            pA.x**2
            + pA.y**2
            - pB.x**2
            - pB.y**2
            - 2 * v1.x * (pA.x - pB.x)
            - 2 * v1.y * (pA.y - pB.y)
        )
        denominator = 2 * (
            (v2.x - v1.x) * (pA.x - pB.x) + (v2.y - v1.y) * (pA.y - pB.y)
        )
        t = numerator / denominator
        x = v1.x + t * (v2.x - v1.x)
        y = v1.y + t * (v2.y - v1.y)
        return Point(x, y)

    def dist_diff(self, A: Point, B: Point, v: Point) -> float:
        return self.distance(A, v) - self.distance(B, v)

    def distance(self, p1: Point, p2: Point) -> float:
        return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


def problem():
    poly = polygon([Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)])

    last_point = Point(0, 0)

    for _ in range(n):
        input = io.getStrList()  # (0,0) and (10,10)
        new_point = Point(float(input[0]), float(input[1]))
        near = input[2]

        poly.update_vertices(last_point, new_point, near)

        last_point = new_point
        # output
        rd = round(poly.area(), 2)
        print("%.2f" % rd)


problem()

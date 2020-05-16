class deque():
    def __init__(self, array):
        """
        initialization
        """
        self.array = array
        self.mid = 0

    def pushright(self, val):
        """
        To add an element to the right.
        """
        self.array.insert(self.mid, val)

        self.mid = self.mid + 1

    def popleft(self):
        """
        If mid is the rightmost element, move it left.
        """
        if self.mid == len(self.array) - 1:
            self.mid = self.mid - 1

        if (len(self.array) > 0):
            return self.array.pop()
        else:
            return None

    def __str__(self):
        """
        To display itself.
        """
        ret = "["

        if len(self.array) == 0:
            return "[]"

        for idx, val in enumerate(self.array):
            if idx == self.mid:
                ret = ret + "({}) ".format(str(val))
            else:
                ret = ret + str(val) + " "
        return ret.strip() + "]"


def pathfinder(matrix, start, end):
    """
    This function takes in a 2D plane (a matrix represented as a list of lists), a tuple containing coordinates of the start point(start) and a tuple containing coordinates of the destination(end) and returns an integer representing the lowest number of steps required to reach the destination.
    """
    try:
        assert [i for i in list(start + end) if  i  < 0 or i >= len(matrix)] == [] and matrix[(start[0])][(start[1])] != 0 and matrix[(end[0])][(end[1])] != 0, "Error!"
        for i in matrix:
            i.insert(0, 0)
            i.append(0)
        width = len(matrix[0])        
        matrix = [[0] * width] + matrix + [[0] * width]
        height = len(matrix)
        start = (start[0] + 1, start[1] + 1, 0)
        end = (end[0] + 1, end[1] + 1)

        queue = deque([start])

        seen = set()
        while queue:
            x, y, d = queue.popleft()

            if not 0 <= x < width:
                continue
            if not 0 <= y < height:
                continue
            if matrix[x][y] == 0:
                continue

            if (x, y) == end:
                return d

            if (x, y) in seen:
                continue
            seen.add((x, y))

            queue.pushright((x+1, y, d+1))
            queue.pushright((x-1, y, d+1))
            queue.pushright((x, y+1, d+1))
            queue.pushright((x, y-1, d+1))
        return -1
    except TypeError:
        raise AssertionError
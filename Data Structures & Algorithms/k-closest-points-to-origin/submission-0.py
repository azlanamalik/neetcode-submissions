class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_arr = {}

        for point in points:
            new_arr[tuple(point)] = math.sqrt(point[0] ** 2 + point[1] ** 2)

        sorted_points = sorted(new_arr, key=new_arr.get)#create a new array with points sorted on the axis of value

        return [list(point) for point in sorted_points[:k]]
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        time = 0

        while heap:
            temp = []

            for i in range(n + 1):
                if heap:
                    count = heapq.heappop(heap)
                    count += 1

                    if count < 0:
                        temp.append(count)

                    time += 1

                elif temp:
                    time += 1
                else:
                    break

            for count in temp:
                heapq.heappush(heap, count)

        return time
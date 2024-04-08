import heapq

def min_resources_for_intervals(intervals):
    """
    Finds the minimum number of resources needed to schedule all intervals without overlap.
    :param intervals: List of tuples (start_time, finish_time) representing the intervals.
    :return: Minimum number of resources needed.
    """
    if not intervals:
        return 0

    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])
    pq = []  # Priority queue to keep track of end times
    heapq.heappush(pq, intervals[0][1])

    for start, end in intervals[1:]:
        if start >= pq[0]:  # If the current interval starts after the earliest end time
            heapq.heappop(pq)  # The same resource can be reused
        heapq.heappush(pq, end)  # Allocate a new resource or reuse the previous one

    return len(pq)

# Example usage
if __name__ == "__main__":
    job_intervals = [(1, 4), (2, 5), (6, 7), (3, 8), (9, 10)]
    print("Minimum number of resources needed:", min_resources_for_intervals(job_intervals))

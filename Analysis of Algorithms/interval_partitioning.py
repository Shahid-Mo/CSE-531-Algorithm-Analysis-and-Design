import heapq

def read_intervals(n):
    """
    Reads a series of intervals from user input.

    Parameters:
    n (int): The number of intervals to read.

    Returns:
    list of tuples: A list of tuples, each representing an interval with (start time, end time).
    """
    intervals = []
    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append((start, end))
    return intervals

def interval_partitioning(intervals):
    """
    Determines the minimum number of resources needed to schedule all intervals without overlap.

    Parameters:
    intervals (list of tuples): A list of tuples, each representing an interval with (start time, end time).

    Returns:
    int: The minimum number of resources (classes) required.
    """
    # Sort intervals based on their start times
    intervals.sort(key=lambda x: x[0])
    
    # Initialize a priority queue to keep track of the earliest ending time of classes
    min_heap = [intervals[0][1]]
    
    # Iterate through the sorted intervals
    for interval in intervals[1:]:
        # If the current interval starts after the earliest class ends, reuse that class
        if interval[0] >= min_heap[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, interval[1])

    # The size of the heap indicates the number of concurrent classes
    return len(min_heap)

if __name__ == "__main__":
    n = int(input("Enter the number of intervals: "))
    intervals = read_intervals(n)
    max_classes = interval_partitioning(intervals)
    print(f"Minimum number of classes needed: {max_classes}")

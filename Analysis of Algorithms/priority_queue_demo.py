import heapq

def min_priority_queue_demo():
    """
    Demonstrates the use of a minimum priority queue using Python's heapq module.
    """
    pq = []  # Initialize an empty list to use as the priority queue
    # Adding elements to the priority queue
    heapq.heappush(pq, 4)
    heapq.heappush(pq, 7)
    heapq.heappush(pq, 9)
    heapq.heappush(pq, 11)
    
    # The minimum element can always be found at index 0
    min_element = pq[0]
    print("Minimum Element:", min_element)
    
    # Removing the minimum element
    min_element = heapq.heappop(pq)
    print("Minimum Element (popped):", min_element)

def max_priority_queue_demo():
    """
    Demonstrates the use of a maximum priority queue by inverting the values in Python's heapq module.
    """
    max_priority_queue = []  # Initialize an empty list to use as the priority queue
    # Adding elements to the priority queue (inverted to simulate a max-priority queue)
    heapq.heappush(max_priority_queue, -5)
    heapq.heappush(max_priority_queue, -2)
    heapq.heappush(max_priority_queue, -9)
    heapq.heappush(max_priority_queue, -1)
    
    # The maximum element is the inverse of the minimum element in the inverted queue
    max_element = -max_priority_queue[0]
    print("Maximum Element:", max_element)
    
    # Removing the maximum element (inverted back to original value)
    max_element = -heapq.heappop(max_priority_queue)
    print("Maximum Element (popped):", max_element)

if __name__ == "__main__":
    print("Min-Priority Queue Demo:")
    min_priority_queue_demo()
    print("\nMax-Priority Queue Demo:")
    max_priority_queue_demo()


import heapq

def cache_replacement(requests, cache_size):
    """
    Simulates a cache replacement strategy based on future request times.

    Parameters:
    requests (list): Sequence of page requests.
    cache_size (int): Maximum size of the cache.
    """
    # Tracking future requests for each page
    future_requests = {}
    for i, request in enumerate(requests):
        if request not in future_requests:
            future_requests[request] = []
        future_requests[request].append(i)
        
    # Adding a final 'inf' to mark the end of requests for each page
    for request in future_requests:
        future_requests[request].append(float('inf'))

    cache = []  # The cache represented as a min-heap
    for i, request in enumerate(requests):
        # Move to the next request for the current page
        future_requests[request].pop(0)
        
        if any(item[1] == request for item in cache):
            print("hit")
            continue  # Hit: Requested page is already in the cache
        
        if len(cache) < cache_size:
            print(f"load {request} to an empty page")
        else:
            # Evict the page needed furthest in the future
            heapq.heappop(cache)
            print(f"evict {request}")
        
        heapq.heappush(cache, (future_requests[request][0], request))

# Example usage
requests = [5, 1, 3, 1, 5, 6, 3, 2, 5, 1]
cache_size = 3
cache_replacement(requests, cache_size)

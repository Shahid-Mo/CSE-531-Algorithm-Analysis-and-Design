# Algorithm Collection

This GitHub repository is a curated collection of algorithm implementations crafted during my CSE 531 Algorithm Analysis and Design course in my Master's program. It encompasses Python-based solutions across various domains, including graph theory, dynamic programming, caching mechanisms, and advanced sorting techniques. Each file within the repository is thoroughly documented, effectively bridging theoretical concepts with their practical applications. Designed to serve as both a personal academic showcase and a valuable educational resource.
## Files and Descriptions

### Graph Algorithms

- **bellman_ford.py & bellman_ford_v2.py**: Implements the Bellman-Ford algorithm for finding shortest paths in a weighted graph, including a version with optimizations.

- **bfs.py**: Breadth-First Search (BFS) algorithm for traversing or searching tree or graph data structures.

- **dijkstra.py**: Dijkstra's algorithm for finding the shortest paths between nodes in a graph.

- **graph.py**: Basic implementation of a graph data structure, including utility functions.

- **graph_coloring.py**: Graph coloring algorithm to assign colors to the vertices of a graph so that no two adjacent vertices share the same color.

- **kruskals_k_trees.py**: Kruskal's algorithm for finding a Minimum Spanning Tree (MST) for a connected weighted graph, extended to work with forests and k-minimum spanning trees.

### Scheduling and Partitioning

- **interval_partitioning.py**: Demonstrates interval partitioning, a strategy for scheduling resources without conflicts.

- **interval_scheduling.py**: Interval scheduling algorithm for finding a maximum subset of mutually compatible jobs.

### Dynamic Programming

- **knapsack_0_1.py**: 0-1 Knapsack problem solved using dynamic programming.

- **lcs.py**: Longest Common Subsequence (LCS) algorithm to find the longest subsequence common to all sequences in a set of sequences.

- **subset_sum.py**: Subset Sum problem solving to find a subset whose sum is equal to a given target.

- **unbounded_knapsack.py**: Solves the Unbounded Knapsack problem allowing unlimited use of items.

### Caching and Replacement Strategies

- **cache_replacement_strategy.py**: Demonstrates a cache replacement strategy based on future request times.

- **offline_caching.py**: Implements an offline caching strategy to optimize cache usage over a predetermined request sequence.

### Sorting and Ordering

- **merge_sort.py**: Implements the Merge Sort algorithm, a classic divide-and-conquer sorting technique.

### Utility and Miscellaneous

- **max_value_key_selection.py**: Script for finding a key with the maximum value within a subset of keys in a dictionary.

- **priority_queue_demo.py**: Demonstrates the usage of priority queues through Python's `heapq` module.

- **string_interleaving.py**: Checks if a string is an interleaving of two other strings while preserving their character order.

## Usage

Each script is standalone and can be run using Python 3.x. For example, to run the BFS algorithm, simply execute:

```bash
python bfs.py

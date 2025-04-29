def explain_algorithm(algorithm: str) -> str:
    explanations = {
        "quicksort": """
        QuickSort: Divide and Conquer
        1. Choose pivot (here: last element)
        2. Partition: Elements < pivot go left, > pivot go right
        3. Recursively sort left and right partitions
        Avg Time: O(n log n) | Worst: O(n²)
        """,
        "dijkstra": """
        Dijkstra's Algorithm: Shortest Path
        1. Initialize distances (infinity except start node)
        2. Process nodes by minimum distance
        3. Update neighbors' distances if shorter path found
        Time: O((V+E) log V) with priority queue
        """
    }
    return explanations.get(algorithm, "Explanation not available")
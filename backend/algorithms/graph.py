from typing import Dict, List

def dfs(graph: Dict[str, List[str]], start: str) -> dict:
    """Depth-First Search with step tracking"""
    visited = []
    stack = [start]
    steps = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            steps.append({
                "current": node,
                "visited": visited.copy(),
                "stack": stack.copy()
            })
            stack.extend(reversed(graph[node]))
    
    return {"steps": steps, "traversal": visited}

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> dict:
    """Returns shortest paths with intermediate steps"""
    # Implementation with priority queue
    import heapq
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    steps = []
    
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        steps.append({
            "current": current_node,
            "distances": distances.copy()
        })
        
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return {"steps": steps, "distances": distances}

def bfs(graph: Dict[str, List[str]], start: str) -> dict:
    """Breadth-First Search with step tracking"""
    visited = []
    queue = [start]
    steps = []
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            steps.append({
                "current": node,
                "visited": visited.copy(),
                "queue": queue.copy()
            })
            queue.extend(graph[node])
    
    return {"steps": steps, "traversal": visited}

def astar(graph: Dict[str, Dict[str, int]], start: str, end: str, heuristic: Dict[str, int]) -> dict:
    """A* Search with step tracking"""
    import heapq
    open_set = [(heuristic[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    steps = []
    
    while open_set:
        _, current = heapq.heappop(open_set)
        steps.append({
            "current": current,
            "open_set": [node for (_, node) in open_set],
            "g_scores": g_score.copy()
        })
        
        if current == end:
            break
            
        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                heapq.heappush(open_set, (tentative_g + heuristic[neighbor], neighbor))
    
    return {"steps": steps, "path": reconstruct_path(came_from, start, end)}

def reconstruct_path(came_from: dict, start: str, end: str) -> List[str]:
    """Helper for A* to rebuild the path"""
    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
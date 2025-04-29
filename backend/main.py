from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from algorithms.sort import quicksort, bubblesort, mergesort
from algorithms.graph import dfs, bfs, dijkstra, astar
from algorithms.explanations import explain_algorithm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with Vercel URL later
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Algorithm Tutor Backend"}

# ======================
# Sorting Endpoints
# ======================

@app.post("/sort/quicksort")
async def endpoint_quicksort(numbers: list[int]):
    """
    Example request body:
    [5, 3, 8, 1, 2]
    
    Returns:
    {
        "steps": [{"array": [...], "pivot": 2, "left": 0, "right": 4}, ...],
        "sorted": [1, 2, 3, 5, 8],
        "explanation": "QuickSort: Divide and Conquer..."
    }
    """
    result = quicksort(numbers)
    return {
        **result,
        "explanation": explain_algorithm("quicksort")
    }

@app.post("/sort/bubblesort")
async def endpoint_bubblesort(numbers: list[int]):
    """
    Example request body:
    [5, 3, 8, 1, 2]
    
    Returns:
    {
        "steps": [[3,5,1,2,8], [3,1,2,5,8], ...],
        "sorted": [1, 2, 3, 5, 8]
    }
    """
    return bubblesort(numbers)

@app.post("/sort/mergesort")
async def endpoint_mergesort(numbers: list[int]):
    """
    Returns merge sort with step-by-step merges
    """
    return mergesort(numbers)

# ======================
# Graph Endpoints  
# ======================

@app.post("/graph/dfs")
async def endpoint_dfs(graph: dict, start: str):
    """
    Example request body:
    {
        "graph": {"A": ["B","C"], "B": ["D"], "C": [], "D": []},
        "start": "A"
    }
    
    Returns:
    {
        "steps": [
            {"current": "A", "visited": ["A"], "stack": ["B","C"]},
            {"current": "B", "visited": ["A","B"], "stack": ["D","C"]},
            ...
        ],
        "traversal": ["A","B","D","C"]
    }
    """
    return dfs(graph, start)

@app.post("/graph/bfs")
async def endpoint_bfs(graph: dict, start: str):
    """Same input format as DFS"""
    return bfs(graph, start)

@app.post("/graph/dijkstra")
async def endpoint_dijkstra(graph: dict, start: str):
    """
    Example request body:
    {
        "graph": {
            "A": {"B": 6, "D": 1},
            "B": {"A": 6, "D": 2, "E": 2},
            "D": {"A": 1, "B": 2, "E": 1},
            "E": {"B": 2, "D": 1}
        },
        "start": "A"
    }
    
    Returns:
    {
        "steps": [
            {"current": "A", "distances": {"A":0,"B":6,"D":1,"E":∞}},
            {"current": "D", "distances": {"A":0,"B":3,"D":1,"E":2}},
            ...
        ],
        "distances": {"A":0,"B":3,"D":1,"E":2}
    }
    """
    return dijkstra(graph, start)

@app.post("/graph/astar")
async def endpoint_astar(graph: dict, start: str, end: str, heuristic: dict):
    """
    For pathfinding with heuristics (e.g. grid coordinates)
    """
    return astar(graph, start, end, heuristic)

# ======================
# Utility Endpoints
# ======================

@app.get("/explain/{algorithm_name}")
async def get_explanation(algorithm_name: str):
    """
    Example: GET /explain/quicksort
    
    Returns:
    {"explanation": "QuickSort: Divide and Conquer..."}
    """
    return {"explanation": explain_algorithm(algorithm_name)}

@app.get("/algorithms")
async def list_algorithms():
    """Returns all available algorithms"""
    return {
        "sorting": ["quicksort", "bubblesort", "mergesort"],
        "graph": ["dfs", "bfs", "dijkstra", "astar"]
    }
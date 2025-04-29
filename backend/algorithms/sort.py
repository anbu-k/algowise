def quicksort(arr: list[int]) -> dict:
    """Returns each step of the sort with pivot highlights"""
    steps = []
    
    def _quicksort(arr: list[int], low: int, high: int):
        if low < high:
            pivot_idx = partition(arr, low, high)
            steps.append({
                "array": arr.copy(),
                "pivot": pivot_idx,
                "left": low,
                "right": high
            })
            _quicksort(arr, low, pivot_idx - 1)
            _quicksort(arr, pivot_idx + 1, high)
    
    def partition(arr: list[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    _quicksort(arr, 0, len(arr) - 1)
    return {"steps": steps, "sorted": arr}

def bubblesort(arr: list[int]) -> dict:
    """Returns array state after each pass"""
    steps = []
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(arr.copy())
    
    return {"steps": steps, "sorted": arr}

def mergesort(arr: list[int]) -> dict:
    """Returns each merge step of the sort"""
    steps = []
    
    def _mergesort(arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left = _mergesort(arr[:mid])
        right = _mergesort(arr[mid:])
        
        merged = merge(left, right)
        steps.append(merged.copy())
        return merged
    
    def merge(left: list[int], right: list[int]) -> list[int]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    _mergesort(arr)
    return {"steps": steps, "sorted": sorted(arr)}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#CORS for frontend (replace with Vercel URL later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Temporary for testing; restrict later
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Algorithm Tutor Backend"}

# Quicksort endpoint
@app.post("/sort/quicksort")
async def quicksort(numbers: list[int]):
    # Replace 
    sorted_numbers = sorted(numbers)
    return {"sorted": sorted_numbers}
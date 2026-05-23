from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "DevOps Project Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"tasks": tasks}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}
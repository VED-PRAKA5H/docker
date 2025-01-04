import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def check_func():
    data = {
        "item1": {"description": "All my friends drive a low rider", "type": "car"},
        "item2": {"description": "Music is my aeroplane, it's my aeroplane", "type": "plane", "size": 5},
    }
    return data


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

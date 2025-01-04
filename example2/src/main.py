import uvicorn  # ASGI server for running FastAPI applications
from fastapi import FastAPI  # FastAPI framework for building APIs

app = FastAPI()  # Create a FastAPI instance


@app.get("/")  # Define a route for the root URL using a GET request
def check_func():
    # Sample data dictionary to return as the response
    data = {
        "item1": {"description": "All my friends drive a low rider", "type": "car"},
        "item2": {"description": "Music is my aeroplane, it's my aeroplane", "type": "plane", "size": 5},
    }
    return data  # Return the data as the response


if __name__ == "__main__":
    # Run the FastAPI app using Uvicorn, accessible on all network interfaces at port 8000
    uvicorn.run(app, port=8000, host="0.0.0.0")


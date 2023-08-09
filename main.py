"""
Module to call the functions
"""
from fastapi import FastAPI
import uvicorn
from projectlib.sample import reverse, swap

app = FastAPI()


@app.get("/")
async def root():
    """
    I can help in doing operations like Reverse String , Swap Strings
    """
    return {"message": "Use me to Reverse String & Swaping any 2 String variables"}


@app.get("/reverse/{value}")
async def reverse_string(value: str):
    """
    I can help you to Reverse String
    """
    result = reverse(value)
    print(result)
    return {"result": result}


@app.get("/swap/{value1}/{value2}")
async def swap_strings(value1: str, value2: str):
    """
    I can help you to Swap String Variables
    """
    result = swap(value1, value2)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

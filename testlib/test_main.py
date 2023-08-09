"""
Module to test the api calls
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    """
    I am here to root landing message
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Use me to Reverse String & Swaping any 2 String variables"
    }

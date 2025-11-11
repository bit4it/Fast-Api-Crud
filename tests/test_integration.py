from fastapi.testclient import TestClient
from app.main import app as fastapi_app

client = TestClient(fastapi_app)

def test_create_item_endpoint():
    payload = {"name": "Laptop", "price": 50000, "description": "A high-end gaming laptop"}
    response = client.post("/api/items/", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 50000

def test_get_item_endpoint():
    payload = {"name": "Smartphone", "price": 30000, "description": "A latest model smartphone"}
    create_response = client.post("/api/items/", json=payload)
    assert create_response.status_code == 201
    created_item = create_response.json()
    item_id = created_item["id"]


    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 200
    retrieved_item = get_response.json()
    assert retrieved_item["name"] == "Smartphone"
    assert retrieved_item["price"] == 30000

def test_update_item_endpoint():
    payload = {"name": "Tablet", "price": 20000, "description": "A lightweight tablet"}
    create_response = client.post("/api/items/", json=payload)
    assert create_response.status_code == 201
    created_item = create_response.json()
    item_id = created_item["id"]

    update_payload = {"price": 18000}
    update_response = client.put(f"/api/items/{item_id}", json=update_payload)
    assert update_response.status_code == 200
    updated_item = update_response.json()
    assert updated_item["price"] == 18000

def test_delete_item_endpoint():
    payload = {"name": "Headphones", "price": 5000, "description": "Noise-cancelling headphones"}
    create_response = client.post("/api/items/", json=payload)
    assert create_response.status_code == 201
    created_item = create_response.json()
    item_id = created_item["id"]

    delete_response = client.delete(f"/api/items/{item_id}")
    assert delete_response.status_code == 200
    delete_data = delete_response.json()
    assert delete_data["message"] == "Item deleted successfully"

    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 404
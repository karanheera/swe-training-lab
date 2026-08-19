from fastapi.testclient import TestClient

from order_app.api import app


client = TestClient(app)


def test_health(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "test")

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "environment": "test",
    }


def test_order():
    response = client.get("/order?price=100&quantity=10")

    assert response.status_code == 200
    assert response.json() == {"subtotal": 1000.0, "total": 900.0}


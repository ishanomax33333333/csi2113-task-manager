import tempfile
from pathlib import Path
import app as app_module

def test_health():
    client = app_module.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_add_task():
    old_db = app_module.DB
    with tempfile.TemporaryDirectory() as tmp:
        app_module.DB = str(Path(tmp) / "test.db")
        app_module.init_db()
        client = app_module.app.test_client()

        response = client.post("/api/tasks", json={"title": "Learn Docker"})
        assert response.status_code == 201
        assert response.json["title"] == "Learn Docker"

        app_module.DB = old_db

from fastapi.testclient import TestClient
from logscan.main import app

client = TestClient(app)


def test_labels():
    assert client.post("/classify", json={"text": 'Unhandled exception in worker'}).json()["label"] == "error"
    assert client.post("/classify", json={"text": 'request timeout from upstream'}).json()["label"] == "timeout"


def test_empty_is_refused():
    assert client.post("/classify", json={"text": "  "}).status_code == 422

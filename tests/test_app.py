import pytest
import json
from app.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_predict_endpoint(client):
    test_data = {'features': [6, 148, 72, 35, 0, 33.6, 0.627, 50]}
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'prediction' in data
    assert isinstance(data['prediction'], list)
    assert data['prediction'] == [1]

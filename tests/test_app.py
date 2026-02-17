import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the home endpoint returns correct data"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Hello from Flask!'
    assert data['status'] == 'running'

def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_info_endpoint(client):
    """Test the info endpoint"""
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert 'app' in data
    assert 'environment' in data

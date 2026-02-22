from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_elibility_pass():
    payload = {
        'income' :60000,
        'age' : 25,
        'employement_status' : 'employed'
    }
    response = client.post('/loag_eligibility',json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligible' : True}

def test_eligibility_fail():
     payload = {
        'income' :30000,
        'age' : 20,
        'employement_status' : 'unemployed'
    }
     response = client.post('/loag_eligibility',json=payload)
     assert response.status_code == 200
     assert response.json() == {'eligible' : False} 
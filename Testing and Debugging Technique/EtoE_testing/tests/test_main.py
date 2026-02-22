from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_eligibility_pass():
    response = client.post('/loan-eligility',
                           json={
                               'income' : 60000,
                               'age' :36,
                               'employement_status' :'employed'
                           })
    assert response.status_code ==200
    assert response.json() == {'eligible' :True}


def test_eligibility_fail():
    response = client.post('/loan-eligility',
                           json={
                               'income' : 30000,
                               'age' :20,
                               'employement_status' :'employed'
                           })
    assert response.status_code ==200
    assert response.json() == {'eligible' :False}
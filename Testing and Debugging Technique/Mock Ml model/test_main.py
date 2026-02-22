from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
import numpy as np

client = TestClient(app)

def test_predict_with_mock():
    with patch('model.model.predict') as mock_predict :
        mock_predict.return_value = [99]
        responce = client.post(
            '/predict',
            json={
                'SepalLengthCm' : 5.5,
                'SepalWidthCm':4.2,
                'PetalLengthCm' : 2.1,
                'PetalWidthCm' : 1.9

            }
        )
        assert responce.status_code == 200
        assert responce.json()=={'prediction' : 99}
        #mock_predict.assert_called_once_with(np.array([[5.5,4.2,2.1,1.9]]))

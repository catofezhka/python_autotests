import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers',params={'trainer_id': 2561})
    assert response.status_code ==200



@pytest.mark.parametrize('key, value', [("trainer_name", "ann")])
def test_response_json(key, value):
    response = requests.get(f'{host}/trainers',params={'trainer_id': 2561})
    assert response.json()[key] == value

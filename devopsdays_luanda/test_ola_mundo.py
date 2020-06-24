def test_status_code(client):
    resposta = client.get('/')
    assert resposta.status_code == 200


def test_tdd_status_code(client):
    resposta = client.get('/tdd')
    assert resposta.status_code == 200
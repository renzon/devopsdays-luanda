def test_status_code(client):
    resposta = client.get('/')
    assert resposta.status_code == 200
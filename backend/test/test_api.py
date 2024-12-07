import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pytest
from backend.api import app
from backend.database import obter_colecao

@pytest.fixture
def cliente():
    """Configura o cliente de teste."""
    app.config['TESTING'] = True
    cliente = app.test_client()

    # Usa um banco de dados de teste
    with app.app_context():
        db = obter_colecao('pessoas')
    
    yield cliente

    # Limpeza, caso necessário
    with app.app_context():
        db.drop()  # Limpa o banco após o teste, se necessário

def teste_criar_pessoa(cliente):
    """Testa a criação de uma nova pessoa."""
    resposta = cliente.post('/pessoas', json={
        "nome": "João",
        "sobrenome": "Silva",
        "endereco": "Rua das Flores, 123",
        "cpf": "12345678900",
        "genero": "Masculino",
        "telefone": "11987654321"
    })

    assert resposta.status_code == 201
    assert resposta.json['mensagem'] == "Pessoa cadastrada com sucesso!"

def teste_listar_todas_pessoas(cliente):
    """Testa a listagem de todas as pessoas."""
    # Cria uma pessoa para testar a listagem
    cliente.post('pessoas', json={
        "nome": "João",
        "sobrenome": "Silva",
        "endereco": "Rua das Flores, 123",
        "cpf": "12345678900",
        "genero": "Masculino",
        "telefone": "11987654321"
    })

    resposta = cliente.get('/pessoas')
    assert resposta.status_code == 200
    assert len(resposta.json) == 1  # Verifica que há 1 pessoa cadastrada

def teste_atualizar_pessoa(cliente):
    """Testa a atualização de uma pessoa."""
    # Cria uma pessoa para atualizar
    cliente.post('/pessoas', json={
        "nome": "João",
        "sobrenome": "Silva",
        "endereco": "Rua das Flores, 123",
        "cpf": "12345678900",
        "genero": "Masculino",
        "telefone": "11987654321"
    })

    # Atualiza os dados
    resposta = cliente.put('/pessoas/12345678900', json={
        "nome": "João Atualizado",
        "sobrenome": "Silva",
        "endereco": "Rua das Rosas, 456",
        "cpf": "12345678900",
        "genero": "Masculino",
        "telefone": "11987654322"
    })

    assert resposta.status_code == 200
    assert resposta.json['mensagem'] == "Pessoa atualizada com sucesso!"

def teste_deletar_pessoa(cliente):
    """Testa a exclusão de uma pessoa."""
    # Cria uma pessoa para deletar
    cliente.post('/pessoas', json={
        "nome": "João",
        "sobrenome": "Silva",
        "endereco": "Rua das Flores, 123",
        "cpf": "12345678900",
        "genero": "Masculino",
        "telefone": "11987654321"
    })

    # Deleta a pessoa
    resposta = cliente.delete('/pessoas/12345678900')

    assert resposta.status_code == 200
    assert resposta.json['mensagem'] == "Pessoa deletada com sucesso!"

def teste_criar_pessoa_cpf_invalido(cliente):
    pessoa_invalida = {
        "nome": "João",
        "sobrenome": "Silva",
        "endereco": "Rua A",
        "cpf": "12345",  # CPF inválido
        "genero": "masculino",
        "telefone": "1234567890"
    }
    resposta = cliente.post('/pessoas', json=pessoa_invalida)
    assert resposta.status_code == 400
    assert "CPF deve ter exatamente 11 dígitos numéricos." in resposta.json["erros"]["cpf"]

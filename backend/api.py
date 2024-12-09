from flask import Flask, request, jsonify
from backend.database import obter_colecao
from backend.logging_config import logger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

colecao = obter_colecao('pessoas')

@app.route('/pessoas', methods=['POST'])
def criar_pessoa():
    dados = request.get_json()
    erros = {}

    # Valida nome
    nome = dados.get("nome")
    if not nome:
        erros["nome"] = "Nome é obrigatório."
    elif len(nome) < 2 or len(nome) > 50:
        erros["nome"] = "Nome deve ter entre 2 e 50 caracteres."

    # Valida sobrenome
    sobrenome = dados.get("sobrenome")
    if not sobrenome:
        erros["sobrenome"] = "Sobrenome é obrigatório."
    elif len(sobrenome) < 2 or len(sobrenome) > 50:
        erros["sobrenome"] = "Sobrenome deve ter entre 2 e 50 caracteres."

    # Valida endereço
    endereco = dados.get("endereco")
    if not endereco:
        erros["endereco"] = "Endereço é obrigatório."
    elif len(endereco) < 5:
        erros["endereco"] = "Endereço deve ter pelo menos 5 caracteres."

    # Valida CPF
    cpf = dados.get("cpf")
    if not cpf:
        erros["cpf"] = "CPF é obrigatório."
    elif not cpf.isdigit() or len(cpf) != 11:
        erros["cpf"] = "CPF deve ter exatamente 11 dígitos numéricos."

    # Valida gênero
    genero = dados.get("genero")
    if not genero:
        erros["genero"] = "Genero é obrigatório."
    elif len(genero) < 1:
        erros["genero"] = "Genero deve ter pelo menos 1 caracteres."

    # Valida telefone
    telefone = dados.get("telefone")
    if not telefone:
        erros["telefone"] = "Telefone é obrigatório."
    elif not telefone.isdigit() or not (10 <= len(telefone) <= 11):
        erros["telefone"] = "Telefone deve ter entre 10 e 11 dígitos numéricos."

    # Retorna erros se houver
    if erros:
        return jsonify({"erros": erros}), 400

    # Inserção no banco
    colecao.insert_one(dados)
    logger.info(f'Pessoa cadastrada: {dados}')
    return jsonify({"mensagem": "Pessoa cadastrada com sucesso!"}), 201

@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    pessoas = list(colecao.find({}, {"_id": 0}))
    logger.info('Listando todas as pessoas.')
    return jsonify(pessoas), 200

@app.route('/pessoas/<cpf>', methods=['GET'])
def obter_pessoa(cpf):
    pessoa = colecao.find_one({"cpf": cpf}, {"_id": 0})
    if not pessoa:
        return jsonify({"mensagem": "Pessoa não encontrada."}), 404
    logger.info(f'Leitura de pessoa: {cpf}')
    return jsonify(pessoa), 200

@app.route('/pessoas/<cpf>', methods=['PUT'])
def atualizar_pessoa(cpf):
    dados = request.get_json()
    resultado = colecao.update_one({"cpf": cpf}, {"$set": dados})
    if resultado.matched_count == 0:
        return jsonify({"mensagem": "Pessoa não encontrada."}), 404
    logger.info(f'Pessoa atualizada: {cpf}')
    return jsonify({"mensagem": "Pessoa atualizada com sucesso!"}), 200

@app.route('/pessoas/<cpf>', methods=['DELETE'])
def deletar_pessoa(cpf):
    resultado = colecao.delete_one({"cpf": cpf})
    if resultado.deleted_count == 0:
        return jsonify({"mensagem": "Pessoa não encontrada."}), 404
    logger.info(f'Pessoa deletada: {cpf}')
    return jsonify({"mensagem": "Pessoa deletada com sucesso!"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

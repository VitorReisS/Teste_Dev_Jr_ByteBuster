pessoa = {
    "nome": {"type": "string", "required": True},
    "sobrenome": {"type": "string", "required": True},
    "endereco": {"type": "string", "required": True},
    "cpf": {"type": "string", "required": True, "unique": True},
    "genero": {"type": "string", "required": True},
    "telefone": {"type": "string", "required": True}
}

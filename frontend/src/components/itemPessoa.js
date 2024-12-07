import React from 'react';
import api from '../api';

export default function ItemPessoa({ pessoa, atualizarDados, onEditar }) {
    const handleDelete = async () => {
        try {
            await api.delete(`/pessoas/${pessoa.cpf}`);
            atualizarDados();
            alert('Pessoa deletada com sucesso!');
        } catch (err) {
            console.error(err);
            alert('Erro ao deletar pessoa!');
        }
    };

    return (
        <div>
            <p>Nome: {pessoa.nome} {pessoa.sobrenome}</p>
            <p>Endereço: {pessoa.endereco}</p>
            <p>CPF: {pessoa.cpf}</p>
            <p>Gênero: {pessoa.genero}</p>
            <p>Telefone: {pessoa.telefone}</p>
            <button onClick={() => onEditar(pessoa)}>Editar</button>
            <button onClick={handleDelete}>Deletar</button>
        </div>
    );
}
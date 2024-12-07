import React from 'react';
import ItemPessoa from './itemPessoa';

export default function ListaPessoas({ pessoas, atualizarDados, onEditar }) {
    return (
        <div>
            <header>
                <h1>Listagem de Pessoas</h1>
            </header>
            {pessoas.map((pessoa) => (
                <ItemPessoa key={pessoa.cpf} pessoa={pessoa} atualizarDados={atualizarDados} onEditar={onEditar} />
            ))}
        </div>
    );
}
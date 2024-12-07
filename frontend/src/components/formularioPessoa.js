import React, { useState, useEffect } from 'react';
import api from '../api';

export default function FormularioPessoa({ atualizarDados, pessoaParaEditar, limparEdicao }) {
    const [dadosFormulario, setDadosFormulario] = useState({
        nome: '',
        sobrenome: '',
        endereco: '',
        cpf: '',
        genero: '',
        telefone: '',
    });

    const [erros, setErros] = useState({});

    useEffect(() => {
        if (pessoaParaEditar) {
            setDadosFormulario(pessoaParaEditar);
        }
    }, [pessoaParaEditar]);

    const aoAlterar = (e) => {
        setDadosFormulario({ ...dadosFormulario, [e.target.name]: e.target.value });
    };

    const validar = () => {
        const novosErros = {};

        if (!dadosFormulario.nome.trim() || dadosFormulario.nome.length < 2 || dadosFormulario.nome.length > 50) {
            novosErros.nome = 'O nome deve ter entre 2 e 50 caracteres.';
        }
        if (!dadosFormulario.sobrenome.trim() || dadosFormulario.sobrenome.length < 2 || dadosFormulario.sobrenome.length > 50) {
            novosErros.sobrenome = 'O sobrenome deve ter entre 2 e 50 caracteres.';
        }

        if (!dadosFormulario.endereco.trim() || dadosFormulario.endereco.length < 5) {
            novosErros.endereco = 'O endereço deve ter no mínimo 5 caracteres.';
        }

        if (!/^\d{11}$/.test(dadosFormulario.cpf)) {
            novosErros.cpf = 'O CPF deve conter exatamente 11 dígitos.';
        }

        if (!dadosFormulario.genero.trim() || dadosFormulario.genero.length < 5) {
            novosErros.genero = 'O gênero deve ser masculino ou feminino.';
        }

        if (!/^\d{10,11}$/.test(dadosFormulario.telefone)) {
            novosErros.telefone = 'O telefone deve conter entre 10 e 11 dígitos.';
        }
        setErros(novosErros);
        return Object.keys(novosErros).length === 0;
    };

    const onEnviar = async (e) => {
        e.preventDefault();
        if (!validar()) {
            return;
        }

        try {
            if (pessoaParaEditar) {
                // Atualizar pessoa
                await api.put(`/pessoas/${dadosFormulario.cpf}`, dadosFormulario);
                alert('Cadastro atualizado com sucesso!');
            } else {
                // Criar nova pessoa
                await api.post('/pessoas', dadosFormulario);
                alert('Pessoa cadastrada com sucesso!');
            }
            atualizarDados();
            limparFormulario();
        } catch (err) {
            console.error(err);
            alert('Erro ao salvar os dados!');
        }
    };

    const limparFormulario = () => {
        setDadosFormulario({
            nome: '',
            sobrenome: '',
            endereco: '',
            cpf: '',
            genero: '',
            telefone: '',
        });
        setErros({});
        if (limparEdicao) limparEdicao();
    };

    return (
        <div>
            <header>
                <h1>Cadastro de Pessoas</h1>
            </header>
            <p />
            <form onSubmit={onEnviar}>
                <input name="nome" value={dadosFormulario.nome} onChange={aoAlterar} placeholder="Nome" />
                {erros.nome && <p className="erro">{erros.nome}</p>}

                <input name="sobrenome" value={dadosFormulario.sobrenome} onChange={aoAlterar} placeholder="Sobrenome" />
                {erros.sobrenome && <p className="erro">{erros.sobrenome}</p>}

                <input name="endereco" value={dadosFormulario.endereco} onChange={aoAlterar} placeholder="Endereço" />
                {erros.endereco && <p className="erro">{erros.endereco}</p>}

                <input name="cpf" value={dadosFormulario.cpf} onChange={aoAlterar} placeholder="CPF (somente números)" disabled={!!pessoaParaEditar} />
                {erros.cpf && <p className="erro">{erros.cpf}</p>}

                <input name="genero" value={dadosFormulario.genero} onChange={aoAlterar} placeholder="Gênero" />
                {erros.genero && <p className="erro">{erros.genero}</p>}

                <input name="telefone" value={dadosFormulario.telefone} onChange={aoAlterar} placeholder="Telefone (somente números)" />
                {erros.telefone && <p className="erro">{erros.telefone}</p>}

                <button type="submit">{pessoaParaEditar ? 'Atualizar' : 'Cadastrar'}</button>
                {pessoaParaEditar && <button type="button" onClick={limparFormulario}>Cancelar Edição</button>}
            </form>
        </div>
    );
}

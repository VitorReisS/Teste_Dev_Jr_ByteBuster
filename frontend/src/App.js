import React, { useState, useEffect } from 'react';
import api from './api';
import FormularioPessoa from './components/formularioPessoa';
import ListaPessoas from './components/listaPessoas';

export default function App() {
  const [pessoas, setPessoas] = useState([]);
  const [pessoaParaEditar, setPessoaParaEditar] = useState(null);

  const buscarDados = async () => {
    try {
      const response = await api.get('/pessoas');
      setPessoas(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    buscarDados();
  }, []);

  const onEditar = (pessoa) => {
    setPessoaParaEditar(pessoa);
  };

  const limparEdicao = () => {
    setPessoaParaEditar(null);
  };

  return (
    <>
      <FormularioPessoa atualizarDados={buscarDados} pessoaParaEditar={pessoaParaEditar} limparEdicao={limparEdicao} />
      <ListaPessoas pessoas={pessoas} atualizarDados={buscarDados} onEditar={onEditar} />
    </>
  );
}

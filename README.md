# **Cadastro de Pessoas - Aplicação CRUD**

Esta aplicação é um sistema básico de cadastro de pessoas (CRUD) que utiliza **Flask**, **MongoDB** e **ReactJS**. Ela permite realizar as operações de **criação**, **leitura**, **atualização** e **exclusão** de pessoas.

## **Funcionalidades**
- Cadastrar novas pessoas.
- Listar todas as pessoas cadastradas.
- Atualizar os dados de uma pessoa existente.
- Deletar uma pessoa cadastrada.

---

## **Estrutura do Projeto**

```plaintext
projeto/
|-- backend/
|   |-- tests
|   |   |-- test_api.py
|   |   |-- __init__.py
|   |-- __init__.py
|   |-- api.py
|   |-- database.py
|   |-- models.py
|   |-- logging_config.py
|-- frontend/
|   |-- src/
|   |   |-- components/
|   |   |   |-- personForm.js
|   |   |   |-- personList.js
|   |   |   |-- personItem.js
|   |   |-- app.js
|   |   |-- index.js
|   |   |-- api.js
|   |   |-- styles.css
|   |-- package.json
|-- .env
|-- requirements.txt
```

---

## **Requisitos**

### **Backend**
- Python 3.8 ou superior
- MongoDB
- Flask
- pymongo
- python-dotenv
- pytest

### **Frontend**
- Node.js 16 ou superior
- npm (gerenciador de pacotes)
- ReactJS
- CSS

---

## **Instalação**

### **1. Backend**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/Teste_Dev_Jr_ByteBuster.git
   cd Teste_Dev_Jr_ByteBuster
   ```

2. Configure um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   Crie um arquivo **`.env`** na raiz do diretório **`app/`** com o seguinte conteúdo:
   ```env
   MONGO_URI=mongodb://localhost:27017
   DATABASE_NAME=pessoas_db
   ```

5. Certifique-se de que o MongoDB está rodando no sistema:
   ```bash
   mongod
   ```

6. Inicie o servidor Flask:
   ```bash
   python -m backend.api
   ```

   O backend estará disponível em: [http://localhost:5000](http://localhost:5000)

---

### **2. Frontend**
1. Vá para o diretório do frontend:
   ```bash
   cd frontend
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Inicie o servidor React:
   ```bash
   npm start
   ```

   O frontend estará disponível em: [http://localhost:3000](http://localhost:3000)

---

### **3. Pytest**

1. Inicie o Pytest:
   ```bash
   pytest -v
   ```

Exemplo de Saída Esperada:
```bash
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0 -- C:\Users\Vitor\Downloads\Teste_Defeinitivo\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Vitor\Downloads\Teste_Defeinitivo
plugins: mock-3.14.0
collected 5 items

backend/test/test_api.py::teste_criar_pessoa PASSED                                                                                                            [ 20%]
backend/test/test_api.py::teste_listar_todas_pessoas PASSED                                                                                                    [ 40%]
backend/test/test_api.py::teste_atualizar_pessoa PASSED                                                                                                        [ 60%]
backend/test/test_api.py::teste_deletar_pessoa PASSED                                                                                                          [ 80%]
backend/test/test_api.py::teste_criar_pessoa_cpf_invalido PASSED                                                                                               [100%]

========================================================================== 5 passed in 0.55s ==========================================================================
```

---

## **Como Usar**
1. Acesse o frontend em [http://localhost:3000](http://localhost:3000).
2. Utilize o formulário para adicionar pessoas.
3. Visualize as pessoas cadastradas na lista.
4. Para atualizar um cadastro:
   - Clique no botão **"Editar"** ao lado do registro que deseja alterar.
   - O formulário será preenchido automaticamente com os dados existentes.
   - Atualize as informações desejadas e clique no botão **"Atualizar"**.
   - Para cancelar a edição, clique no botão **"Cancelar Edição"**.
5. Para deletar, clique no botão **"Deletar"**.

---

## **Estrutura de Logs**
Os logs do sistema serão salvos em um arquivo chamado **`app.log`**, localizado no diretório principal. Eles registram todas as operações de leitura e escrita no banco de dados.

---

## **Possíveis Problemas e Soluções**

1. **Erro ao conectar ao MongoDB**:
   - Certifique-se de que o serviço do MongoDB está ativo.
   - Verifique se a URI no arquivo `.env` está correta.

2. **Frontend não encontra o backend**:
   - Confirme que o backend está rodando em [http://localhost:5000](http://localhost:5000).
   - Verifique se há conflitos de porta.

3. **Problemas com dependências**:
   - No backend: Reinstale as dependências com `pip install -r requirements.txt`.
   - No frontend: Use `npm install` para garantir que todos os pacotes estão instalados.

4. **Erro ao atualizar os dados**:
   - Verifique se o CPF informado no banco é único, pois ele é usado como identificador.
   - Certifique-se de que o backend está rodando corretamente e que a API `/pessoas/{cpf}` aceita requisições `PUT`.

5. **Botão "Atualizar" não funciona**:
   - Verifique no console do navegador se há erros relacionados à API.
   - Confirme se o backend está em execução em [http://localhost:5000](http://localhost:5000).

---

## **Tecnologias Utilizadas**
- **Backend**: Python, Flask, pymongo, dotenv, pytest.
- **Frontend**: ReactJS, Axios.
- **Banco de Dados**: MongoDB.
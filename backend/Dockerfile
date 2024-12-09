# Use uma imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o contêiner
COPY ../requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o restante da aplicação para o contêiner
COPY ./backend /app


# Exponha a porta usada pelo React
EXPOSE 5000

# Define o comando para rodar a aplicação
CMD ["python", "api.py"]

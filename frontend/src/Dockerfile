# Use uma imagem oficial do Node.js
FROM node:16

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo de dependências
COPY package-lock.json package.json ./ 

# Instala as dependências do frontend
RUN npm install

# Copia o restante da aplicação para o contêiner
COPY . .

# Exponha a porta usada pelo React
EXPOSE 3000

# Define o comando para rodar o servidor de desenvolvimento
CMD ["npm", "start"]

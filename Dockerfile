# Usar uma imagem base do Python
FROM python:3

# Configurar o diretório de trabalho
WORKDIR /

# Copiar os arquivos de requisitos e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação
COPY . .

COPY .env .env

# Expor a porta que a aplicação Flask irá rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]

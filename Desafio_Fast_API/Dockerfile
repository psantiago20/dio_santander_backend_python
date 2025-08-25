# Imagem base com Python
FROM python:3.10-slim

# Criar diretório da app
WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Comando padrão para rodar o servidor FastAPI
CMD ["uvicorn", "workout_api.main:app", "--host", "0.0.0.0", "--port", "8000"]

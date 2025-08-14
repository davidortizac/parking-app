FROM python:3.11-slim
WORKDIR /app

# Instalar dependencias del sistema para PostgreSQL
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copiar archivos y requerimientos
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer puerto del backend
EXPOSE 8000

# Comando para iniciar FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
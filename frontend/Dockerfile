# Dockerfile para frontend (React + Vite + TailwindCSS)
FROM node:18-alpine
# Directorio de trabajo
WORKDIR /app
# Copiar archivos de dependencias primero para aprovechar cache
COPY package.json package-lock.json* ./
# Instalar dependencias
RUN npm install
# Copiar el resto de la app
COPY . .
# Exponer el puerto que Vite usa por defecto
EXPOSE 3000
# Comando por defecto: iniciar servidor de desarrollo accesible desde fuera del contenedor
CMD ["npm", "run", "dev", "--", "--host"]
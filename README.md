# 🚗 Gestión de Parqueadero Web

Aplicación web para la gestión de parqueaderos con reservas por franjas horarias, control por tipo de vehículo, pico y placa, sanciones y rotación semanal.

---

## 📦 Tecnologías utilizadas
- Frontend: React + TailwindCSS
- Backend: FastAPI (Python)
- Base de datos: PostgreSQL
- Contenedores: Docker & docker-compose

---

## 🚀 Cómo desplegar localmente

1. **Clona el repositorio:**
```bash
git clone https://github.com/tu-org/parqueadero-app.git
cd parqueadero-app
```

2. **Estructura esperada:**
```
- frontend/
  - Dockerfile
- backend/
  - main.py
  - models.py
  - routers/
  - services/
  - requirements.txt
  - Dockerfile
- docker-compose.yml
```

3. **Levanta todo con Docker:**
```bash
docker-compose up --build
```

- Frontend: http://localhost:3000
- Backend: http://localhost:8000/docs

---

## 🧪 Endpoints disponibles (Swagger UI)
Accede a `/docs` del backend para probar:
- `/usuarios`
- `/vehiculos`
- `/reservas`
- `/dashboard`

---

## 🛡️ Consideraciones de seguridad
- Validación de usuarios sancionados
- Control por pico y placa
- Gestión rotativa por grupos

---

## 📤 Despliegue en producción
- Recomendado detrás de un WAF corporativo
- Usar HTTPS y autenticación
- Base de datos externa o gestionada

---

## 📧 Contacto
Proyecto mantenido por el equipo de desarrollo de infraestructura y automatización.

# 🚀 gemini.md — MiniCommerce MVP

Guía rápida para construir el **MVP de MiniCommerce** en monorepo usando **Flask + Angular + PostgreSQL**.
Este archivo está pensado para ejecución directa, enfoque práctico y velocidad de desarrollo.

---

## 🧠 Descripción del MVP

Aplicación web minimalista de compra de un solo producto:

* Visualización de producto
* Vista detalle
* Formulario de compra
* Confirmación
* Envío automático de email

Arquitectura: **Monorepo**

---

## 🧱 Stack

### Backend

* Python 3.10+
* Flask
* Flask-SQLAlchemy
* Flask-Mail
* psycopg2-binary
* python-dotenv
* PostgreSQL

### Frontend

* Angular
* Standalone components
* Reactive Forms
* HttpClient
* TailwindCSS

---

## 📁 Estructura del Monorepo

> Frontend construido con **Angular + TailwindCSS**

```
Monorepo
│
├── backend/   (Flask API)
│   ├── app/
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── config.py
│   │   └── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/  (Angular)
│   ├── src/app/
│   │   ├── core/
│   │   ├── services/
│   │   ├── pages/
│   │   │   ├── home/
│   │   │   ├── product/
│   │   │   ├── checkout/
│   │   │   └── success/
│   │   ├── components/
│   │   └── app.routes.ts
│
└── README.md
```

---

## ⚙️ Variables de Entorno (.env)

```
DATABASE_URL=postgresql://user:password@localhost:5432/minicommerce
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=correo@gmail.com
MAIL_PASSWORD=app_password
MAIL_DEFAULT_SENDER=MiniCommerce <correo@gmail.com>
SECRET_KEY=supersecretkey
```

---

## 🗄️ Modelo de Datos (PostgreSQL)

### Product

* id (UUID)
* name
* description
* price
* image_url

### Order

* id (UUID)
* name
* last_name
* email
* product_id
* created_at

---

## 🔌 API REST

### Producto

```
GET /api/products
GET /api/products/{id}
```

### Orden

```
POST /api/orders
```

Body:

```json
{
  "name": "Victor",
  "last_name": "Chavez",
  "email": "victor@email.com",
  "product_id": "uuid"
}
```

---

## 📧 Email Automático

Asunto:

```
Confirmación de compra - MiniCommerce
```

Contenido:

```
Hola {name},

Tu compra fue confirmada correctamente.

Producto: {product}
Orden ID: {order_id}

Gracias por tu compra.
MiniCommerce Team
```

---

## 🧭 Flujo del Sistema

```
Usuario
 ↓
Home
 ↓
Card Producto
 ↓
Vista Detalle
 ↓
Formulario
 ↓
Confirmar Compra
 ↓
API Flask
 ↓
Validación
 ↓
Guardar en PostgreSQL
 ↓
Enviar Email
 ↓
Respuesta OK
 ↓
Vista Confirmación
```

---

## 🧩 Componentes Angular

* home
* product
* checkout
* success

Servicios:

* product.service.ts
* order.service.ts

---

## 📌 Backlog MVP

1. Crear monorepo
2. Configurar Flask
3. Conexión PostgreSQL
4. Modelo Product
5. Modelo Order
6. API Products
7. API Orders
8. Envío de email
9. Angular base
10. Vistas
11. Integración frontend-backend
12. Validaciones
13. UX mínimo

---

## 🧪 Criterios de Aceptación

* Compra funcional
* Email real enviado
* Datos persistidos en PostgreSQL
* Flujo completo operativo
* API REST limpia
* Arquitectura clara
* Código modular

---

## 🎯 Objetivo de la Prueba

Demostrar:

* Arquitectura
* Diseño de sistema
* Integración real
* Flujo de negocio
* Clean Code
* Buenas prácticas
* Capacidad fullstack

---

## ⚡ Comandos Rápidos

### Backend

```
python -m venv venv
source venv/bin/activate  # windows: venv\Scripts\activate
pip install -r requirements.txt
python app/main.py
```

### Frontend

```
ng new frontend
cd frontend
ng serve
```

---

## 🏁 Definición Formal del MVP

> Sistema web minimalista de comercio electrónico de un solo producto que permite visualizar, seleccionar, registrar datos del usuario, confirmar compra y enviar correo electrónico automático, construido bajo arquitectura monorepo con Flask, Angular y PostgreSQL.

---

## 🔥 Enfoque

Speed > Complejidad
Calidad > Cantidad
Arquitectura > Features
Flujo real > Mockups

---

## 🧠 Mentalidad

Este MVP no es un demo.
Es una **prueba técnica profesional**.

---

# ✅ LISTO PARA EJECUCIÓN

Este archivo es suficiente para:

* Construir el MVP
* Defender arquitectura
* Presentar diseño
* Justificar decisiones técnicas
* Pasar prueba técnica

---

Si quieres, siguiente paso:
👉 generar `requirements.txt`
👉 generar `config.py`
👉 generar `main.py`
👉 modelos SQLAlchemy
👉 endpoints
👉 estructura Angular

Modo ejecución directa 🚀

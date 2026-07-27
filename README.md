# 🏦 BankSystem

## 📌 Descripción del proyecto

**BankSystem** es un sistema bancario desarrollado en Python que permite gestionar la información de clientes mediante un CRUD (Crear, Leer, Actualizar y Eliminar).

El proyecto aplica conceptos de **Programación Orientada a Objetos (POO)**, manejo de archivos JSON y buenas prácticas de desarrollo utilizando control de versiones con **Git y GitHub mediante GitFlow**.

---

# 🎯 Objetivo del sistema

Desarrollar una aplicación que permita administrar clientes de un sistema bancario de manera organizada, facilitando el registro, consulta, actualización y eliminación de información.

---

# 🚀 Funcionalidades principales

## 👤 Módulo de Clientes

El sistema permite:

✅ Registrar clientes
✅ Listar clientes registrados
✅ Buscar clientes
✅ Actualizar información de clientes
✅ Eliminar clientes

---

# 🛠️ Tecnologías utilizadas

| Tecnología | Descripción                                       |
| ---------- | ------------------------------------------------- |
| 🐍 Python  | Lenguaje principal de desarrollo                  |
| 📦 POO     | Organización del código mediante clases y objetos |
| 📄 JSON    | Almacenamiento de información                     |
| 🌱 Git     | Control de versiones                              |
| 🐙 GitHub  | Repositorio remoto y colaboración                 |
| 🔄 GitFlow | Organización de ramas del proyecto                |

---

# 📂 Estructura del proyecto

```
BankSystem
│
├── src
│   │
│   ├── controllers
│   │   └── cliente_controller.py
│   │
│   ├── models
│   │   └── cliente.py
│   │
│   ├── data
│   │   └── clientes.json
│   │
│   └── main.py
│
└── README.md
```

---

# ⚙️ Instalación y ejecución

## 1. Clonar el repositorio

```bash
git clone https://github.com/felipecastrillom7890-web/BankSystem.git
```

## 2. Entrar al proyecto

```bash
cd BankSystem
```

## 3. Ejecutar el sistema

```bash
py src/main.py
```

---

# 🖥️ Menú del sistema

Al ejecutar el programa se muestra el siguiente menú:

```
========== SISTEMA BANCARIO ==========

1. Registrar cliente
2. Listar clientes
3. Buscar cliente
4. Actualizar cliente
5. Eliminar cliente
6. Salir
```

---

# 💾 Almacenamiento de datos

Los datos de los clientes se almacenan utilizando archivos en formato JSON:

```
src/data/clientes.json
```

Esto permite guardar la información y conservar los registros del sistema.

---

# 🌱 Control de versiones (GitFlow)

El proyecto utiliza una estructura organizada de ramas:

```
main
 |
develop
 |
 ├── feature/mejoras-registro-clientes
 |
 ├── feature/crear-cuentas
 |
 └── feature/solo-crud-clientes
```

Cada nueva funcionalidad se desarrolla en una rama independiente y posteriormente se integra mediante Pull Request.

---

# 📌 Estado actual del proyecto

✅ CRUD de clientes implementado
✅ Registro de clientes funcionando
✅ Almacenamiento en JSON
✅ Control de versiones configurado
✅ Integración mediante Pull Requests

🚧 Próximas mejoras:

* Validaciones avanzadas
* Mejoras de interfaz
* Nuevos módulos bancarios

---

# 👨‍💻 Autor

**Felipe**
Programa: Análisis y Desarrollo de Software (ADSO)
SENA
**Gabriela**
Programa: Análisis y Desarrollo de Software (ADSO)
SENA

---

⭐ Proyecto desarrollado con fines educativos para aplicar principios de programación, POO y gestión profesional de código.
